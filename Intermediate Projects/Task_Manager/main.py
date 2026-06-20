from taskmanager import TaskManager


task = TaskManager()
running = True

while running:

    print("-"*25,"Task Manager","-"*25)
    print("Welcome, To Task Manager")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

    try:
        ans = int(input("Enter Any Number From Above : "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if(ans==1):
        print("-"*25,"Add Task","-"*25)
        title = input("Enter Task Title : ")
        desc = input("Enter Task Description : ")
        task.add_task(title,desc)
    
    elif(ans==2):
        print("-"*25,"View All Task","-"*25)
        task.view_tasks()

    elif(ans==3):
        print("-"*25,"Mark Task Complete","-"*25)
        try:
            task_id = int(input("Enter Task ID : "))
            task.mark_task_completed(task_id)
        except ValueError:
            print("Invalid ID! Please enter a number.")

    elif(ans==4):
        print("-"*25,"Delete Task","-"*25)
        try:
            task_id = int(input("Enter Task ID : "))
            task.delete_task(task_id)
        except ValueError:
            print("Invalid ID! Please enter a number.")

    elif(ans==5):
        print("-"*25,"You Decided To Exit!","-"*25)
        task.save_to_file()
        running=False

print("-"*25,"ThankYou For Uisng Task Manager","-"*25)


