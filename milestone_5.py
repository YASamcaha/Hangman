#Importing random module, used to choose a random word from game list
import random


#Creating class for hangman game
class Hangman:
    '''
    This class is used to create an instance of the Hangman game.

    Attributes:
        word_list (list): List of words to be used in the game
        num_lives (int): Number of lives the user has 
    '''

    def __init__(self,word_list,num_lives = 5):
        '''
      See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        #Setting default number of lives as 5
        self.num_lives = num_lives
        #Random word selected from list as defined in milestone 2
        self.word_list = ["Apple","Pear","Cherry"]
        #Converts the word selected to all lowercase
        self.word = random.choice(word_list).lower()
        #Converts the random word to a list of "_" using lambda function
        self.word_guessed = list(map(lambda letter:letter.replace(letter,"_"),[*self.word]))
        #Ensures only the unique letters are considered by converting to a set
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This function is used to check if the guess is in the word and how many lives left

        The purpose of this function is to ensure the guess is all lowercase,
        and to check the guess is within the randomly selected word. If that is the case, it will match the letter
        to the list of "_" and replace each instance to give the end user a visual representation of their guess.
        Each guess also results in a life being lost until the end user wins or loses.

        Attributes:
        guess(str): Takes in the user input

        Returns:
            str: Returns statement depending on if the guess was correct or not
            int: Number of lives remaining after the guess
     '''
        #Converting to lowercase
        guess.lower()
        #Check if guess is in random word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")         
            #Iterates through the word to find the matching guess and index.
            # Index is then matched to the word_guesses to replace all instances of the letter.            
            for index,letter in enumerate(self.word):
                if guess == letter:
                    for i, n in enumerate(self.word_guessed):
                        if i == index:
                           self.word_guessed[i] = guess
            #Removing a life once the user has guessed
            self.num_letters -=1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        print(self.word_guessed)



    def ask_for_input(self):
        '''
        This function asks for user input and checks against a list of guesses 

        This function is the method of asking for user input. 
        It checks to ensure the input is valid, testing against its length and whether it's alphanumerical.
        Once checked it returns a statement to inform the user if the guess is valid or if the guess has already been used before.
        If it has not been used before it is added to the list of guesses to be used in the next round of the game.

        Returns:
            str: Returns statement depending on if the letter has been used previously
        '''
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetic character.") 
                break
            #Checking if the guess is already in the list of guesses        
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            #If the guess is not in the list of guesses it's checked 
            # to see if it matches the word and is then added onto the list of guesses
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess) 
                break
                    



#Timer decorator to time the duration of the game
import time
def game_timer(play_game):
    def wrapper(word_list):
        time_start_game = time.time()
        play_game(word_list)
        time_end_game = time.time()
        print(f'You played for {round(time_end_game - time_start_game,2)} seconds')
    return wrapper



@game_timer
def play_game(word_list):
    '''
        This function is used to run the game and asks for a list input 

        The main purpose of this function is to continuously run the game until the user loses or wins.
        Conditions are set depending on the amount of lives left.

        Returns:
            str: Returns statement depending on if you have won or lost the game
     '''
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            return print("You lost!")
            
        elif game.num_lives != 0 and game.num_letters == 0:
            return print("Congratulations, you won the game!") 
        else:
            if game.num_letters > 0:
                game.ask_for_input()
