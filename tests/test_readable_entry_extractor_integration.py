# from lib.diary import *
# from lib.diary_entry import *
# from lib.readable_entry_extractor import *

# '''When add multiple diary entries ReadableEntryExtractor extracts
# and returns a the longest readable'''
# def test_extracts_longest_multiple_enties():
#     diary = Diary()
#     entry1 = DiaryEntry("My title 1", "One two three four five")
#     entry2 = DiaryEntry("My title 2", "six seven eight")
#     entry3 = DiaryEntry("My title 3", "nine ten eleven")
#     diary.add(entry1)
#     diary.add(entry2)
#     diary.add(entry3)
#     extractor = ReadableEntryExtractor(diary)
#     assert extractor.extract(2, 3) == ['entry1']

# '''When add multiple diary entries ReadableEntryExtractor#extracts
# and returns readable -> not enough time to read any, returns an ematy list'''
# diary = Diary()
# entry1 = DiaryEntry("My title 1", "One two three four five")
# entry2 = DiaryEntry("My title 2", "six seven eight")
# entry3 = DiaryEntry("My title 3", "nine ten eleven")
# diary.add(entry1)
# diary.add(entry2)
# diary.add(entry3)
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(1, 2) # => []

# '''When add no diary entries ReadableEntryExtractor#extracts
# and returns empty list'''
# diary = Diary()
# extractor = ReadableEntryExtractor(diary)
# extractor.extract(1, 2) # => []