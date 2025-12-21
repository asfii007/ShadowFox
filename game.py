import random

words = ["apple", "banana", "grape", "orange","Tree","moango","city","music","india","python"]
word = random.choice(words)

guessed = []
tries = 6

print(" Hangman Game")

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that.")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("❌ Wrong! Tries left:", tries)
    else:
        print("✅ Correct!")

if tries == 0:
    print(" You lost! The word was:", word)
