print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input(
    'you\'re at a crossroad. where do you want to go? Type "left" or "right".')

if choice1 == "left":
    choice2 = input(
        ' you\'ve come to lake.There is an island in the middle of the lake.Type "wait" to wait for a boat.Type "swim" to swim across'
    ).lower()
    if choice2 == "wait":
        choice3 = input(
            "you arrive at the island unharmed.there is a house 3 doors. red,yellow and blue. which color do you choose?"
        )
        if choice3 == "blue":
            print("eaten by beast. Game Over")
        if choice3 == "red":
            print("your room full of fire.Game Over")
        if choice3 == "blue":
            print("you win the game.Congrats")
    else:
        print("attack by shark.game over")
else:
    print("fall into a hole.Game Over")
