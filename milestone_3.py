#Milestone covers if the guessed character is in the word

#Importing code from milestone_2 as "m2"
import milestone_2 as m2

guess = m2.input_guess
valid_check = m2.input_guess_check() 
random_word = m2.random_word 


def check_guess(guess):
    #Converting to lowercase
    guess.lower()
    #Check if guess is in random word
    if guess in random_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
#Iterative check if guess is valid
    while True:
        if valid_check is True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") 
            break
    check_guess(guess)
        


ask_for_input()