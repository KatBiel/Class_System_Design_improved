from lib.diary import *

'''Initially Diary has no entries'''

def test_diary_no_entries():
    diary = Diary()
    diary.all() == []