import re

class PhoneNumberExtractor():

    def __init__(self, diary):
        self.diary = diary

    def extract(self):
        phone_numbers = []
        for entry in self.diary.all():
            if entry.content not in phone_numbers:
                phone_numbers += re.findall(r"\b0[0-9]{10}\b", entry.content)
        unique_numbers = []
        for num in phone_numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)
        return unique_numbers

        # using set() - set is like a list but cannot have duplicates
        phone_numbers = set() 
        for entry in self.diary.all():
                found_numbers = re.findall(r"\b0[0-9]{10}\b", entry.content)
                phone_numbers.update(found_numbers) #like append but for set
        return phone_numbers # have to change tests to {'07800000000', '07800000001', '07800000002'}

        # phone_numbers = []
        # list_of_content = []
        # for entry in self.diary.all():
        #     list_of_content.extend(entry.content.split())
        # for word in list_of_content:
        #     if len(word) == 11 and word[0] == 0:
        #         phone_numbers.append(word)
        # return phone_numbers


