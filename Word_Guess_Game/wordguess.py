import random

# List of words
words = ["oracle","amaxon","microsoft","cat","dog","almond","cashewnuts","dragon fruit","apple", "banana", "orange", "grape", "kiwi", "mango", "pear", "peach", "plum", "strawberry"]

#choose random word from the list
guessed_word = random.choice(words)
print(guessed_word)


hint = guessed_word[0] + guessed_word[-1]
print(hint)

store_g_l = []
try_p = 6

player_name = input("Enter your name: ")
print("Welcome to the Game World, ", player_name)
print('We are going to give you 6 attempts for guessing.')

for guess in range(try_p):
    while True:
        letter = input('Guess the letter: ')
        
        if len(letter) == 1:
            break
        else:
            print("Oops! Please guess a single letter.")

    if letter in guessed_word:
        print('Yes')
        store_g_l.append(letter)
    else:
        print("No")

    if guess == 3:
        clue_request = input("Would you like a clue? (yes/no): ")
        if clue_request.lower().startswith("y"):
            print("Clue: The first and last letter of the word is", hint)
        else:
            print("You are very confident.")

    print("Now let's see what you have guessed so far.")
    print("You have guessed:", len(store_g_l), 'letter(s) correctly.')
    print("These letters are:", store_g_l)

word_guess = input("Guess the whole word: ").lower()
if word_guess == guessed_word:
    print("Congrats! You are correct.")
else:
    print("Sorry! The answer was:", guessed_word)

print("\nPlease press Enter to exit the process.")
input()
