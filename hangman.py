import random

def hangman():
    words = ["python", "hangman", "coding", "computer", "program"]
    chosen_word = random.choice(words)
    guessed_letters = []
    correct_letters = ["_"] * len(chosen_word)
    attempts = 6  

    print(" Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses allowed.\n")
    while attempts > 0 and "_" in correct_letters:
        print("Word: ", " ".join(correct_letters))
        print(f"Incorrect guesses left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}" if guessed_letters else "")

        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single alphabet letter.\n")
            continue
        if guess in guessed_letters:
            print(" You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        # Step 4: Check guess
        if guess in chosen_word:
            print(" Correct!\n")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    correct_letters[i] = guess
        else:
            print(" Incorrect!\n")
            attempts -= 1
    if "_" not in correct_letters:
        print(f" Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f" Out of guesses! The word was: {chosen_word}")
if __name__ == "__main__":
    hangman()
import random

def hangman():
    words = ["python", "hangman", "coding", "computer", "program"]
    chosen_word = random.choice(words)
    guessed_letters = []
    correct_letters = ["_"] * len(chosen_word)
    attempts = 6  

    print(" Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print("You have 6 incorrect guesses allowed.\n")
    while attempts > 0 and "_" in correct_letters:
        print("Word: ", " ".join(correct_letters))
        print(f"Incorrect guesses left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}" if guessed_letters else "")

        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single alphabet letter.\n")
            continue
        if guess in guessed_letters:
            print(" You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)
        if guess in chosen_word:
            print(" Correct!\n")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    correct_letters[i] = guess
        else:
            print(" Incorrect!\n")
            attempts -= 1
    if "_" not in correct_letters:
        print(f" Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f" Out of guesses! The word was: {chosen_word}")
if __name__ == "__main__":
    hangman()
