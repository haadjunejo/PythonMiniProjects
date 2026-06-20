from task import Task
import json
import datetime
class TaskManager:

    def __init__(self):
        self.tasks = []
        self.filepath = r"D:\CS 6th sem books\Summer2026\Python\PythonMiniProjects\Task_Manager\tasks.json"
        self.next_id=1
        self.load_from_file()


    def add_task(self,title,desc):
        t = Task(self.next_id,title,desc)
        self.tasks.append(t)
        self.next_id+=1
        print("New Task Successfully Added!")

    def view_tasks(self):
        if(len(self.tasks)==0):
            print("No Tasks!")
            return
        print("-"*25,"Tasks","-"*25)
        for t in self.tasks:
            print(f"Id : {t.id}")        
            print(f"Title : {t.title}")        
            print(f"description : {t.desc}")        
            print(f"Creation Date : {t.created_date}")        
            print(f"Status : {t.is_completed}")        

    def delete_task(self,task_id):
        self.tasks = [t for t in self.tasks if t.id!=task_id]
        print("Task Successfully Deleted!")

    def mark_task_completed(self,task_id):
        for t in self.tasks:
            if(t.id==task_id):
                t.mark_completed()
                break
        else:
            print("No Task Found!")

    def save_to_file(self):
        task_list = []
        for t in self.tasks:
            task_list.append(t.to_dict())

        with open(self.filepath,"w") as f:
            json.dump(task_list,f,indent=4)

    def load_from_file(self):
        try:
            with open(self.filepath,"r") as f :
                data = json.load(f)
                for t in data:
                    task = Task(t["id"], t["title"], t["desc"])
                    task.is_completed = t["is_completed"]  
                    task.created_date = datetime.date.fromisoformat(t["created_date"])
                    self.tasks.append(task)                       

                if self.tasks:
                    self.next_id = max(t.id for t in self.tasks) + 1
        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous tasks found. Starting fresh!")
            pass   