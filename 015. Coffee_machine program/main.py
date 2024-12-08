MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(MENU['espresso']['ingredients']['coffee'])
profit=0
def report():
    '''print current resource level and profit'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f'Profit: {profit} $')

def is_resource_sufficient(drink):
    for item in drink['ingredients']:
        if resources[item]<drink['ingredients'][item]:
            print(f"sorry not enough {item}")
            return False
        return True
    
def make_coffee(choice,drink):
    for item in drink['ingredients']:
        resources[item]-=drink['ingredients'][item]
    print(f"here is your {choice} drink.Enjoy ☕")

def process_payment(drink_price):
    print("please insert coins and check if payment sufficient")
    print("insert coin")
    total=int(input("quarters(0.25$): "))*0.25
    total+=int(input("dimes(0.10$): "))*0.10
    total+=int(input("nickles(0.05$): "))*0.05
    total+=int(input("pennies(0.01$): "))*0.01
    if total>=drink_price:
        change=round(total-drink_price,2)
        print(f"Here is {change} in change")
        global profit
        profit+=drink_price
        return True
    else:
        print("not enough money")
        return False
    
def coffee_machine():
    is_on=True
    while is_on:
        choice=input("what would you like? (espresso/latte/cappuccino): ")
        if choice=='off':
            is_on=False
            print(f"the coffee machine turn off")
        elif choice=="report":
            report()
        elif choice in MENU:
            drink=MENU[choice]
            if is_resource_sufficient(drink):
                if process_payment(drink['cost']):
                    make_coffee(choice,drink)

coffee_machine()
