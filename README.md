# Simple Command-Line To-Do List

This is a simple Python command-line To-Do List application. You can add, view, and remove tasks. Tasks are saved in a `todo.txt` file in the same directory, so your list is preserved between runs.

## Features

- Add new tasks
- View all tasks
- Remove tasks by number
- Tasks are saved automatically

## Usage

1. **Run the app:**
   ```
   python todolist.py
   ```

2. **Choose an option:**
   - `[1] Show` — View your current tasks
   - `[2] Add` — Add a new task
   - `[3] Remove` — Remove a task by its number
   - `[4] Quit` — Exit the app

## Example

```
Options: [1] Show [2] Add [3] Remove [4] Quit
Choose an option: 2
Enter new task: Buy groceries
Task added.

Options: [1] Show [2] Add [3] Remove [4] Quit
Choose an option: 1
Your tasks:
1. Buy groceries
