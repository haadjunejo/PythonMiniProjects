import datetime
class Task:

    def __init__(self,id,title,desc):
        self.id=id
        self.title=title
        self.desc=desc
        self.is_completed=False
        self.created_date= datetime.date.today()

    def mark_completed(self):
        self.is_completed=True

    def mark_incompleted(self):
        self.is_completed=False

    def to_dict(self):
        task_dict = self.__dict__.copy()
        task_dict["created_date"]=str(self.created_date)
        return task_dict