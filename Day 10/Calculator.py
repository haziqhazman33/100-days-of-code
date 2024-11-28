from art import logo

print(logo)

def add(n1,n2):
    return n1+n2

def minus(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation={"+":add,"-":minus,"*":multiply,"/":divide}
def calc():
    num1=float(input("input first number: "))
    
    
    calc_continue=False

    while not calc_continue:
        symbol=(input("enter operation:+-* or /: "))
        
        while symbol not in operation:
            print("Invalid please restart program")
            symbol=(input("enter operation again (+,-,*,/): "))
    
        num2=float(input("input second number: "))

        calculation=operation[symbol]
        answer=calculation(num1,num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        response=input("continue: 'y' or 'n' ")
        if response=='y':
            num1=answer
        if response=='n':
            calc_continue=True            


calc()
