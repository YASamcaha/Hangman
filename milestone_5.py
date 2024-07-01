
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
        self.word = random.choice(word_list).lower()
        self.word_guessed = list(map(lambda letter:letter.replace(letter,"_"),[*self.word]))
        self.num_letters = int(len(set(self.word)))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This function is used to check if the guess is in the word and how many lives left

        Returns:
            str: Returns statement depending on if the guess was correct or not
            int: Number of lives remaining after the guess
     '''
        #Converting to lowercase
        guess.lower()
        #Check if guess is in random word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # for letter in self.word:
            #         if guess == letter:
            #             #Finding the index at which the guess is correct 
            #             # and using it to replace "_" with the guessed letter
            #                 # self.word_guessed[self.word.index(letter)] = letter
            #              
                        
            for index,letter in enumerate(self.word):
                if guess == letter:
                    for i, n in enumerate(self.word_guessed):
                        if i == index:
                           self.word_guessed[i] = guess

            self.num_letters -=1
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
        print(self.word_guessed)



    def ask_for_input(self):
        '''
        This function asks for user input and checks against a list of guesses 

        Returns:
            str: Returns statement depending on if the letter has been used previously
        '''
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.") 
                break
            #Checking if the guess is already in the list of guesses        
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                break
            #If the guess is not in the list of guesses its checked 
            # to see if it matches the word and is then added onto the list of guesses
            else:
                self.check_guess(guess) 
                self.list_of_guesses.append(guess) 
                break
                    



def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            return print("You lost!")
            
        elif game.num_lives != 0 and game.num_letters == 0:
            return print("Conragtulations, you won the game!") 
        else:
            if game.num_letters > 0:
                game.ask_for_input()


play_game(["apple","Pear","Mango","Grape"])
         
