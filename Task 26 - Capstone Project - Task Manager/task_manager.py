import datetime
import os

users = {}
tasks = []

def load_users():
    with open("user.txt", "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            if len(parts) >= 2:
                users[parts[0]] = parts[1]

def load_tasks():
    global tasks
    tasks = []
    with open("tasks.txt", "r") as f:
        for line in f:
            tasks.append(line.strip().split(", "))

def save_tasks():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(", ".join(t) + "\n")

def reg_user():
    while True:
        new_username = input("Enter new username: ")
        if new_username in users:
            print("Username already exists.\n")
            continue
        new_password = input("Enter new password: ")
        confirm = input("Confirm password: ")
        if new_password == confirm:
            with open("user.txt", "a") as f:
                f.write(f"{new_username}, {new_password}\n")
            users[new_username] = new_password
            print("User registered.\n")
            break
        else:
            print("Passwords do not match.\n")

def add_task():
    assigned_to = input("Assign to: ")
    if assigned_to not in users:
        print("User not found.\n")
        return
    title = input("Task title: ")
    desc = input("Task description: ")
    due_date = input("Due date (e.g. 25 Oct 2024): ")
    assigned_date = datetime.datetime.today().strftime("%d %b %Y")
    task = [assigned_to, title, desc, assigned_date, due_date, "No"]
    tasks.append(task)
    save_tasks()
    print("Task added.\n")

def view_all():
    for i, t in enumerate(tasks, 1):
        print(f"\nTask {i}:")
        print(f"  Title:         {t[1]}")
        print(f"  Assigned to:   {t[0]}")
        print(f"  Date assigned: {t[3]}")
        print(f"  Due date:      {t[4]}")
        print(f"  Completed:     {t[5]}")
        print(f"  Description:   {t[2]}")
    print()

def view_mine(current_user):
    user_tasks = [t for t in tasks if t[0] == current_user]
    for i, t in enumerate(user_tasks, 1):
        print(f"\nTask {i}:")
        print(f"  Title:         {t[1]}")
        print(f"  Assigned to:   {t[0]}")
        print(f"  Date assigned: {t[3]}")
        print(f"  Due date:      {t[4]}")
        print(f"  Completed:     {t[5]}")
        print(f"  Description:   {t[2]}")
    if not user_tasks:
        print("No tasks assigned.\n")
        return
    try:
        selection = int(input("\nEnter task number to select or -1 to return: "))
        if selection == -1:
            return
        task_index = tasks.index(user_tasks[selection - 1])
        if tasks[task_index][5].lower() == "yes":
            print("Task already completed.\n")
            return
        action = input("Enter 'c' to complete or 'e' to edit: ").lower()
        if action == 'c':
            tasks[task_index][5] = "Yes"
            save_tasks()
            print("Marked complete.\n")
        elif action == 'e':
            edit_user = input("New user (leave blank to keep): ")
            edit_due = input("New due date (leave blank to keep): ")
            if edit_user and edit_user in users:
                tasks[task_index][0] = edit_user
            if edit_due:
                tasks[task_index][4] = edit_due
            save_tasks()
            print("Task updated.\n")
    except (IndexError, ValueError):
        print("Invalid selection.\n")

def view_completed():
    for i, t in enumerate(tasks, 1):
        if t[5].lower() == "yes":
            print(f"\nTask {i}:")
            print(f"  Title:         {t[1]}")
            print(f"  Assigned to:   {t[0]}")
            print(f"  Date assigned: {t[3]}")
            print(f"  Due date:      {t[4]}")
            print(f"  Completed:     {t[5]}")
            print(f"  Description:   {t[2]}")
    print()

def delete_task():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t[1]} (assigned to {t[0]})")
    try:
        selection = int(input("Enter task number to delete: "))
        if 1 <= selection <= len(tasks):
            del tasks[selection - 1]
            save_tasks()
            print("Task deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")

def generate_reports():
    total = len(tasks)
    completed = sum(1 for t in tasks if t[5].lower() == "yes")
    incomplete = total - completed
    overdue = sum(1 for t in tasks if t[5].lower() == "no" and datetime.datetime.strptime(t[4], "%d %b %Y") < datetime.datetime.today())
    perc_incomplete = (incomplete / total * 100) if total else 0
    perc_overdue = (overdue / total * 100) if total else 0

    with open("task_overview.txt", "w") as f:
        f.write(f"Total tasks: {total}\n")
        f.write(f"Completed tasks: {completed}\n")
        f.write(f"Incomplete tasks: {incomplete}\n")
        f.write(f"Overdue tasks: {overdue}\n")
        f.write(f"% Incomplete: {perc_incomplete:.2f}%\n")
        f.write(f"% Overdue: {perc_overdue:.2f}%\n")

    with open("user_overview.txt", "w") as f:
        f.write(f"Total users: {len(users)}\n")
        f.write(f"Total tasks: {total}\n\n")
        for user in users:
            user_tasks = [t for t in tasks if t[0] == user]
            u_total = len(user_tasks)
            if total == 0 or u_total == 0:
                f.write(f"{user}: 0 tasks assigned.\n\n")
                continue
            u_completed = sum(1 for t in user_tasks if t[5].lower() == "yes")
            u_incomplete = u_total - u_completed
            u_overdue = sum(1 for t in user_tasks if t[5].lower() == "no" and datetime.datetime.strptime(t[4], "%d %b %Y") < datetime.datetime.today())
            f.write(f"{user}:\n")
            f.write(f"  Total tasks assigned: {u_total}\n")
            f.write(f"  % of total tasks: {(u_total / total * 100):.2f}%\n")
            f.write(f"  % completed: {(u_completed / u_total * 100):.2f}%\n")
            f.write(f"  % incomplete: {(u_incomplete / u_total * 100):.2f}%\n")
            f.write(f"  % overdue: {(u_overdue / u_total * 100):.2f}%\n\n")
    print("Reports generated.\n")

def display_statistics():
    if not os.path.exists("task_overview.txt") or not os.path.exists("user_overview.txt"):
        generate_reports()
    print("\nTask Overview:")
    with open("task_overview.txt", "r") as f:
        print(f.read())
    print("User Overview:")
    with open("user_overview.txt", "r") as f:
        print(f.read())

load_users()
load_tasks()

while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    if username_input in users and users[username_input] == password_input:
        print("\nLogin successful.\n")
        break
    else:
        print("Invalid login. Try again.\n")

while True:
    if username_input == "admin":
        menu = input('''Please select one of the following options:
r   - register user
a   - add task
va  - view all tasks
vm  - view my tasks
vc  - view completed tasks
del - delete a task
ds  - display statistics
gr  - generate reports
e   - exit
: ''').lower()
    else:
        menu = input('''Please select one of the following options:
a   - add task
va  - view all tasks
vm  - view my tasks
e   - exit
: ''').lower()

    if menu == 'r' and username_input == "admin":
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(username_input)
    elif menu == 'vc' and username_input == "admin":
        view_completed()
    elif menu == 'del' and username_input == "admin":
        delete_task()
    elif menu == 'gr' and username_input == "admin":
        generate_reports()
    elif menu == 'ds' and username_input == "admin":
        display_statistics()
    elif menu == 'e':
        print("Goodbye!")
        break
    else:
        print("Invalid option.\n")
