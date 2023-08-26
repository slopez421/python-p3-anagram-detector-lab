

class Anagram: 
    def __init__(self, word):
        self.word = word

    def match(self, list):
        matches = []

        for words in list:
            if sorted(self.word) == sorted(words):
                matches.append(words)
            
        return matches