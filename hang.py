import random
import unicodedata

def normalize(word):
    """Remove accents from a word for comparison purposes."""
    return ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')

def display_word(word, guessed_letters):
    """Display the word with underscores for unguessed letters."""
    return ' '.join(letter if normalize(letter) in guessed_letters else '_' for letter in word)

def hangman_game():
    terms = [
        "Être", "Avoir", "Aller", "Parler", "Manger", "Boire", "Dormir", "Vouloir", 
        "Pouvoir", "Chercher", "Prendre", "Comprendre", "Demander", "Aimer", 
        "Réserver", "Payer", "Visiter", "Acheter", "Regarder", "Attendre"
    ]

    word = random.choice(terms)
    normalized_word = normalize(word).upper()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman! Guess the French verb.")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter: ").strip().upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in normalized_word:
            print("Good guess!")
            if all(normalize(letter).upper() in guessed_letters for letter in word):
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            print("Wrong guess.")
            attempts -= 1

    else:
        print("\nGame over. The word was:", word)

if __name__ == "__main__":
    hangman_game()
