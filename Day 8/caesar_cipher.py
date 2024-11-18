alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
game_on=False

def caesar(start_text,shift_amt,direction):
    end_text=""
    if direction=="decode":
        shift_amt*=-1
    for char in text:
        if char in alphabet:
            new_pos=(alphabet.index(char)+shift_amt)%26
            end_text+=alphabet[new_pos]
        else:
            end_text+=char
    print(f"Here's the {direction}d result: {end_text}")

print(logo)
while game_on==False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amt=shift, direction=direction)
    result=input("Type 'yes' if you want to continue otherwise type 'no'\n")
    if result=='no':
        game_on=True
        print("goodbye")
