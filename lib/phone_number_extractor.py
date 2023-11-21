import re

class PhoneNumberExtractor():

    def __init__(self, diary):
        self.diary = diary

    def extract(self):
        phone_numbers = []
        for entry in self.diary.all():
            if entry.content not in phone_numbers:
                phone_numbers += re.findall(r"0[0-9]{10}", entry.content)
        unique_numbers = []
        for num in phone_numbers:
            if num not in unique_numbers:
                unique_numbers.append(num)
        return unique_numbers

        # phone_numbers = []
        # list_of_content = []
        # for entry in self.diary.all():
        #     list_of_content.extend(entry.content.split())
        # print("List of content:", list_of_content)
        # for word in list_of_content:
        #     if len(word) == 11 and word[0] == 0:
        #         phone_numbers.append(word)
        # print("Phone numbers:", phone_numbers) 
        # return phone_numbers


