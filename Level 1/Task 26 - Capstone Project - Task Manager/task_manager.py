import sqlite3

# --- Connect to database (or create it if it doesn't exist) ---
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# --- Create the table if it doesn't exist ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        authorID INTEGER,
        qty INTEGER
    )
''')
conn.commit()

# --- Predefined data to populate the table (can skip if already added) ---
def populate_initial_data():
    books = [
        (3001, 'A Tale of Two Cities', 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 2356, 25),
        (3004, 'The Lord of the Rings', 6380, 37),
        (3005, "Alice's Adventures in Wonderland", 5620, 12),
    ]
    try:
        cursor.executemany('INSERT INTO book VALUES (?, ?, ?, ?)', books)
        conn.commit()
    except sqlite3.IntegrityError:
        # Skip if records already exist
        pass

# --- Add new book to the database ---
def enter_book():
    try:
        id = int(input("Enter book ID: "))
        title = input("Enter title: ")
        authorID = int(input("Enter author ID: "))
        qty = int(input("Enter quantity: "))
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (id, title, authorID, qty))
        conn.commit()
        print("Book added successfully.")
    except sqlite3.IntegrityError:
        print("Book with that ID already exists.")
    except ValueError:
        print("Invalid input. Please enter numbers for ID, author ID, and quantity.")

# --- Update an existing book ---
def update_book():
    try:
        id = int(input("Enter book ID to update: "))
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        book = cursor.fetchone()
        if not book:
            print("No book found with that ID.")
            return

        print(f"Current details: ID={book[0]}, Title='{book[1]}', Author ID={book[2]}, Qty={book[3]}")
        new_qty = input("Enter new quantity (leave blank to keep current): ")
        new_authorID = input("Enter new author ID (leave blank to keep current): ")

        qty = int(new_qty) if new_qty else book[3]
        authorID = int(new_authorID) if new_authorID else book[2]

        cursor.execute("UPDATE book SET qty=?, authorID=? WHERE id=?", (qty, authorID, id))
        conn.commit()
        print("Book updated.")
    except ValueError:
        print("Invalid input. Make sure you're entering numbers where required.")

# --- Delete a book from the database ---
def delete_book():
    try:
        id = int(input("Enter the book ID to delete: "))
        cursor.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        if cursor.rowcount:
            print("Book deleted.")
        else:
            print("No book found with that ID.")
    except ValueError:
        print("Please enter a valid numeric ID.")

# --- Search for a specific book ---
def search_book():
    title = input("Enter part or full title to search: ").strip()
    cursor.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + title + '%',))
    results = cursor.fetchall()
    if results:
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Qty: {book[3]}")
    else:
        print("No matching book found.")

# --- Main menu loop ---
def main():
    populate_initial_data()  # Populate only once (skips if data already exists)

    while True:
        print("\n--- Shelf Track Menu ---")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            enter_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_book()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please select from the menu.")

# --- Run the program ---
if __name__ == "__main__":
    main()
    conn.close()