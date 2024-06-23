#Random module used to randomise selection from list
import random

word_list = ["Bananas","Pineapple","Blueberries","Strawberries","Peaches"]

#chooses a random word using "choice" from the list passed in as arg
random_word = random.choice(word_list)
input_guess = input("Please enter a single letter: ")




#Defining function to check the guess meets parameters
def input_guess_check():
#checks if the guess is 1 long and is also in the alphabet
    if len(input_guess) == 1 and input_guess.isalpha():
        return True
        print("Good Guess!")