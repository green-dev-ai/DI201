from anagram_checker import Anagram

def main():
# get user input and validate
    user_word = input(f"provide a word to check its anagrams :")
    user_word = user_word.casefold().strip()

# pass it to anagram 
    my_anagram = Anagram(user_word)
    
# find all of the anagrams
    if my_anagram.is_valid_word(user_word) == True:
        anagram_list = []
        for word in my_anagram.words_list:
            if my_anagram.is_anagram(word, user_word) == True:
               if user_word != word:
                    anagram_list.append(word)
                    
        print(f"these are the anagram words for {user_word} : {anagram_list}")  
    else:    
        print(F"there is no anagram for this word")
    
           
    
    cont = input(f"would you like to play again (Y/N) ?")
    print(f"{cont}")
    if cont == "Y":
        return True
    else:
        return False
        
       




flag = True
while flag == True:
    flag = main()

    
