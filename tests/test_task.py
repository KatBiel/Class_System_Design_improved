from lib.task import *

def test_task_contruction():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"