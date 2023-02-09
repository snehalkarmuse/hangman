# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 



## Milestone 2
- In this created and initilized variables and used random module. Computer will choose random word from the list.
- milestone_2.py accepts input from user and checks wheather it is alphabet and single letter.
- If it is not then it prints a friendly message.

## Milestone 3
- In this miolestone, creates two function called ask_in_input and check_guess.
- ask_in_put() takes the input and validate for alphabate and only one charachter has been entered.
  Calls check_guess() with the parameter which gets from the user.
- check_guess() with user input parameter, convert taht into lower case first. check it is in the word which computer selected   from the world_list.
it prints the message wheather it is in the word or not.

## Milestone 4
- create a class with name Hangman.
- Declares attributes and methods.
- Initilized with init method. 
- In ask_for_input() method adding the guesses in word_guess attirbute replaces it with guess. Decrements num_lives.
- check_guess() check each guess in word. If matches increments word_guess and decrement num_lives.