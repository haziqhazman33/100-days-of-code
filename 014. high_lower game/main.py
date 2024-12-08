from art import logo,vs
import random
from game_data import data
# print(logo)

def choosen_account():
    return random.choice(data)

def format(account):
    name=account['name']
    role=account['description']
    place=account['country']

    return f"{name}, {role}, from {place}"

def compare(guess,acc_a,acc_b):
    if acc_a>acc_b:
        return guess=='a'
    else:
        return guess=='b'
    
    #example ('a',120,140) 120<140 if guess is 'a' and 'a'=='b' return False
    # in main False == True =>

def main():
    print(logo)
    account_a=choosen_account()
    account_b=choosen_account()
    game_over=False
    score=0
    while not game_over:
        account_a=account_b
        account_b=choosen_account()
        print(f"Compare A: {format(account_a)}")
        print(f' {vs}')
        print(f'Compare B: {format(account_b)}')

        player_guess=input("Who has more followers? Type 'A' or 'B': ").lower()

        return_bool=compare(player_guess,account_a['follower_count'],account_b['follower_count'])
        if return_bool == True:
            score+=1
            print(f"you're right! Current score: {score}")
        else:     
            game_over=True
            print(f"sorry, That's wrong. Final score: {score}")
        
        
main()
