# 👨‍🎓 Student Management System

A Python-based student record management system that allows administrators to add, delete, update, and search student information with persistent JSON storage.

## 📋 Features

- **Add Student** - Register new students with CMS ID, name, department, and CGPA
- **Delete Student** - Remove student records by CMS ID
- **Update Student** - Modify existing student information
- **Search Student** - Find and display specific student details by CMS ID
- **View All Students** - Display all registered students
- **Data Persistence** - Automatic save/load using JSON files
- **Duplicate Prevention** - Prevents duplicate CMS IDs from being added
- **Error Handling** - Comprehensive error checking and validation

---

## 🏗️ Project Architecture

### Modules

#### **main.py**
Main program with interactive menu loop for user operations.

**Menu Options:**
```
1. Add Student
2. Delete Student
3. Update Student
4. Search By CMS ID
5. View All Students
6. Quit
```

**Workflow:**
- User selects an option
- Input is collected
- Function is called from studentManager module
- Results are displayed
- Loop continues until user quits

---

#### **studentManager.py**
Core module containing all CRUD (Create, Read, Update, Delete) operations.

**Key Functions:**

| Function | Purpose |
|----------|---------|
| `add_student(student)` | Add new student to database |
| `delete_student(cms_id)` | Remove student by CMS ID |
| `update_student(updated_student)` | Modify student information |
| `searchBYCms_id(cms_id)` | Find and display student by CMS ID |
| `display_students()` | Show all students in database |

---

### **Function Details**

#### **1. add_student(student)**

Adds a new student to the system.

**Parameters:**
```python
student = {
    "cms_id": "034-34-0400",
    "name": "Ali",
    "dept": "EE",
    "cgpa": "3.8"
}
```

**Logic:**
- Load existing data from JSON file (or create empty list)
- Check for duplicate CMS ID
- Prevent duplicates with error message
- Append new student to data
- Save updated data to JSON file

**Error Handling:**
- Handles missing file (creates new one)
- Handles corrupted JSON data
- Prevents duplicate CMS IDs

---

#### **2. delete_student(cms_id)**

Removes a student from the system by CMS ID.

**Parameters:**
```python
cms_id = "034-34-0400"
```

**Logic:**
- Load data from JSON file
- Filter out student with matching CMS ID
- Check if student was actually found
- Save updated data to file

**Error Handling:**
- Confirms file exists
- Reports if student not found

---

#### **3. update_student(updated_student)**

Modifies existing student information.

**Parameters:**
```python
updated_student = {
    "cms_id": "034-34-0400",
    "name": "Ali Khan",
    "dept": "EE",
    "cgpa": "3.9"
}
```

**Logic:**
- Load data from JSON file
- Search for student by CMS ID
- Update name, department, and CGPA
- Save changes to file

**Error Handling:**
- Confirms file exists
- Reports if student not found

---

#### **4. searchBYCms_id(cms_id)**

Searches for and displays a specific student's information.

**Parameters:**
```python
cms_id = "034-34-0400"
```

**Output:**
```
--- Student Record ---

CMS ID     : 034-34-0400
Name       : Ali
Department : EE
CGPA       : 3.8
------------------------------
```

**Error Handling:**
- Confirms file exists
- Reports if student not found

---

#### **5. display_students()**

Displays all registered students in a formatted table.

**Output:**
```
--- Student Records ---

Student 1
CMS ID     : 034-34-0400
Name       : Ali
Department : EE
CGPA       : 3.8
------------------------------
Student 2
CMS ID     : 050-50-0599
Name       : Tony
Department : BBA
CGPA       : 2.5
------------------------------
```

**Error Handling:**
- Confirms file exists
- Handles empty database
- Handles corrupted JSON

---

## 🚀 Installation & Setup

### Requirements
- Python 3.7+
- No external dependencies (uses built-in libraries only)

### Clone Repository
```bash
git clone https://github.com/yourusername/PythonMiniProjects.git
cd PythonMiniProjects/Student_Management_System
```

### Important: Update File Path
In `studentManager.py`, update the file path:

```python
# Current (Windows example)
file_path = r"D:\CS 6th sem books\Summer2026\Python\PythonMiniProjects\Student_Management_System\students.json"

# Or use relative path (recommended)
file_path = "students.json"
```

Using relative path makes it portable across different machines!

### Run the Application
```bash
python main.py
```

---

## 📖 How to Use

### Main Menu
```
======================== Student Management System ========================
Welcome, To SMS
1 : Add Student
2 : Delete Student
3 : Update Student
4 : Search By CMS ID Student
5 : View Students
6 : Quit
```

### Example Usage Flow

#### **Step 1: Add Student**
```
Press any number from above : 1
--------------------------- Add Student ---------------------------
Enter Student Cms_id : 034-34-0400
Enter Student Name : Ali
Enter Student department : EE
Enter Student Cgpa : 3.8
✓ Student added successfully
```

#### **Step 2: Add Another Student**
```
Press any number from above : 1
--------------------------- Add Student ---------------------------
Enter Student Cms_id : 050-50-0599
Enter Student Name : Tony
Enter Student department : BBA
Enter Student Cgpa : 2.5
✓ Student added successfully
```

#### **Step 3: View All Students**
```
Press any number from above : 5
--- Student Records ---

Student 1
CMS ID     : 034-34-0400
Name       : Ali
Department : EE
CGPA       : 3.8
------------------------------
Student 2
CMS ID     : 050-50-0599
Name       : Tony
Department : BBA
CGPA       : 2.5
------------------------------
```

