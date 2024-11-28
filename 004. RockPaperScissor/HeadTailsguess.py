import random

random_int=random.randint(0,1)
yourchoice=int(input("guess either heads,0 or tails,1.input either number 0 or 1 \n"))
if yourchoice==random_int:
    print("congratulations,correct guess")
else:
    print("wrong answer")
