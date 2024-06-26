# <table><tr><td>Hangman Game</td></tr></table>

## ${\textsf{\color{lightblue}What does it do?}}$
This hangman game uses the functionality of the random module in python to select a random word from a predefined list of words.
The end goal is for the user to correctly guess the word by guessing the letters before they run out of lives.

## ${\textsf{\color{lightyellow}What have I learnt?}}$
1. How to create a class to define the specific elements of the game
2. How to incorporate principles of OOP to ensure my code is more readable and accesible to others
3. How to manage a project that utilises more than one file by using importing to not duplicate work
4. Version control through Git/Github and how best to manage the different iterations of the project
5. Using decorators to add increased functionaltiy to exisiting functions

 ##  ${\textsf{\color{lightgreen}Usage Instructions}}$
1. Run the file "milestone_4.py"
2. When creating an instance of the game use the Hangman class Hangman([list of words]) 
    1. Ensure the words are all valid and do not contain any non alphabetical elements
         
3. To play ensure you make a valid guess (a single alphabetical input), otherwise it will cause an error!
4. You have a limited number of lives and every guess will reduce your total lives
5. Finally the game has a built in timer so you can see how well you performed versus your previous games


##  ${\textsf{\color{purple}File Structure}}$
Currently the project is set up so that the game is broken up into manageable blocks or milestones.
Previous iterations of the game can be found in the other "mileston" files
The main game is run from the "mileston_4.py" file

##  ${\textsf{\color{red}Licence Information}}$
This project a uses GNU GENERAL PUBLIC LICENSE
