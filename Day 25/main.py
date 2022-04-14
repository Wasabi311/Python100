import turtle
import pandas

screen = turtle.Screen()# create a screen
screen.title("U.S.States Game") # create a title 
image = "blank_states_img.gif" 
screen.addshape(image) 
turtle.shape(image)


data = pandas.read_csv("50_states.csv")# read csv file
all_states = data.state.to_list()# convert data in column in csv file to a list
guessed_states = []# record the correct answers  


while len(guessed_states)<50:# only can guess 50 times 
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct",
                                    prompt = "What's another state's name ?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        #missing_states =[]
        #for state in all_states:
        #    if state not in guessed_states:
        #       missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break # exit while loop


    if answer_state in all_states:
        guessed_states.append(answer_state)# use list to record the correct answers
        t=turtle.Turtle() #turtle write the name on the screen
        t.hideturtle()# no turtle 
        t.penup()# no drawing line 
        state_data = data[data.state == answer_state]# pickng the row in csv 
        t.goto(int(state_data.x),int(state_data.y))# go to (x,y)
        t.write(answer_state) # write the name 







