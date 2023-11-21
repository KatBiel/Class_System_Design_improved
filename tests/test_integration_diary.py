from lib.diary import *
from lib.diary_entry import *

'''When add multiple diary entries
all  lists them out in the order they were added'''

def test_add_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry("My title 1", "My content 1")
    entry2 = DiaryEntry("My title 2", "My content 2")
    entry3 = DiaryEntry("My title 3", "My content 3")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.all() == [entry1, entry2, entry3]