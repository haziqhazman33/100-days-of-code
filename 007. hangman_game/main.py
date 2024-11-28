from random import choice
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
from replit import clear
end_game=False
print(logo)
chosen_word=choice(word_list)
print(chosen_word)
lives=6
word_length=len(chosen_word)
print(word_length)
display=["_"]*word_length #list
print(stages[6])
def game_state():
    print(f"word_in_guessed:{' '.join(display)}")
    print(f"attempts left: {lives}")
    print(stages[lives])

while not end_game:
    guess= input("GUess a letter: ").lower()

    if len(guess)!=1:
        print("try again only one letter")

    if guess in display:
        print(f"you've already guessed the letter {guess}")
    for position in range(word_length):
        letter=chosen_word[position]
        if guess==letter:
            display[position]=letter
    game_state()
    if guess not in chosen_word:
        lives-=1
        print(f"you guessed {guess}, that's not in word therefore you lose a life")
        
        if lives == 0:
            end_game = True
            print("You lose.")
            print(f"the correct guess is: {chosen_word}")
        game_state()
        
    if "_" not in display:
        end_game = True
        print("You win.")
