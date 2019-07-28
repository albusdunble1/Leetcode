import random

user_input = None

while user_input != "n":
    guess = None
    num = random.randint(1,10)
    
    while guess != num:
        guess = int(input("Guess a number from 1-10: "))
        while guess not in range(1,11):
            guess = int(input("Guess a number from 1-10 only, try again: "))

        if guess == num:
            print("You guessed it!")
        elif guess > num:
            print("Too high")
        else:
            print("Too low")

    user_input = input("Do you still want to play? (y/n): ")
