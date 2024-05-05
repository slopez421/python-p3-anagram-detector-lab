

class Anagram: 
    def __init__(self, word):
       self.word = word

    def match(self, lists):
        list = []
        for words in lists:
            if sorted([letter for letter in self.word]) == sorted([letter for letter in words]):
                list.append(words)

        return list
        