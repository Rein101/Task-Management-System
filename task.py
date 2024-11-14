from datetime import datetime

class Task:
    _id_counter = 0
    def __init__(self,title, due_date, flag, status = 'Pending',description = None):
        Task._id_counter += 1 # Private to prevent access or alterations
        self._task_id = Task._id_counter
        
        self.title = title
        self.due_date = due_date
        self.status = status
        self._description = description 
        self.flag = flag

    def due_date_ddmmyyyy(self):
        # To make the date date easily readable, We must handle the input using strptime() and strftime()
        date = datetime.strptime(self.due_date, "%Y-%m-%d") # to convert a string to a datetime object
        return date.strftime("%d%m%Y") # to convert to their string representation.
    
    def get_task_id(self):
        return self._task_id
        
    def set_description(self, description):
        if len(description) > 15:
            raise ValueError("Description exceeds 15 characters: Invalid")
        self._description = description

    def get_description(self):
        return self._description   
    
    def mark_complete(self):
        self.status = "Completed"
        return self.status
        
    def __str__(self):
        return f'Task ID : {self._task_id},Task : {self.title}, Due Date(dd-mm-yyyy): {self.due_date}, Status: {self.status}, Description: {self._description}, Task Type: {self.flag}'

## Subclass PersonalTask
class PersonalTask(Task):
    def __init__(self, description, due_date, priority = 'low'):
        # super().__init__(title,date,flag) # states the parent class constructors. no need for overriding
        self.priority = priority
        
    def set_priority(self, priority):
        priority_options = ['high','medium','low']
        if priority.lower() in priority_options:
            self.priority = priority.lower()
        else:
            print("Not a Valid Priority!")
    
    def is_priority(self):
        if self.priority.lower() == 'high':
            return True
        else:
            return False
    def __str__(self):
        return  super().__str__() + f', Team: {", ".join(self.priority)}'
        
class WorkTask(Task):
    def __init__(self):
        # super().__init__(title, date, flag)
        self.team_member = [ ]
        
    def add_team_member(self, member):
        self.member = member
        return self.team_member.append(self.member)
    
    def __str__(self):
        return super().__str__() + f', Team: {", ".join(self.team_member)}'