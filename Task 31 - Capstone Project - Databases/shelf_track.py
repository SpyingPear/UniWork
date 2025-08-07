import sqlite3

# Create and connects to database
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# Creates table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        authorID INTEGER,
        qty INTEGER
    )
''')

# Inserts initial data 
initial_books = [
    (3001, "A Tale of Two Cities", 1290, 30),
    (3002, "Harry Potter and the Philosopher’s Stone", 8937, 40),
    (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
    (3004, "The Lord of the Rings", 6380, 37),
    (3005, "Alice’s Adventures in Wonderland", 5620, 12)
]
def enter_book():
    id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    authorID = int(input("Enter author ID: "))
    qty = int(input("Enter quantity: "))
    cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (id, title, authorID, qty))
    conn.commit()
    print("Book added successfully.")

def update_book():
    id = int(input("Enter book ID to update: "))
    column = input("What would you like to update? (title/authorID/qty): ").strip()
    value = input(f"Enter new value for {column}: ")
    cursor.execute(f"UPDATE book SET {column} = ? WHERE id = ?", (value, id))
    conn.commit()
    print("Book updated.")

def delete_book():
    id = int(input("Enter book ID to delete: "))
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    print("Book deleted.")

def search_book():
    keyword = input("Enter book title to search for: ")
    cursor.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()
    for book in results:
        print(book)

# Menu loop
while True:
    print("\n1. Enter book\n2. Update book\n3. Delete book\n4. Search books\n0. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        enter_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_book()
    elif choice == '0':
        break
    else:
        print("Invalid choice.")

conn.close()
