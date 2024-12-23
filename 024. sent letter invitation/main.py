with open ("./Input/Names/invited_names.txt") as file:
    content=file.readlines()
names=[]
for name in content:
    jk=name.strip('\n')
    names.append(jk)

with open ("./Input/Letters/starting_letter.txt") as file:
    content=file.read()
    for name in names:
        new_letter=content.replace("[name]",name)
        with open(f"./Output/ReadyToSend/{name}.txt",mode='w') as letter:
            letter.write(new_letter)
