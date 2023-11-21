class TaskList():
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        
    def all_incomplete(self):
        # incompleted_list = []
        # for task in self.tasks:
        #     if task.complete == False:
        #         incompleted_list.append(task)
        # return incompleted_list
        return [task for task in self.tasks if task.complete is False]
    
    def all_complete(self): # --> for loop and list comprehension
        # completed_list = []
        # for task in self.tasks:
        #     if task.complete == True:
        #         completed_list.append(task)
        # return completed_list
        return [task for task in self.tasks if task.complete is True]