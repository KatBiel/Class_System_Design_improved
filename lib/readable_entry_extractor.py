class ReadableEntryExtractor():

    def __init__(self, diary):
        self.diary = diary
    
    def extract(self, wpm, time):
        readable_entries = [
            entry for entry in self.diary.all()
            if self._entry_readable_in_time(wpm, time, entry)
        ]
        if len(readable_entries) == 0:
                return None
        else:
            return max(readable_entries,
                        key = lambda entry: self.count_words(entry.content))

    def _entry_readable_in_time(self, wpm, time, entry):
        length_of_readble_chunk = wpm * time
        return self.count_words(entry.content) <= length_of_readble_chunk

    def count_words(self, string):
        return len(string.split(" "))
