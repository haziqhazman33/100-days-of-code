import turtle
import pandas as pd
image="blank_states_img.gif"

from tkinter import messagebox
  


#setup screen
screen=turtle.Screen()
screen.title("US state Game")
screen.setup(width=800,height=600)
screen.bgpic(image)

#load states data
data=pd.read_csv('50_states.csv')
states=data['state'].to_list() #['Alabama', 'Alaska', 'Arizona']

# state_data=data[data['state']=='Arizona']
# x,y=int(state_data.x),int(state_data.y)

writer=turtle.Turtle()
writer.hideturtle()
writer.penup()
def write_state(name,x,y):
    writer.goto(x,y)
    writer.write(name,align='center',font=('Arial',12,'normal'))

guessed_state=[]

while len(guessed_state)<len(states):
    answer_state=screen.textinput(title=f"{len(guessed_state)}/50 States Correct",prompt="What's another state's name?").title()
    print(answer_state)
    f"{len(guessed_state)}/50 States Correct"
    if answer_state=='Exit':
        missing_state=[]
        messagebox.showinfo("The End", "Thank you for playing") # The alert.
        for state in states:
            if state not in guessed_state:
                missing_state.append(state)
                #list convert into dataframe
                new_data = pd.DataFrame(missing_state)
                new_data.to_csv('state_to_learn.csv')
        break
    if answer_state in states:
        guessed_state.append(answer_state)
        state_data=data[data['state']==answer_state]
        write_state(answer_state,int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))

screen.exitonclick()
