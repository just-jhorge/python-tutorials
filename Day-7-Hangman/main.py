import random
import hangman_art
import hangman_words

print(hangman_art.logo)

random_word = random.choice(hangman_words.word_list)
display = []
lives = 6

# Fill the display list with underscores representing each letter in the random word picked
for _ in range(len(random_word)):
    display += '_'

end_of_game = False

while not end_of_game:
    guessed_letter = input('Please guess a letter: ').lower()

    for position in range(len(random_word)):
        letter = random_word[position]

        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in random_word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose 👎🏾")
            print(f"The word is: {random_word}")

    print(f"You have {lives} lives remaining")
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('You win 🏆🎊🥳')
