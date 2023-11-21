class ReadableEntryExtractor():

    def __init__(self, diary):
        self.diary = diary
    
    def extract(self, wpm, time):
        length_of_readble_chunk = wpm * time
        readable_chunk = []
        for entry in self.diary.all():
            if len(entry.content) <= length_of_readble_chunk:
                readable_chunk.append(entry.content)
        return readable_chunk