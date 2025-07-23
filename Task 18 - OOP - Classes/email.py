#Just a note I had a friend help me fix the code, I got stuck withh the populate inbox
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

inbox = []  

def populate_inbox():
    inbox.append(Email("welcome@hyperiondev.com", "Welcome to HyperionDev!", "Thanks for joining"))
    inbox.append(Email("bootcamp@hyperiondev.com", "Great work on the bootcamp!", "Keep up the great effort!"))
    inbox.append(Email("results@hyperiondev.com", "You scored 95% on your last test!", "Well done on the excellent results!"))

def list_emails():
    if not inbox:
        print("Inbox is empty.")
        return
    for i, email in enumerate(inbox):
        status = "Unread" if not email.has_been_read else "Read"
        print(f"{i}: {email.subject_line} ({status})")

def read_email(index):
    if index < 0 or index >= len(inbox):
        print("Invalid index.")
        return
    email = inbox[index]
    print(f"\nFrom: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content:\n{email.email_content}\n")
    email.mark_as_read()
    print("Email marked as read.\n")

def view_unread_emails():
    unread = [(i, email) for i, email in enumerate(inbox) if not email.has_been_read]
    if not unread:
        print("No unread emails.")
        return
    for i, email in unread:
        print(f"{i}: {email.subject_line}")

populate_inbox()

while True:
    print("\nMenu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Enter selection: ")

    if choice == "1":
        list_emails()
        try:
            idx = int(input("Enter email index to read: "))
            read_email(idx)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        view_unread_emails()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid input.")