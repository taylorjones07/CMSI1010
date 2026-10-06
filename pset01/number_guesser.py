import random


number = random.randint(1, 1000)
attempts = 0

# Guesses
while True:
    guess = input("Guess a number between 1 and 1000, or type 'bye' or 'exit' to quit: ")

    if guess == "bye" or guess == "exit":
        break

    if not guess.isdigit():
        print("Please enter a valid number")
    else:
        guess = int(guess)
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number!")
            print("Number of attempts:", attempts)

            # How to Reset the game
            number = random.randint(1, 1000)
            attempts = 0