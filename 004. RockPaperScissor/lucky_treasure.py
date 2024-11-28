from random import randint
print("welcome to island game.this island has treasure that is missing somewhere now its your turn to find it.so,GUd luck")
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
guess=int(input("if you guess correctly the position of treasure, it all yours.row and column from 1 to 3:"))
position = [randint(1,3),randint(1,3)]
print(position)
row = int(position[0])
column = int(position[1])

map[row-1][column-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
if guess==position:
    print(" fine,just keep it.")
else:
    print("lol, try again")
