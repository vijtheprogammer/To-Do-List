# 📝 Command-Line To-Do List App

This is a simple, interactive command-line to-do list application written in Python. It allows you to view, add, and delete tasks stored in `.txt` files. Designed with user-friendly prompts and animations for a smooth experience.

---

## 📦 Features

- ✅ View tasks from a `.txt` file
- ➕ Add tasks line-by-line
- ❌ Delete tasks by number
- 🔒 Handles input errors and invalid file types
- 🧹 Clears terminal screen for a clean interface
- ⏳ Loading animations for a smoother UX
- 🚪 Graceful exit support (even via `Ctrl+C`)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### How to Run

```bash
python todo.py

Welcome to your To-Do List!
---------------------------

Please select an option:

1. View Tasks
2. Add Task
3. Delete Task
4. Exit

> 2

Please specify the .txt file below
File name: daily_tasks.txt
...
Please enter one task per line. Press 'q' to quit.
Task: Buy groceries
Task: Email project report
Task: Call mom
Task: q

All tasks have been written successfully!


Please select an option:

1. View Tasks
2. Add Task
3. Delete Task
4. Exit

> 1

Please specify a filename (or type exit to cancel). 
File: daily_tasks.txt

Tasks
-----

1. Buy groceries
2. Email project report
3. Call mom
