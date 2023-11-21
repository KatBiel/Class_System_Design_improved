from lib.diary_entry import *

def test_diary_entry():
    entry = DiaryEntry("My title", "My content")
    assert entry.title == "My title"
    assert entry.content == "My content"