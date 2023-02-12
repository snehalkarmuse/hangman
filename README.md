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
- Initilized with init method. created for loop in init method to change the word_guessed list to "_" . num_letters is a number with unique letters set. crteated teh for loop to get through each word and count the length of it. created the set with unique letters. 
- In ask_for_input() method adding the guesses in word_guess attirbute replaces it with guess. Decrements num_lives. printes the output accordingly to understand the user.
- check_guess() check each guess in word. If matches increments word_guess and replace the word_guessed with letters from underscore. Otherwise decrement num_lives and make the changes in word_guessed. 
## Milestone 5
- created function call PlayGame(), which took word list as an argument. Initialzed variable called num_lives to 5. created the instance of the class called game. passed teh argument word list and num lives. Checked the input, if num_lives is equal to 5 then prints "you lost!" else call check_guess(). If you have still num_lives left and num_letters are not zero then prints "you won". 
 - Call the function called PlayGame(), with word list as an argument.
 - check the length of the unique letters left to fill in the word displayed with num_letters left. For this creat a set which will take unique letters and put that in num_letters. Write all this in initialize method in class. update according in check_guess function.