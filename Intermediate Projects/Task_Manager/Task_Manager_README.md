# ✅ Task Manager

A Python-based task management application using object-oriented design. Track, organize, and manage your daily tasks with persistent storage and completion status tracking.

## 📋 Features

- **Add Task** - Create new tasks with title and description
- **View All Tasks** - Display all tasks with creation date and status
- **Mark Task Complete** - Mark tasks as done or incomplete
- **Delete Task** - Remove tasks from the system
- **Task Tracking** - Automatic creation date recording
- **Data Persistence** - Save/load tasks using JSON files
- **Status Tracking** - Keep track of completed vs. pending tasks
- **Error Handling** - Robust input validation and exception handling
- **Clean UI** - User-friendly command-line interface

---

## 🏗️ Project Architecture

### **Class 1: Task**

Represents a single task in the system with completion tracking and date management.

**Attributes:**
- `id` - Unique task identifier
- `title` - Task name/title
- `desc` - Detailed task description
- `is_completed` - Boolean status (True/False)
- `created_date` - Date task was created (auto-generated)

**Methods:**

| Method | Purpose |
|--------|---------|
| `mark_completed()` | Mark task as done |
| `mark_incompleted()` | Mark task as incomplete |
| `to_dict()` | Convert task to dictionary for JSON serialization |

**Usage Example:**
```python
task = Task(1, "Buy groceries", "Get milk, eggs, and bread")
print(task.is_completed)  # False
task.mark_completed()
print(task.is_completed)  # True
```

---

### **Class 2: TaskManager**

Core class managing all task operations, persistence, and ID generation.

**Attributes:**
- `tasks` - List of Task objects
- `filepath` - Path to JSON file for storage
- `next_id` - Counter for generating unique task IDs

**Key Methods:**

| Method | Purpose |
|--------|---------|
| `add_task(title, desc)` | Create and add new task |
| `view_tasks()` | Display all tasks |
| `mark_task_completed(task_id)` | Mark specific task as complete |
| `delete_task(task_id)` | Remove task by ID |
| `save_to_file()` | Persist tasks to JSON |
| `load_from_file()` | Load tasks from JSON |

---

### **Method Details**

#### **add_task(title, desc)**

Adds a new task to the system.

**Parameters:**
```python
title = "Buy groceries"
desc = "Get milk, eggs, and bread from the store"
```

**Logic:**
- Create Task object with next available ID
- Add to tasks list
- Increment next_id counter
- Automatically records current date

**Example:**
```python
task_manager = TaskManager()
task_manager.add_task("Buy groceries", "Get milk, eggs, and bread")
# Output: New Task Successfully Added!
```

---

#### **view_tasks()**

Displays all tasks in a formatted manner.

**Output Format:**
```
------------------------- Tasks -------------------------
Id : 1
Title : Buy groceries
description : Get milk, eggs, and bread
Creation Date : 2026-06-20
Status : False
-----
Id : 2
Title : Wash car
description : Wash car before dad wakes up
Creation Date : 2026-06-19
Status : False
```

**Logic:**
- Check if tasks list is empty
- Display message if no tasks exist
- Loop through and format each task
- Show ID, title, description, date, and completion status

---

#### **mark_task_completed(task_id)**

Marks a specific task as complete.

**Parameters:**
```python
task_id = 1  # ID of task to mark complete
```

**Logic:**
- Search for task by ID
- Call task's `mark_completed()` method
- Set `is_completed` to True
- Display success/error message

**Example:**
```python
task_manager.mark_task_completed(1)
# Output: Task marked as complete
# OR: No Task Found!
```

---

#### **delete_task(task_id)**

Removes a task from the system by ID.

**Parameters:**
```python
task_id = 1  # ID of task to delete
```

**Logic:**
- Filter tasks list to exclude task with matching ID
- Use list comprehension for clean removal
- Display success message

**Example:**
```python
task_manager.delete_task(1)
# Output: Task Successfully Deleted!
```

---

#### **save_to_file()**

Persists all tasks to JSON file.

**Logic:**
- Convert each task to dictionary using `to_dict()`
- Handle date serialization (convert to string)
- Write to JSON file with pretty formatting

**File Output:**
```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "desc": "Get milk, eggs, and bread",
        "is_completed": false,
        "created_date": "2026-06-20"
    },
    {
        "id": 2,
        "title": "Wash car",
        "desc": "Wash car before dad wakes up",
        "is_completed": false,
        "created_date": "2026-06-19"
    }
]
```

---

#### **load_from_file()**

Loads saved tasks from JSON file.

