class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            if sorted(candidate) == self.sorted_word:
                matches.append(candidate)
        return matches            

listen = Anagram("Listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])