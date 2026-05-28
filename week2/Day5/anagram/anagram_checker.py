class Anagram:
    def __init__(self, word):
        self.words_list = []
    #  load word list
        with open('sowpods.txt', 'r') as f:
            for word in f:
                self.words_list.append(word.casefold().strip())
        

    def is_valid_word(self, word):
        # check if the word is real
        valid_word = word.strip()
        if valid_word in self.words_list:
            return True
        else:     
            print(f"{word} this is not a valid word")
            return False     

    def is_anagram(self, word1, word2):
        letters1 = []
        letters2 = []
        # check if words have same letters
        for char in word1:
            letters1.append(char)
        letters1.sort()
        for char in word2:
            letters2.append(char)
        letters2.sort()
        # print(letters1)
        # print(letters2)
        
        if letters1 == letters2:
            return True
        else:
            return False
        

    def get_anagrams(self, word):
        # creates a list of anagrams for the given word
        anagrams_list = []
        for word in self.words_list():
            if is_anagram(word, self.words_list()) == True:
                anagrams_list(self.words_list()).append
        return anagrams_list
            




             


