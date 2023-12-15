# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, candidates):
        return [candidate for candidate in candidates if self.is_anagram(candidate)]
    
    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return sorted(candidate_lower) == sorted(self.word) and candidate_lower != self.word

anagram = Anagram("word")