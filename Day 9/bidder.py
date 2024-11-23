from art import logo
import os
bids={}
def place_bid(name,value):
    bids[name]=value
    
game_on=False
print(logo)
while not game_on:
    place_bid(name=input("please input name:"),value=int(input("please input bid amount:")))
    os.system('cls')
    other_bid=input("is there any other bidder left 'yes' or 'no':")
    if other_bid=="no":
        highest_value=max(bids.values())
        print(f"{highest_value} is now highest bid value")
        for name in bids:

            choice=input(f"{name}you want adds bids either 'yes' or 'no' ?")
            if choice=="yes":
                bids[name]=int(input(f"{name} add your bids: "))
 
        max_name=max(bids,key=bids.get)
        print(f"{max_name} win the biddest with value {bids[max_name]}")
        game_on=True
