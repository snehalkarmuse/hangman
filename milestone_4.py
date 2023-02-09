import random

class Hangman:
    def __init__(self, word_list, num_lives) -> None:
        self.word = word_list
        self.num_lives = 5
        self.word_guesses = []
        self.num_letters = 0
        self.word_list = word_list
        self.list_of_guesses = []

