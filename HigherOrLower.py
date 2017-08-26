print("Welcome to the Higher or Lower guessing game, by Caleb Sim from Sim Inc.")
print("========================================================================")
import random
number = random.randint(0, 10)
guess = input("I have got my number, now try and guess a number out of 0-10 (or q to exit): ")
while guess != 'q':
    if guess > number:
        print("It is lower than ", guess)
        guess = input("Guess again: ")
    elif guess < number:
        print("It is higher than ", guess)
        guess = input("Guess again: ")
    elif guess == number:
        print("You guessed right!")
        guess = input("Press [ENTER] to continue or 'q' to exit")
    elif guess == "":
        number = random.randint(0, 10)
        guess = input("I have got my number, now try and guess a number out of 0-", limit, " (or q to exit): ")
