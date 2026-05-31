from anagram_checker import Anagram

def main():

# pass it to anagram 
    my_anagram = Anagram()
    
# find all of the anagrams
    
    while True:
        # get user input and validate
        user_word = input(f"provide a word to check its anagrams :").casefold().strip()
        anagrams = my_anagram.get_anagrams(user_word)
        
        if anagrams:
            print(f"these are the anagram words for {user_word} :")
            print(F"{anagrams}") 
        else:
            print(F"no anagram found for: {user_word}")
        cont = input(f"would you like to play again (Y/N) ?")
        if cont != "Y":
            break

       

main()
 

