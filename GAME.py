import random

# List of predefined words
word_list = ['apple', 'robot', 'candy', 'pizza', 'tiger']

# Randomly choose a word
secret_word = random.choice(word_list)
guessed_letters = []
tries = 6

# Create a display version of the word
display_word = ['_' for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 chances to guess wrong.\n")

# Game loop
while tries > 0 and '_' in display_word:
    print("Word:", ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.\n")

# Game result
if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game over! The word was:", secret_word)
