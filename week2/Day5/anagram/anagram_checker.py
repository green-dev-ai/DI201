class Anagram:
    def __init__(self):
        self.words_list = []
    #  load word list
        with open('sowpods.txt', 'r') as f:
            for word in f:
                self.words_list.append(word.casefold().strip())
        

    def is_valid_word(self, word):
        # check if the word is real
        valid_word = word
        if valid_word in self.words_list:
            return True
        else:     
            print(f"{word} this is not a valid word")
            return False     

    def is_anagram(self, word1, word2):
        return sorted(word1.casefold()) == sorted(word2.casefold())
        

    def get_anagrams(self, word):
        # creates a list of anagrams for the given word

        if not self.is_valid_word(word):
            return []
        anagrams_list = []
        for w in self.words_list:
                if w != word and self.is_anagram(word, w):
                    anagrams_list.append(w)
        return anagrams_list
                 


