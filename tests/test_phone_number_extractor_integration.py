from lib.diary import *
from lib.diary_entry import *
from lib.phone_number_extractor import *

'''When add multiple diary entries PhoneNumberExtractor extracts
and returns a list of phone numbers from all diary entry contents'''
def test_extract_phone_number_from_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry("My title 1", "My friend is 07800000000 and 07800000001")
    entry2 = DiaryEntry("My title 2", "My content 2")
    entry3 = DiaryEntry("My title 3", "My friend is 07800000002")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == ['07800000000', '07800000001', '07800000002']

'''When add multiple diary entries PhoneNumberExtractor extracts
and returns a list of phone numbers and ignores invalid numbers'''
def test_extract_ignore_invalid():
    diary = Diary()
    entry1 = DiaryEntry("My title 1", "My friend is 078000000000 and 078000223")
    entry2 = DiaryEntry("My title 2", "My content 234556")
    diary.add(entry1)
    diary.add(entry2)
    extractor = PhoneNumberExtractor(diary)
    extractor.extract() == []

# '''When add multiple diary entries PhoneNumberExtractor extracts
# and returns a list of phone numbers from all diary entry contents
# and ignores duplicates'''
def test_extract_ignore_duplicates():
    diary = Diary()
    entry1 = DiaryEntry("My title 1", "My friend is 07800000000 and 07800000001")
    entry2 = DiaryEntry("My title 2", "My friend is 07800000001")
    diary.add(entry1)
    diary.add(entry2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == ['07800000000', '07800000001']

# '''When add no diary entries PhoneNumberExtractor#extracts
# and returns empty list'''
def test_extract_for_empty_entry():
    diary = Diary()
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == []
