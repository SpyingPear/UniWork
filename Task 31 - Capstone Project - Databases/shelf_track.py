import sqlite3

def connect_db():
    conn = sqlite3.connect("ebookstore.db")
    return conn, conn.cursor()

def setup_tables(cursor):
    # Makes sure both tables exist before doing anything
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            country TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            authorID INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            FOREIGN KEY (authorID) REFERENCES author(id)
        )
    ''')

def insert_initial_data(cursor, conn):
    # Only adds this data if the tables are empty
    authors = [
        (1290, "Charles Dickens", "England"),
        (8937, "J.K. Rowling", "England"),
        (2356, "C.S. Lewis", "Ireland"),
        (6380, "J.R.R. Tolkien", "South Africa"),
        (5620, "Lewis Carroll", "England")
    ]
    books = [
        (3001, "A Tale of Two Cities", 1290, 30),
        (3002, "Harry Potter and the Philosopher’s Stone", 8937, 40),
        (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
        (3004, "The Lord of the Rings", 6380, 37),
        (3005, "Alice’s Adventures in Wonderland", 5620, 12)
    ]

    # Checks if tables are empty before inserting
    cursor.execute("SELECT COUNT(*) FROM author")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO author VALUES (?, ?, ?)", authors)

    cursor.execute("SELECT COUNT(*) FROM book")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO book VALUES (?, ?, ?, ?)", books)

    conn.commit()

def get_int(prompt, length=4):
    # Gets an int from user and makes sure it's the correct length
    try:
        val = int(input(prompt).strip())
        if len(str(val)) != length:
            raise ValueError(f"Needs to be {length} digits.")
        return val
    except ValueError as e:
        print("Invalid input:", e)
        return None

def enter_book(cursor, conn):
    print("\n--- Add New Book ---")
    id = get_int("Enter new book ID (4 digits): ")
    if id is None: return

    title = input("Enter title: ").strip()
    authorID = get_int("Enter author ID (4 digits): ")
    if authorID is None: return

    try:
        qty = int(input("Enter quantity: ").strip())
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (id, title, authorID, qty))
        conn.commit()
        print("Book added.")
    except sqlite3.IntegrityError:
        print("Book ID or Author ID already exists or doesn't exist.")
    except Exception as e:
        print("Something went wrong while adding the book:", e)

def update_book(cursor, conn):
    print("\n--- Update Book ---")
    id = get_int("Enter book ID to update: ")
    if id is None: return

    # Gets book & author info
    try:
        cursor.execute('''
            SELECT book.title, book.qty, book.authorID, author.name, author.country
            FROM book
            JOIN author ON book.authorID = author.id
            WHERE book.id = ?
        ''', (id,))
        result = cursor.fetchone()
    except Exception as e:
        print("Error retrieving book:", e)
        return

    if not result:
        print("Book not found.")
        return

    # Shows current info
    print(f"\nCurrent title: {result[0]}")
    print(f"Current quantity: {result[1]}")
    print(f"Author ID: {result[2]}")
    print(f"Author's Name: {result[3]}")
    print(f"Author's Country: {result[4]}")

    option = input("\nWhat do you want to update? (title/qty/authorID): ").strip()
    if option not in ("title", "qty", "authorID"):
        print("Not a valid option.")
        return

    value = input(f"Enter new value for {option}: ").strip()

    try:
        if option in ("qty", "authorID"):
            value = int(value)
        cursor.execute(f"UPDATE book SET {option} = ? WHERE id = ?", (value, id))
        conn.commit()
        print("Book updated.")
    except Exception as e:
        print("Update failed:", e)
        return

    # Ask if the user also wants to update the author details
    update_author = input("\nDo you also want to update the author's name or country? (yes/no): ").strip().lower()
    if update_author == "yes":
        author_id = result[2]
        new_name = input("Enter new author name (leave blank to skip): ").strip()
        new_country = input("Enter new author country (leave blank to skip): ").strip()

        # Only update fields that were filled in
        try:
            if new_name:
                cursor.execute("UPDATE author SET name = ? WHERE id = ?", (new_name, author_id))
            if new_country:
                cursor.execute("UPDATE author SET country = ? WHERE id = ?", (new_country, author_id))
            conn.commit()
            print("Author info updated.")
        except Exception as e:
            print("Couldn't update author info:", e)

def delete_book(cursor, conn):
    print("\n--- Delete Book ---")
    id = get_int("Enter book ID to delete: ")
    if id is None: return

    try:
        cursor.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()

        if cursor.rowcount:
            print("Book deleted.")
        else:
            print("Book not found.")
    except Exception as e:
        print("Something went wrong while deleting:", e)

def search_books(cursor):
    print("\n--- Search Books ---")
    keyword = input("Search by title (or part of it): ").strip()
    cursor.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()

    if results:
        for book in results:
            print(f"ID: {book[0]} | Title: {book[1]} | Author ID: {book[2]} | Qty: {book[3]}")
    else:
        print("No matches found.")

def view_all_books(cursor):
    print("\n--- All Books with Author Info ---")
    cursor.execute('''
        SELECT book.title, author.name, author.country
        FROM book
        INNER JOIN author ON book.authorID = author.id
    ''')
    rows = cursor.fetchall()

    if not rows:
        print("No books in the system.")
        return

    for title, name, country in rows:
        print(f"\nTitle: {title}")
        print(f"Author: {name}")
        print(f"Country: {country}")
        print("-" * 40)

def show_all_details(cursor):
    print("\n--- Full Book Details ---")

    # Pulls info from both book and author tables
    cursor.execute('''
        SELECT book.title, author.name, author.country
        FROM book
        JOIN author ON book.authorID = author.id
    ''')
    results = cursor.fetchall()

    if not results:
        print("No books to display.")
        return

    # Displays in a clean format
    for title, name, country in results:
        print(f"\nTitle: {title}")
        print(f"Author's Name: {name}")
        print(f"Author's Country: {country}")
        print("-" * 50)

def main():
    # Uses with-block so databse closes properly no matter what
    with sqlite3.connect("ebookstore.db") as conn:
        cursor = conn.cursor()
        setup_tables(cursor)
        insert_initial_data(cursor, conn)

        while True:
            print("\n--- Shelf Track Menu ---")
            print("1. Enter book")
            print("2. Update book")
            print("3. Delete book")
            print("4. Search books")
            print("5. View details of all books")
            print("6. View details of all books (with author + country)")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            if choice == '1':
                enter_book(cursor, conn)
            elif choice == '2':
                update_book(cursor, conn)
            elif choice == '3':
                delete_book(cursor, conn)
            elif choice == '4':
                search_books(cursor)
            elif choice == '5':
                view_all_books(cursor)
            elif choice == '6':
                show_all_details(cursor)
            elif choice == '0':
                print("Exiting... Bye!")
                break
            else:
                print("Not a valid choice. Try again.")

if __name__ == "__main__":
    main()