**Logic:**
- Read JSON file from disk
- Loop through each task dictionary
- Recreate Task objects with saved data
- Restore completion status
- Convert date string back to date object
- Update next_id to prevent ID conflicts
- Handle missing files gracefully

**Error Handling:**
- Catches `FileNotFoundError` (first run)
- Catches `JSONDecodeError` (corrupted data)
- Prints friendly message on error
- Starts fresh with empty task list

---

## 🚀 Installation & Setup

### Requirements
- Python 3.7+
- No external dependencies (uses built-in libraries only)

### Clone Repository
```bash
git clone https://github.com/yourusername/PythonMiniProjects.git
cd PythonMiniProjects/Task_Manager
```

### Important: Update File Path
In `taskmanager.py`, update the filepath:

**Current (Windows):**
```python
self.filepath = r"D:\CS 6th sem books\...\tasks.json"
```

**Better (Relative Path - Recommended):**
```python
self.filepath = "tasks.json"
```

Relative paths make the project portable across different machines!

### Run the Application
```bash
python main.py
```

---

## 📖 How to Use

### Main Menu
```
======================== Task Manager ========================
Welcome, To Task Manager
1. Add Task
2. View All Tasks
3. Mark Task Complete
4. Delete Task
5. Exit
```

### Example Usage Flow

#### **Step 1: Add First Task**
```
Enter Any Number From Above : 1
--------------------------- Add Task ---------------------------
Enter Task Title : Buy groceries
Enter Task Description : Get milk, eggs, and bread
✓ New Task Successfully Added!
```

#### **Step 2: Add Second Task**
```
Enter Any Number From Above : 1
--------------------------- Add Task ---------------------------
Enter Task Title : Wash car
Enter Task Description : Wash car before dad wakes up
✓ New Task Successfully Added!
```

#### **Step 3: View All Tasks**
```
Enter Any Number From Above : 2
--------------------------- View All Task ---------------------------
Id : 1
Title : Buy groceries
description : Get milk, eggs, and bread
Creation Date : 2026-06-20
Status : False

Id : 2
Title : Wash car
description : Wash car before dad wakes up
Creation Date : 2026-06-19
Status : False
```

#### **Step 4: Mark Task Complete**
```
Enter Any Number From Above : 3
--------------------------- Mark Task Complete ---------------------------
Enter Task ID : 1
✓ Task marked as complete
```

#### **Step 5: Delete Task**
```
Enter Any Number From Above : 4
--------------------------- Delete Task ---------------------------
Enter Task ID : 2
✓ Task Successfully Deleted!
```

#### **Step 6: Exit & Save**
```
Enter Any Number From Above : 5
--------------------------- You Decided To Exit! ---------------------------
✓ Tasks saved to tasks.json
```

---

## 💾 Data Storage

### **tasks.json**
Stores all task records in JSON format:

```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "desc": "Get milk, eggs, and bread",
        "is_completed": false,
        "created_date": "2026-06-20"
    },
    {
        "id": 2,
        "title": "Wash car",
        "desc": "Wash car before dad wakes up",
        "is_completed": true,
        "created_date": "2026-06-19"
    }
]
```

**Fields:**
- `id` - Unique task identifier
- `title` - Task name
- `desc` - Task description
- `is_completed` - Boolean completion status
- `created_date` - ISO format date (YYYY-MM-DD)

---

## 🎯 Key Learning Concepts

This project demonstrates:

✅ **Object-Oriented Programming**
- Class design and encapsulation
- Methods and attributes
- Object serialization

✅ **Date/Time Handling**
- Working with Python's `datetime` module
- Date object creation and manipulation
- Date serialization for JSON compatibility

✅ **File I/O & JSON**
- Reading from JSON files
- Writing to JSON files
- Handling date serialization edge cases
- Error handling for file operations

✅ **Data Structures**
- Lists and list operations
- Dictionaries for object representation
- List comprehensions for filtering

✅ **Error Handling**
- Try-except blocks
- Multiple exception types
- Input validation
- User-friendly error messages

✅ **Clean Code Principles**
- Single responsibility (Task vs. TaskManager)
- Separation of concerns
- Reusable methods
- Clear naming conventions

---

## 🔄 Application Flow

