#Random module used to randomise selection from list
import random

word_list = ["Bananas","Pineapple","Blueberries","Strawberries","Peaches"]

#chooses a random word using "choice" from the list passed in as arg
random_word = random.choice(word_list)


#Random letter input with conditional checks 
input_guess = input("Please enter a single letter: ")

#Checking if the guess is 1 long and is also in the alhpabet
if len(input_guess) == 1 and input_guess.isalpha():
    print("Good Guess!")

else:
    print("Oops! That is not a valid input.")