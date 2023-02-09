import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word = word_list
        self.num_lives = num_lives
        self.word_guesses = []
        self.num_letters = 0
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess): 
        self.guess = guess
        self.guess = self.guess.lower()
        if self.guess in self.word:
            print(f"Good guess {self.guess} is in the word. ")
        else:
            print(f"Sorry {self.guess} is not in the word. Try again.")
    
    def ask_for_input(self):
        while True:
            self.guess = input("Enter a letter: ")
            if len(self.guess) == 1 and self.guess.isalpha():
                print("Good Guess.")
                break
            elif self.guess in self.list_of_guesses:
                print("You have already tried that letter.")
            else:
                self.check_guess(self.guess)
    
hangman = Hangman(["mango","banana","apple","orange","grapes"], 5 )
hangman.ask_for_input()
