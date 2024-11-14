import csv
from datetime import datetime
from task import Task, PersonalTask, WorkTask

class TaskManager:
    def __init__(self, task_file_name = "task_list.csv"):
        self.tasks = [ ]
        self.task_list_file_name = task_file_name
    
    def add_task(self, task):
        """To add elements to list self.task"""
        return self.tasks.append(task)
    
    def get_tasks(self, flag = None):
        """ Lists all tasks or only tasks of a specific type (personal or work)"""
        self.list_tasks = [task for task in self.tasks if isinstance(task, PersonalTask) and flag == "personal" 
                or isinstance(task, WorkTask) and flag == "work"]
        return self.list_tasks
    
    def delete_task(self, task_id):
        """Deletes a task by matching its _task_id; prints a message if the task is not found."""
        # Use of list comprehension
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
       # self.tasks is updated
    
    def save_task(self, filename):
        """Saves all tasks to a CSV file named task_list.csv"""
        filename = self.task_list_file_name
        
        with open(filename,'w', newline='') as file:
            """csv.writer class is used to write data directly to a CSV file."""
            input = csv.writer(file)
            # to write the variable/column names
            input.writerow(["Task_ID","Description","Due Date","Type","Priority"])
            for task in self.tasks:
                if isinstance(task, PersonalTask):
                    input.writerow([task.get_task_id(), task._description, task.due_date, "personal", task.priority])
                elif isinstance(task, WorkTask):
                    input.writerow([task.get_task_id(), task._description, task.due_date, "work", ""])
            
    def load_task(self, filename):
        """ Load all tasks from a CSV file named task_list.csv."""
        filename = self.task_list_file_name
        # we must use try... except to handle any potential exceptions that might occur during the file reading or task creation process.
        try:
            with open(filename, 'r', newline='\n') as file:
                output = csv.reader(file)
                next(output)  # jumps the header so that we can load the data
                for row in output:
                    task_id, description, due_date, flag, priority = row
                    if flag == "personal":
                        task = PersonalTask(description, due_date)
                        task.set_priority(priority)
                    elif flag == "work":
                        task = WorkTask(description, due_date)
                        for member in priority.split(","):
                            task.add_team_member(member.strip())

                    else:
                        continue
                    task.task_id = task_id
                    self.tasks.append(task)

        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except (ValueError, IndexError):
            print("Error: Invalid data format in the CSV file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
                
            
    
    def get_pending_tasks(self):
        """ Uses a lambda function to filter and list pending tasks"""
        current_date = datetime.now().date()
        self.pending = list(filter(lambda task: datetime.strptime(task.due_date, "%Y-%m-%d").date() >= current_date, self.tasks))
        return self.pending
    
    def get_overdue_tasks(self):
        """Uses list comprehension to list overdue tasks based on the current date."""
        current_date = datetime.now().date()
        self.overdue = [task for task in self.tasks if datetime.strptime(task.due_date, "%Y-%m-%d").date() < current_date]
        return self.overdue