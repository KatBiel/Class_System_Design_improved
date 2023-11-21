## 1. Describe the Problem

'''
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
'''

## 2. Design the Class System
'''
# Nouns
Diary
DiaryEntry
wpm / reading speed
Tasks 
Todo
Contacts -> mobile phones
list

# verbs
keep track
reflect
read diary enrey
select 
see a list
'''

'''
python
'''
class Diary():
    def add(self, diary_entry):
        # diary entry: instance of DiaryEntry
        # returns nothing
        # side-effects: ads diary entry to entry list
        pass

    def all(self):
        # returns a list of all DiaryEntry instances
        pass

class DiaryEntry():
    #(expose properties) 
    #Public Properties:
    #title: string representing title
    #contents: string representing entry contents
    pass

    def __init__(self, title, content):
        #title: string representing title
        #contents: string representing entry contents
        #side effects: sets the above properties
        pass


class TaskList():
    def add(self, task):
        # task: instance of Task
        # returns nothing
        # side-effects: ads task to task list
        pass
        
    def all_incomplete():
        # returns a list of instances of Task 
        # represented by incompleted tasks
        pass

    def all_complete(): #--> for loop and list comprehension
        # returns a list of instances of Task 
        # represented by completed tasks
        pass


class Task():
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, title):
        #Title: string representing a task to complete
        #Side-effects: 
        #sets the task property 
        #sets the complete property
        pass
        
    def mark_complete(self):
        # Side-effects: sets the task property to False
        # returns nothing

class PhoneNumberExtractor():

    def __init__(self, diary):
        # diary: an instance of a Diary
        # Side-effect: set diary property
        pass

## Side-effect -> This comment is indicating that the primary purpose 
## of the __init__ method is to initialize the diary property of the 
## PhoneNumberExtractor instance with the value passed as the diary parameter.
    
    def extract(self):
        #returns: extracts contact numbers and returns as a list
        pass

class ReadableEntryExtractor():

    def __init__(self, diary):
        # diary: an instance of Diary
        # Side-effect: set diary property
        pass
    
    def extract(self, wpm, time):
        # wpm: integer
        # time: integer, time in minutes
        # returns the longer diary entry that can be read 
        # in the given time and speed
        pass

'''
'''
## 3. Create Examples as Integration Tests

#Diary

'''When add multiple diary entries
all  lists them out in the order they were added'''
diary = Diary()
entry1 = DiaryEntry("My title 1", "My content 1")
entry2 = DiaryEntry("My title 2", "My content 2")
entry3 = DiaryEntry("My title 3", "My content 3")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.all() # => [entry1, entry2, entry3]

''''''

# TaskList

'''When add multiple tasks, lists them in incomplete'''
task_list = TaskList()
task1 = "Walk the dog"
task2 = "Feed the cats"
task_list.add(task1)
task_list.add(task2)
task_list.all_incomplete() == [task1, task2]
task_list.all_complete() == []
# this should be broken into two tests

'''When add multiple tasks, and mark one task as completed'''
task_list = TaskList()
task1 = "Walk the dog"
task2 = "Feed the cats"
task_list.add(task1)
task_list.add(task2)
task1.mark_complete()
task_list.all_incomplete() == [task2]
task_list.all_complete() == [task1]

#PhoneNumberExtractor

'''When add multiple diary entries PhoneNumberExtractor extracts
and returns a list of phone numbers from all diary entry contents'''
diary = Diary()
entry1 = DiaryEntry("My title 1", "My friend is 07800000000 and 07800000001")
entry2 = DiaryEntry("My title 2", "My content 2")
entry3 = DiaryEntry("My title 3", "My friend is 07800000002")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ['07800000000', '07800000001', '07800000002']

'''When add multiple diary entries PhoneNumberExtractor extracts
and returns a list of phone numbers and ignores invalid numbers'''
diary = Diary()
entry1 = DiaryEntry("My title 1", "My friend is 078000000000 and 078000223")
entry2 = DiaryEntry("My title 2", "My content 234556")
diary.add(entry1)
diary.add(entry2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

'''When add multiple diary entries PhoneNumberExtractor extracts
and returns a list of phone numbers from all diary entry contents
and ignores duplicates'''
diary = Diary()
entry1 = DiaryEntry("My title 1", "My friend is 07800000000 and 07800000001")
entry2 = DiaryEntry("My title 2", "My friend is 07800000001")
diary.add(entry1)
diary.add(entry2)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ['07800000000', '07800000001']

'''When add no diary entries PhoneNumberExtractor#extracts
and returns empty list'''
diary = Diary()
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

#ReadableEntryExtractor

'''When add multiple diary entries ReadableEntryExtractor extracts
and returns a the longest readable'''
diary = Diary()
entry1 = DiaryEntry("My title 1", "One two three four five")
entry2 = DiaryEntry("My title 2", "six seven eight")
entry3 = DiaryEntry("My title 3", "nine ten eleven")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
extractor = ReadableEntryExtractor(diary)
extractor.extract(2, 3) # => ['entry1']

'''When add multiple diary entries ReadableEntryExtractor#extracts
and returns readable -> not enough time to read any, returns an ematy list'''
diary = Diary()
entry1 = DiaryEntry("My title 1", "One two three four five")
entry2 = DiaryEntry("My title 2", "six seven eight")
entry3 = DiaryEntry("My title 3", "nine ten eleven")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
extractor = ReadableEntryExtractor(diary)
extractor.extract(1, 2) # => []

'''When add no diary entries ReadableEntryExtractor#extracts
and returns empty list'''
diary = Diary()
extractor = ReadableEntryExtractor(diary)
extractor.extract(1, 2) # => []

## 4. Create Examples as Unit Tests

# Diary:

'''Initially Diary has no entries'''
diary = Diary()
diary.all() # => []


# DiaryEntry:
entry = DiaryEntry("My title", "My content")
entry.title # => "My title"
entry.content # => "My content"

# TaskList

'''Initially TaskList has no incomplete tasks'''
task_list = TaskList()
task_list.all_incomplete() #=> []

'''Initially TaskList has no complete tasks'''
task_list = TaskList()
task_list.all_complete() #=> []


# Task
task = Task("Walk the dog")
task.title # => "Walk the dog"



## 5. Implement the Behaviour
'''