
import random

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def load_dictionary(file_path, min_len=4, max_len=12):
    try:
        with open(file_path, 'r') as f:
            words = [line.strip().lower() for line in f
                     if line.strip().isalpha() and min_len <= len(line.strip()) <= max_len]
        if not words:
            print(f"No words found between {min_len} and {max_len} letters.")
        return words
    except FileNotFoundError:
        print("❌ Dictionary file not found!")
        return []

def get_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game(dictionary_path='C://Users//dosur//OneDrive//Desktop//PYTHON//codealpha_tasks//Hangman_game//words.txt'):
    word_list = load_dictionary(dictionary_path, min_len=4, max_len=12)

    if not word_list:
        return

    word = get_random_word(word_list)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("\nWord:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("❗ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess.")
            wrong_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You guessed the word:", word)
            break
    else:
        print(HANGMAN_PICS[-1])
        print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman_game()
