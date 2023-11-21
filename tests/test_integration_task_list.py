# from lib.task_list import *
# from lib.task import *

# '''When add multiple tasks, lists them in incomplete'''
# def test_add_multiple_tasks():
#     task_list = TaskList()
#     task1 = "Walk the dog"
#     task2 = "Feed the cats"
#     task_list.add(task1)
#     task_list.add(task2)
# assert task_list.all_incomplete() == [task1, task2]



# task_list.all_complete() == []
# # this should be broken into two tests

# '''When add multiple tasks, and mark one task as completed'''
# task_list = TaskList()
# task1 = "Walk the dog"
# task2 = "Feed the cats"
# task_list.add(task1)
# task_list.add(task2)
# task1.mark_complete()
# task_list.all_incomplete() == [task2]
# task_list.all_complete() == [task1]