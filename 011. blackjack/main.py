import random
from art import logo
# Create a deck of cards
def create_deck():

    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # Values only

# Calculate the total value of a hand
def calculate_hand(hand):
    total = sum(hand)
    aces = hand.count(11)
    if total==21 and len(hand)==2:
        return 0
    while total > 21 and aces:
        total -= 10  # Convert Ace from 11 to 1
        aces -= 1
    return total

# Function to deal a card
def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def compare(user_score,comp_score):
  if user_score > 21 and comp_score > 21:
    return "You went over. You lose 😤"
  if user_score == comp_score:
    return "Draw 🙃"
  elif comp_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif comp_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > comp_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def blackjack():
    game_over=False
    print(logo)
    deck = create_deck()
    player_hand=[]
    dealer_hand=[]
    # Initial hands
    for _ in range(2):
        player_hand.append(random.choice(deck))
        dealer_hand.append(random.choice(deck))
    player_score=calculate_hand(player_hand)
    dealer_score=calculate_hand(dealer_hand)
    print(f"Player card: {player_hand},score: {player_score}")
    print(f"Computer card:{dealer_hand},score:{dealer_score}")
    # Player's turn
    while not game_over:
        if  player_score==0 or dealer_score==0:
            if player_score==0:
                print(" Yo Blackjack. you win")
                game_over=True
            elif dealer_score==0:
                print("you lose. Comp win with blackjack")
                game_over=True
        else:
            action = input("Do you want to [H]it or [S]tand? ").lower()
            while calculate_hand(dealer_hand)<17:
                dealer_hand.append(random.choice(deck))
            if action == 'h':
                player_hand.append(random.choice(deck))
                print(f"Player card: {player_hand},score: {calculate_hand(player_hand)}")
                print(f"Dealer card: {dealer_hand},score: {calculate_hand(dealer_hand)}")
                if calculate_hand(player_hand)>21 or calculate_hand(dealer_hand)>21:
                   game_over=True
            elif action =='s':
                print(f"Player card: {player_hand},score: {calculate_hand(player_hand)}")
                # print(f"Dealer card: {dealer_hand},score: {calculate_hand(dealer_hand)}")
                break
            else:
                print("invalid choice.only enter h or s")
    
    print(compare(calculate_hand(player_hand),calculate_hand(dealer_hand)))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  blackjack() 
