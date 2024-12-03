from art import logo
import random
import os

def set_level():
    """level of difficulty in game"""
    print("choose your difficulty level: 1.Easy or 2.Hard")
    level=int(input("1 or 2: "))
    while level not in [1,2]:
        level=int(input("INVALID.'1' or '2' only: "))

    if level==1:
        return 10
    else:
        return 5

def checkansw(guess,answer,turn):
    if guess>answer:
        print("too high")
        return turn-1
    
    elif guess<answer:
        print("too low")
        return turn-1
    else:
        print(f"your guess {guess} and it correct.therefore, ")
def game_on():
    print(logo)
    print("welcome to number guessing game")
    game_over=False
    answer=random.randint(1,100)
    turn=set_level()
   
    while not game_over:
        guess=int(input("guess number between 0 to 100: "))
        turn=checkansw(guess,answer,turn)
        if turn==0 and guess!=answer:
            print(f"Game over.the correct answer is {answer}")
            game_over=True
        elif turn!=0 and guess!=answer:
            print(f"you have {turn} remaining")
            #hint
            if abs(guess-answer)<=2:
                print("close enough dont give up")
            # os.system('cls')
        else:
            print("you win the game")
            game_over=True
while input("do you want to play number guessing: 'y' or 'n' ")=='y':      
    game_on()
