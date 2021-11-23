# ----Imports----

import turtle as trtl

# ----Setup----

wn = trtl.Screen()
game = trtl.Turtle()
screen_width = 400
screen_height = 400
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "W", "X", "Y", "Z"]
# ----Functions----

game.speed("fastest")
game.hideturtle()


def startscreen():
    game.penup()
    game.goto(-300, 300)
    game.write("Test Of Quick Reactions Game", font=("Arial", 35, "bold"))

    game.showturtle()
    game.goto(-50, 250)
    game.write("RULES", font=("Arial", 30, "bold"))

    game.goto(-300, 200)
    game.write("This is a game that will test your reaction time", font=("Arial", 20, "bold"))
    game.goto(-250, 175)
    game.write("A Shape will appear that's colored", font=("Arial", 20, "bold"))
    game.goto(-245, 150)
    game.write("Each shape and color has a meaning", font=("Arial", 20, "bold"))
    game.goto(-325, 125)
    game.write("You will have to identify both and the meanings", font=("Arial", 20, "bold"))
    game.goto(-450, 100)
    game.write("They indicate inputs that you must type or mouse clicks on objects", font=("Arial", 20, "bold"))
    game.goto(-400, 75)
    game.write("The objects are there to distract you or to pay attention to", font=("Arial", 20, "bold"))
    game.goto(-325, 50)
    game.write("Theres a countdown telling the time you have left", font=("Arial", 20, "bold"))
    game.goto(-450, 25)
    game.write("If you do not sucessfully complete the inputs in time you'll lose.", font=("Arial", 20, "bold"))
    game.goto(-400, 0)
    game.write("You will also lose if you do the wrong thing, so be careful", font=("Arial", 20, "bold"))
    game.goto(-400, -25)
    game.write("Quick reactions, memorization are included in this game", font=("Arial", 20, "bold"))
    game.goto(-100, -50)
    game.write("Pay attention", font=("Arial", 25, "bold"))


# ----Funtion-Calls----

wn.listen()

wn.mainloop()
