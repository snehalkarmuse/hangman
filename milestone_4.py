import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.word_guesses = ['_','_','_','_','_']
        self.num_letters = 0
        self.list_of_guesses = []

    def check_guess(self, guess): 
        count = 0
        print("word is - ", self.word)
        self.guess = guess
        self.guess = self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess {self.guess} is in the word. ")
            for i in self.word:
                if self.guess == i:
                    self.word_guesses[count] = self.guess 
                    print(self.word_guesses)
                    count = count + 1  
            self.num_lives = self.num_lives -1       
        else:
            print(f"Sorry {self.guess} is not in the word. Try again.")
    
    def ask_for_input(self):
        while True:
            self.guess = input("Enter a letter: ")
            if len(self.guess) == 1 and self.guess.isalpha():
                if self.guess in self.list_of_guesses:
                    print("You have already tried that letter.")
                else:
                    print("Good Guess.")
                    self.check_guess(self.guess)
                break
            else:
                print("Invalid input.")
    
hangman = Hangman(["mango","banana","apple","orange","grapes"], 5 )
hangman.ask_for_input()
