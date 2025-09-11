import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 10.")
    print("You have 3 chances to guess it correctly.")

    # Step 1: Generate random number
    secret_number = random.randint(1, 10)

    # Step 2: Give player 3 chances
    for attempt in range(1, 4):
        guess = int(input(f"\nAttempt {attempt}: Enter your guess (1-10): "))

        # Step 3: Game logic using conditionals
        if guess == secret_number:
            print("Congratulations! You guessed it right!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:  # runs if loop completes without 'break'
        print(f"\nGame Over! The correct number was {secret_number}.")

# Run the game
guessing_game()
