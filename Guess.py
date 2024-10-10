import random

def number_guessing_game():
    # Randomly choose a number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    guess_count = 0

    print("Welcome to the Fun Number Guessing Game!")
    print("I've chosen a really fun integer between 1 and 100. Try to guess it!")
    print("Type 'quit' at any time to exit the game.")

    while True:
        guess = input("Enter your guess: ")

        # Allow the player to quit the game
        if guess.lower() == 'quit':
            print("Thanks for playing! Goodbye!")
            break

        try:
            guess = int(guess)
            guess_count += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Your guess is too low. Try again.")
            elif guess > secret_number:
                print("Your guess is too high. Try again.")
            else:
                print(f"Good job! You guessed the number {secret_number} in {guess_count} guesses.")
                print(f"Your score is {guess_count}.")
                print(f"Go again and to improve your score!")
                break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100 or 'quit' to exit.")

if __name__ == "__main__":
    number_guessing_game()
