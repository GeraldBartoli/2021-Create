#----Imports----

import turtle as trtl


#----Setup----

wn = trtl.Screen()
game = trtl.Turtle()
screen_width = 400
screen_height = 400
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "W", "X", "Y", "Z"]
#----Functions----

game.hideturtle()
game.penup()
game.goto(-300,300)
game.write("Test Of Quick Reactions Game", font=("Arial", 35, "bold"))
game.showturtle()
game.goto(-50,250)
game.write("RULES", font=("Arial", 30, "bold"))
game.goto(-50,200)
game.write("This is a game that will text your reaction", font=("Arial", 25, "bold"))









#----Funtion-Calls----

wn.listen()

wn.mainloop()