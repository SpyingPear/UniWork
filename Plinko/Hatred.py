# ===== Importing external modules ===========
import datetime

# ==== Login Section ====
# Load users into a dictionary
users = {}
with open("user.txt", "r") as f:
    for line in f:
        username, password = line.strip().split(", ")
        users[username] = password

# Prompt for login
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    if username_input in users and users[username_input] == password_input:
        print("Login successful!\n")
        break
    else:
        print("Invalid username or password. Please try again.\n")

# ==== Main Menu ====
while True:
    menu = input(
        '''Select one of the following options:
r  - register a user
a  - add task
va - view all tasks
vm - view my tasks
e  - exit
: '''
    ).lower()

    if menu == 'r':
        # Register new user (only allowed for admin)
        if username_input != "admin":
            print("Only the admin can register new users.")
            continue
        new_username = input("Enter new username: ")
        if new_username in users:
            print("This username already exists.")
            continue
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        if new_password == confirm_password:
            with open("user.txt", "a") as f:
                f.write(f"{new_username}, {new_password}\n")
            users[new_username] = new_password
            print("New user registered successfully.\n")
        else:
            print("Passwords do not match. Try again.\n")

    elif menu == 'a':
        # Add a new task
        assigned_to = input("Enter the username to assign the task to: ")
        if assigned_to not in users:
            print("User does not exist.")
            continue
        task_title = input("Enter task title: ")
        task_description = input("Enter task description: ")
        due_date = input("Enter due date (e.g., 25 Oct 2019): ")
        assigned_date = datetime.datetime.today().strftime("%d %b %Y")
        with open("tasks.txt", "a") as f:
            f.write(f"{assigned_to}, {task_title}, {task_description}, {assigned_date}, {due_date}, No\n")
        print("Task added successfully.\n")

    elif menu == 'va':
        # View all tasks
        print("\nAll Tasks:")
        with open("tasks.txt", "r") as f:
            for line in f:
                user, title, description, assigned, due, completed = line.strip().split(", ")
                print(f"\nTask:          {title}")
                print(f"Assigned to:   {user}")
                print(f"Date assigned: {assigned}")
                print(f"Due date:      {due}")
                print(f"Task complete? {completed}")
                print(f"Description:   {description}")
        print()

    elif menu == 'vm':
        # View tasks assigned to current user
        print(f"\nTasks for {username_input}:")
        with open("tasks.txt", "r") as f:
            found = False
            for line in f:
                user, title, description, assigned, due, completed = line.strip().split(", ")
                if user == username_input:
                    found = True
                    print(f"\nTask:          {title}")
                    print(f"Assigned to:   {user}")
                    print(f"Date assigned: {assigned}")
                    print(f"Due date:      {due}")
                    print(f"Task complete? {completed}")
                    print(f"Description:   {description}")
            if not found:
                print("No tasks assigned.\n")

    elif menu == 'e':
        print("Goodbye!!!")
        break

    else:
        print("Invalid input. Please try again.\n")
