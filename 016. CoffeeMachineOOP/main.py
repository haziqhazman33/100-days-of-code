from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#the module for menu,coffee_maker,money_machine not included in code. refer 100 Days of Code: The Complete Python Pro Bootcamp in udemy . thank you.


Menu=Menu()
CoffeeMaker=CoffeeMaker()
MoneyMachine=MoneyMachine()
is_on=True
choice=""
while is_on:
    refer= ["latte", "espresso", "cappuccino", "report", "off"]
    choice=input(f"what would you like? {Menu.get_items()}: ")
    while choice not in refer:
        choice=input(f"what would you like? {Menu.get_items()}: ")

    if choice=='off':
        is_on=False
        print(f"the coffee machine turn off")
    elif choice=="report":
        print(CoffeeMaker.report())
    else:
        drink=Menu.find_drink(choice)
        print(drink)
        if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
            CoffeeMaker.make_coffee(drink)
