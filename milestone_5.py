import random
class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.word_guesses = []
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        for i in self.word:
            self.word_guesses.append("_")

    def check_guess(self, guess): 
        #print("word is - ", self.word)
        self.guess = guess
        self.guess = self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess {self.guess} is in the word. ")
            idx = 0
            for i in self.word:
                if self.guess == i:
                    self.word_guesses[idx] = self.guess 
                    print(self.word_guesses)
                    self.num_letters = self.num_letters - 1  
                idx = idx + 1              
        else:
            self.num_lives = self.num_lives -1  
            print(f"Sorry {self.guess} is not in the word. Try again.")
            print(f"you have {self.num_lives} lives left.")
            print(self.word_guesses)
            
         
        
        
        
    
    def ask_for_input(self):
        self.guess = input("Enter a letter: ")
        if len(self.guess) == 1 and self.guess.isalpha():
            if self.guess in self.list_of_guesses:
                print("You have already tried that letter.")
            else:
                print("Good Guess.")
                self.list_of_guesses.append(self.guess)
                self.check_guess(self.guess)
                #break
        else:
            print("Invalid input.")
        
def playGame(word_list):
    num_lives = 5    
    game = Hangman(word_list, num_lives )
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters <= 0:
            print("You won! Congragulation.")
            break
        else:
            game.ask_for_input()

playGame(["mango","orange","apple","peach","grape"])