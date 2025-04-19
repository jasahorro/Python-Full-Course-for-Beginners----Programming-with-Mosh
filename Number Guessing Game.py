""" Develop a game where the program randomly selects a number, and the user has 
to guess it. Provide feedback if the guess is too high or too low. This project helps 
you understand loops and conditional statements. """

import random 

user_guess =  input("guess a number between 1 and 10: ")
user_guess = int(user_guess)

random_number = random.randint(1,10)
if user_guess == random_number:
    print("you guessed it right!")
else:
    print("you guessed it wrong!")
    if user_guess < random_number:
        print("your guess is too low")
    elif user_guess > random_number:
        print("your guess is too high")
    else:
        print(f"the random number is {random_number}")
