import random

class HangmanGame:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(words).upper()
        self.word_letters = set(self.word)
        self.alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.used_letters = set()
        self.lives = 6

    def play(self):
        while len(self.word_letters) > 0 and self.lives > 0:
            print('\nYou have', self.lives, 'lives left.')
            
            # Show used letters
            print('Used letters:', ' '.join(sorted(self.used_letters)))

            # Show current word state
            word_list = [letter if letter in self.used_letters else '_' for letter in self.word]
            print('Current word:', ' '.join(word_list))

            # Get player guess
            user_letter = input('Guess a letter: ').upper()
            
            if user_letter in self.alphabet - self.used_letters:
                self.used_letters.add(user_letter)
                
                if user_letter in self.word_letters:
                    self.word_letters.remove(user_letter)
                else:
                    self.lives -= 1
                    print('Letter is not in the word.')
            
            elif user_letter in self.used_letters:
                print('You have already guessed that letter. Try again.')
            
            else:
                print('Invalid character. Please enter a letter.')

        # Game end conditions
        if self.lives == 0:
            print(f'Sorry, you died. The word was {self.word}.')
        else:
            print(f'Congratulations! You guessed the word {self.word}!')

def main():
    french_verbs = ["Être", "Avoir", "Aller", "Parler", "Manger", 
                    "Boire", "Dormir", "Vouloir", "Pouvoir", "Chercher", 
                    "Prendre", "Comprendre", "Demander", "Aimer", 
                    "Réserver", "Payer", "Visiter", "Acheter", 
                    "Regarder", "Attendre"]
    
    while True:
        game = HangmanGame(french_verbs)
        game.play()
        
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            break

    print('Thanks for playing!')

if __name__ == "__main__":
    main()