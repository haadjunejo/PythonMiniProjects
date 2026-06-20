import json
import os

file_path = "D:\CS 6th sem books\Summer2026\Python\PythonMiniProjects\Student_Management_System\students.json"



# ---------------- ADD ----------------
def add_student(student):

    if not os.path.exists(file_path):
        data = []
    else:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []

    if not isinstance(data, list):
        data = []

    # duplicate check
    for s in data:
        if s["cms_id"] == student["cms_id"]:
            print("Duplicate CMS ID not allowed")
            return

    data.append(student)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Student added successfully")


# ---------------- DELETE ----------------
def delete_student(cms_id):

    if not os.path.exists(file_path):
        print("File not found")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    new_data = [s for s in data if s["cms_id"] != cms_id]

    if len(new_data) == len(data):
        print("Student not found")
        return

    with open(file_path, "w") as f:
        json.dump(new_data, f, indent=4)

    print("Student deleted successfully")


# ---------------- UPDATE ----------------
def update_student(updated_student):

    if not os.path.exists(file_path):
        print("File not found")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    updated = False

    for s in data:
        if s["cms_id"] == updated_student["cms_id"]:
            s["name"] = updated_student["name"]
            s["dept"] = updated_student["dept"]
            s["cgpa"] = updated_student["cgpa"]
            updated = True
            break

    if not updated:
        print("Student not found")
        return

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print("Student updated successfully")


def searchBYCms_id(cmd_id):
    if not os.path.exists(file_path):
        print("File not found")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    for s in data:
        if(s["cms_id"]==cmd_id):
            print("\n--- Student Record ---\n")        
            print(f"CMS ID     : {s['cms_id']}")
            print(f"Name       : {s['name']}")
            print(f"Department : {s['dept']}")
            print(f"CGPA       : {s['cgpa']}")
            print("-" * 30)
            break
    else:
        print(f"Student of this {cmd_id} cms-id not exist!")        

# ---------------- DISPLAY ----------------
def display_students():

    if not os.path.exists(file_path):
        print("No file found")
        return

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("File is empty or corrupted")
        return

    if not data:
        print("No students available")
        return

    print("\n--- Student Records ---\n")

    for i, s in enumerate(data, start=1):
        print(f"Student {i}")
        print(f"CMS ID     : {s['cms_id']}")
        print(f"Name       : {s['name']}")
        print(f"Department : {s['dept']}")
        print(f"CGPA       : {s['cgpa']}")
        print("-" * 30)