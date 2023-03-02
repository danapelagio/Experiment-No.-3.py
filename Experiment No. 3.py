import random

# generate a random number between 1 and 100
number = random.randint(1, 100)
# give the user 10 chances to guess the number
for i in range(10):
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations, you guessed it!")
        print("Number of guesses:", i+1)
        break
# if the user didn't guess the number, reveal it
if guess != number:
    print("Sorry, you ran out of guesses. The number was", number)
