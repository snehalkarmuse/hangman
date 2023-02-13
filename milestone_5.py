import random
class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_lives = num_lives
        self.num_letters = len(self.word)
        self.list_of_guesses = []
        self.word_guessed = []
        self.list_of_guesses = []

        for i in self.word:
            self.word_guessed.append("_")

        temp = set()
        temp_length = 0

        for i in self.word:
            temp.add(i)
            temp_length = len(temp)
        print("temp_length: ", temp_length)
        self.num_letters = temp_length
        print("num_letters ", self.num_letters)

    def check_guess(self, guess): 
        #print("word is - ", self.word)
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
            
         
        
    def ask_for_input(self):
        self.guess = input("Enter a letter: ")
        if len(self.guess) == 1 and self.guess.isalpha():
            if self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                print("Good Guess.")
                self.list_of_guesses.append(self.guess)
                self.check_guess(self.guess)
                print("After check guess self num letter ", self.num_letters)
                #break
        else:
            print("Invalid input.")
        
def play_game(word_list):
    num_lives = 5    
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters <= 0:
            print("Congratulations. You won the game!")
            break
        else:
            game.ask_for_input()

play_game(["banana"])