```
START
  ↓
Initialize TaskManager
  ↓
Load tasks from file (tasks.json)
  ↓
Display Main Menu
  ↓
┌─────────────────────────────────────┐
│ Get User Input (1-5)                │
├─────────────────────────────────────┤
│ Option 1 → Add Task                 │
│   ├─ Get title & description        │
│   ├─ Create Task object             │
│   └─ Add to list                    │
│                                     │
│ Option 2 → View All Tasks           │
│   └─ Display formatted list         │
│                                     │
│ Option 3 → Mark Complete            │
│   ├─ Get task ID                    │
│   └─ Update completion status       │
│                                     │
│ Option 4 → Delete Task              │
│   ├─ Get task ID                    │
│   └─ Remove from list               │
│                                     │
│ Option 5 → Exit                     │
│   ├─ Save to file                   │
│   └─ Break loop                     │
└─────────────────────────────────────┘
  ↓
Loop back to menu (unless quit)
  ↓
Display exit message
  ↓
END
```

---

## 🐛 Error Handling

The system handles:
- ✓ Invalid menu input (non-integer)
- ✓ Invalid task ID input (non-integer)
- ✓ Missing JSON file (first run)
- ✓ Corrupted JSON data
- ✓ Task not found scenarios
- ✓ Empty task list

**Error Messages:**
```
Invalid input! Please enter a number.
Invalid ID! Please enter a number.
No Task Found!
No Tasks!
No previous tasks found. Starting fresh!
```

---

## 📁 File Structure

```
Task_Manager/
├── main.py              # Main program with menu loop
├── task.py              # Task class definition
├── taskmanager.py       # TaskManager class with CRUD operations
├── tasks.json           # Task database (auto-created/updated)
└── README.md           # This file
```

---

## ✨ Unique Features

### **Automatic Date Tracking**
Each task automatically records the creation date using `datetime.date.today()`. This is handled transparently by the Task class.

### **Completion Status Toggle**
Tasks can be marked complete or incomplete:
```python
task.mark_completed()      # Set to True
task.mark_incompleted()    # Set to False
```

### **Efficient Task Lookup**
TaskManager efficiently finds and modifies tasks using ID-based lookup.

### **Data Integrity**
- Date conversion for JSON compatibility
- Dictionary copying prevents unintended mutations
- ID auto-increment prevents conflicts

---

## 📈 Usage Statistics

**Example Workflow:**
```
Session 1:
  - Add 5 tasks
  - Exit (auto-saves)
  
Session 2:
  - Load 5 tasks
  - Mark 2 complete
  - Delete 1 task
  - Add 3 new tasks
  - Exit (8 tasks total saved)
  
Session 3:
  - Load 8 tasks
  - Continue managing...
```

---

## ⚠️ Important Notes

### File Path Configuration
The filepath in `taskmanager.py` should use relative path:

**Current:**
```python
self.filepath = r"D:\CS 6th sem books\Summer2026\Python\PythonMiniProjects\Task_Manager\tasks.json"
```

**Recommended:**
```python
self.filepath = "tasks.json"  # Auto-creates in current directory
```

### Date Handling
The Task class uses `datetime.date.today()` which returns the system date. This is serialized to ISO format (YYYY-MM-DD) for JSON storage.

---

## 🚀 Future Enhancements

### Short Term
- [ ] Add priority levels (high, medium, low)
- [ ] Add due date functionality
- [ ] Add task categories/tags
- [ ] Sort tasks by creation date or priority
- [ ] Search tasks by keyword

### Medium Term
- [ ] Add recurring tasks
- [ ] Add task reminders
- [ ] Create GUI with tkinter
- [ ] Add task history/archive
- [ ] Add statistics (tasks completed, etc.)

### Long Term
- [ ] Build web application with Flask
- [ ] Database integration (SQLite/MySQL)
- [ ] Multi-user support
- [ ] Cloud synchronization
- [ ] Mobile app version

---

## 💡 Refactoring Ideas

The current implementation could be enhanced by:

1. **Add Validation**
   ```python
   if not title or not desc:
       print("Title and description cannot be empty!")
   ```

2. **Add Timestamps**
   ```python
   self.completed_date = None  # Set when marked complete
   ```

3. **Add Priority**
   ```python
   def __init__(self, id, title, desc, priority="normal"):
       self.priority = priority
   ```

4. **Add Statistics**
   ```python
   def get_completion_rate(self):
       completed = sum(1 for t in self.tasks if t.is_completed)
       return (completed / len(self.tasks)) * 100
   ```

---

## 📚 Learning Path

This project teaches:
1. **Beginner** - Basic class design and file I/O
2. **Intermediate** - CRUD operations and data persistence
3. **Advanced** - Date handling, JSON serialization, error management

**Next Projects After This:**
- Weather App (API integration)
- Movie Recommendation System (advanced OOP)
- Data Analysis Project (pandas, visualization)

---

## 👨‍💻 Author

Muhammad Haad

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Feel free to fork and submit pull requests for improvements!

---

**Happy Task Managing! ✅**
