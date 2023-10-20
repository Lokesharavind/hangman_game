import random
import hangman_stages
import hangman_words

word_list =["apple","beautiful","potato"]
lives= 6
chosen_word = random.choice(hangman_words.words)
print(chosen_word)
display = []
for i in range(len(chosen_word)):#0 1 2 3 4 5 #apple
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a Letter: ").lower()
    for position in range(len(chosen_word)):#apple
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
        if lives==0:
            game_over = True
            print("You Lose.")
    if '_' not in display:
        game_over = True
        print("You Win")
    print(hangman_stages.stages[lives])