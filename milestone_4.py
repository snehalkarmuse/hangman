import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.word_guessed = []
        self.list_of_guesses = []
        for i in self.word:
            self.word_guessed.append("_")
        # temp = set(self.word)
        #self.num_length = len(temp)
        temp = set()
        temp_length = 0
        for i in self.word:
            temp.add(i)
            temp_length = len(temp)
        self.num_letters = temp_length
                

    def check_guess(self, guess): 

        self.guess = guess
        self.guess = self.guess.lower()
       
        if self.guess in self.word:
            print(f"Good guess! {self.guess} is in the word.")
            idx = 0
            for i in self.word:
                if self.guess == i:
                    self.word_guessed[idx] = self.guess 
                    print(self.word_guessed)
                idx = idx + 1 
            self.num_letters = self.num_letters - 1  
        else:
            self.num_lives = self.num_lives -1  
            print(f"Sorry, {self.guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print(self.word_guessed)

        self.list_of_guesses.append(self.guess)
       
    
    def ask_for_input(self):
        
        while (self.num_lives > 0) and (self.num_letters > 0) :
            self.guess = input("Enter a letter: ")
            if len(self.guess) != 1:
                    print("Invalid letter. Please, enter a single characher.")
            elif self.guess in self.list_of_guesses:
                    print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                print("after check guess self num ", self.num_letters)
                break
            #print("list of guesses ", self.list_of_guesses)
    
hangman = Hangman(["banana"], 5 )
hangman.ask_for_input()
