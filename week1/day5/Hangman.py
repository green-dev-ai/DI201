# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

    ### YOUR CODE STARTS FROM HERE ###

def get_guess(remaining_guesses):
    """ this function asks the player for a new letter and returns the letter."""
    letter = input(f"You have {remaining_guesses} guesses remaining. Guess a letter: ")
    return letter

def check_letter(letter):
    """ this function checks if the letter is a valid new entry and returns true or false """
    if letter in guesses_list:
        print(f"you've already guessed that letter. try again. ")
        return False
    else:
        guesses_list.append(letter)
        return True
    
def check_word(letter):
    """this function check if a letter that was guessed is in the random word returns true or false"""
    if letter in word:
        return True
    else:
        return False


def update_display_word(letter):
    """this function updates the display word with the selected letter"""
    for position, char in enumerate(word):
        if char == letter:
            display_word[position] = letter


def check_win():
    """this function checks to see if the player guesses the word"""
    if "_" in display_word:
        return False
    else:
        return True 

display_word = [""] * len(word)
guesses_list = [""]

i = int(0)
for i in range(len(word)):
    display_word[i] = "_"


remaining_guesses = 6

while remaining_guesses != 0:
    letter = get_guess(remaining_guesses)
    check_letter(letter)
    if check_word(letter) is True:
        update_display_word(letter)
        print(f"{display_word}")
        if check_win() is True:
            print(f" You Won !!! Well done !!!")
            break
    else:
        remaining_guesses -= 1
        print(f"you guessed wrong ! the letter {letter} in not in the random word")
 

if remaining_guesses == 0:
    print(f"You Lose !!!. The word was {word}")

