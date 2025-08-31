# Create the MVC responsibilities plain text file
content = """MVC Responsibilities — Task Manager

Models
- Task: id, title, description, dueDate, status. Behavior: markComplete().
- Status (enum): PENDING, IN_PROGRESS, DONE.
- TaskRepository: CRUD for Task, backed by FileStore. Ensures IDs are unique, maps to/from JSON.
- FileStore: low-level file I/O (read/write tasks.json), no business rules.

Views
- TaskView: shows lists, single task details, forms, confirmations, and errors.
- Only presentation/formatting; no business logic or file I/O.

Controllers
- TaskController: coordinates between View and Repository.
- Validates input (required fields, date format), constructs Task objects.
- Calls repository methods for create/list/find/update/delete/toggle complete.
- Handles errors from Repository/FileStore and tells the View what to show.
- No rendering or file system access here.

Separation of Concerns
- Models encapsulate data + domain behavior; persistence isolated in FileStore.
- Views render UI/state to the user; they don’t know how data is stored.
- Controllers orchestrate flows and validation; they don’t render or read/write files.
"""
path = "/mnt/data/mvc_responsibilities.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)

path
