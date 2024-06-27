#Importing previous milestones functions and variables
from milestone_2 import random_word, word_list, input_guess, input_guess_check, random_word


guess = input_guess
random_word
valid_check = input_guess_check()  


#Creating class for hangman game
class Hangman:
    def __init__(self,word_list,num_lives = 5):
        self.word_list = word_list
        #Setting default number of lives as 5
        self.num_lives = num_lives
    #Random word selected from list as defined in milestone 2
    word = random_word
    word_guessed = list(map(lambda letter:letter.replace(letter,"_"),[*word]))
    num_letters = int(len(set(word)))
    list_of_guesses = []

    def check_guess(self, guess):
        #Converting to lowercase
        guess.lower()
        #Check if guess is in random word
        if guess in Hangman.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                    if guess == letter:
                        #Finding the index at which the guess is correct and using it to replace "_" with the guessed letter
                        Hangman.word_guessed[Hangman.word.index(letter)] = letter
            self.num_letters -=1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")



    def ask_for_input(self):
        while True:
            #Using Check from milestone 2 if false the guess is invalid
            if valid_check is False:
                print("Invalid letter. Please, enter a single alphabetical character.") 
                break
            #Checking if the guess is already in the list of guesses        
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            #If the guess is not in the list of guesses its checked 
            # to see if it matches the word and is then added onto the of guesses
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess) 
                break
                    




Game_test = Hangman(["Bananas","Pineapple","Blueberries","Strawberries","Peaches"])

Game_test.ask_for_input()

