from lib.task_list import *
from lib.task import *

'''When add multiple tasks, lists them in incomplete'''
def test_add_multiple_tasks():
    task_list = TaskList()
    task1 = Task("Walk the dog")
    task2 = Task("Feed the cats")
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all_incomplete() == [task1, task2]

'''When add multiple tasks, complete returns an ematy list'''
def test_add_multiple_tasks():
    task_list = TaskList()
    task1 = Task("Walk the dog")
    task2 = Task("Feed the cats")
    task_list.add(task1)
    task_list.add(task2)
    assert task_list.all_complete() == []


'''When add multiple tasks, and mark one task as completed'''
def test_add_multiple_and_mark_complete():
    task_list = TaskList()
    task1 = Task("Walk the dog")
    task2 = Task("Feed the cats")
    task_list.add(task1)
    task_list.add(task2)
    task1.mark_complete()
    assert task_list.all_incomplete() == [task2]
    assert task_list.all_complete() == [task1]