#### **Step 4: Search Student**
```
Press any number from above : 4
--------------------------- Search By CmsID Student ---------------------------
Enter cms_id of student : 034-34-0400
--- Student Record ---

CMS ID     : 034-34-0400
Name       : Ali
Department : EE
CGPA       : 3.8
------------------------------
```

#### **Step 5: Update Student**
```
Press any number from above : 3
--------------------------- Update Student ---------------------------
Enter cms_id of student : 034-34-0400
Enter Student Updated Name : Ali Khan
Enter Student Updated department : EE
Enter Student Updated Cgpa : 3.9
✓ Student updated successfully
```

#### **Step 6: Delete Student**
```
Press any number from above : 2
--------------------------- Delete Student ---------------------------
Enter cms_id of student : 050-50-0599
✓ Student deleted successfully
```

#### **Step 7: Quit**
```
Press any number from above : 6
--------------------------- Thank You For Visiting Student Management System ---------------------------
```

---

## 💾 Data Storage

### **students.json**
Stores all student records in JSON format:

```json
[
    {
        "cms_id": "034-34-0400",
        "name": "Ali",
        "dept": "EE",
        "cgpa": 3.8
    },
    {
        "cms_id": "050-50-0599",
        "name": "Tony",
        "dept": "BBA",
        "cgpa": 2.5
    }
]
```

**Fields:**
- `cms_id` - Unique student identifier (primary key)
- `name` - Student full name
- `dept` - Department (EE, BBA, CS, etc.)
- `cgpa` - Cumulative GPA (0.0 - 4.0)

---

## 🎯 Key Learning Concepts

This project demonstrates:

✅ **File I/O Operations**
- Reading from JSON files
- Writing to JSON files
- File existence checking with `os.path.exists()`

✅ **JSON Handling**
- Serializing Python dictionaries to JSON
- Deserializing JSON to Python structures
- Error handling for corrupted JSON

✅ **Data Structures**
- Lists and dictionaries
- List comprehensions for filtering
- Dictionary operations

✅ **Error Handling**
- Try-except blocks
- Multiple exception types
- User-friendly error messages

✅ **Procedural Programming**
- Function decomposition
- Separation of concerns (UI vs. logic)
- Reusable functions

✅ **Data Validation**
- Duplicate checking
- Existence verification
- Empty data handling

---

## 🔄 Data Flow

```
START
  ↓
Display Menu
  ↓
Get User Input (1-6)
  ↓
├─ Option 1: Add → Input → Validate → Save
├─ Option 2: Delete → Input → Search → Remove → Save
├─ Option 3: Update → Input → Search → Modify → Save
├─ Option 4: Search → Input → Find → Display
├─ Option 5: View All → Load → Display
└─ Option 6: Quit → Break Loop
  ↓
Loop back to Menu (unless quit)
  ↓
END
```

---

## 🐛 Error Handling

The system handles:
- ✓ Missing JSON file (creates new one)
- ✓ Corrupted JSON data (recovers gracefully)
- ✓ Duplicate CMS IDs (prevents duplicates)
- ✓ Student not found (appropriate messages)
- ✓ Empty database (displays message)
- ✓ File I/O errors

---

## 📁 File Structure

```
Student_Management_System/
├── main.py                 # Main program with menu loop
├── studentManager.py       # Core functions for CRUD operations
├── students.json           # Student database (auto-created)
└── README.md              # This file
```

---

## 🔐 Important Notes

### File Path
The current file path uses absolute path:
```python
file_path = r"D:\CS 6th sem books\...\students.json"
```

**Recommendation:** Use relative path for portability:
```python
file_path = "students.json"
```

This makes the project work on any machine without path changes.

---

## ⚠️ Potential Improvements

The system works well but could be enhanced:

- [ ] Add input validation for CGPA (0-4.0 range)
- [ ] Add error handling for invalid input types
- [ ] Add sorting functionality (by CGPA, name, etc.)
- [ ] Add filtering (by department)
- [ ] Implement OOP design with Student class
- [ ] Add backup/export functionality
- [ ] Add student ID auto-generation
- [ ] Create web interface using Flask
- [ ] Add user authentication
- [ ] Add timestamp for student registration date

---

## 🚀 Future Enhancements

### Short Term
1. **Input Validation**
   - Validate CGPA is between 0-4.0
   - Validate CMS ID format
   - Ensure no empty fields

2. **Search Features**
   - Search by name
   - Search by department
   - Advanced filtering

### Medium Term
3. **Object-Oriented Refactor**
   - Create Student class
   - Create StudentManager class
   - Better encapsulation

4. **Analytics**
   - Average CGPA calculation
   - Department-wise statistics
   - Student count

### Long Term
5. **Web Application**
   - Build with Flask/Django
   - Add GUI with tkinter
   - Database integration (SQLite/MySQL)

---

## 💡 Key Takeaways

- Working with file I/O and JSON
- Building user-friendly CLI applications
- Implementing CRUD operations
- Error handling best practices
- Data persistence strategies
- Function-based architecture

---

## 📚 Learning Path

This project is perfect for:
1. **Beginners** - Learn file I/O and basic data management
2. **Intermediate** - Understand CRUD operations and data persistence
3. **Moving to OOP** - Can be refactored into classes

**Next Steps:**
- Refactor this into OOP (create Student and StudentManager classes)
- Add a GUI with tkinter
- Convert to web application with Flask
- Upgrade to database with SQLite

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

**Happy Coding! 🚀**
