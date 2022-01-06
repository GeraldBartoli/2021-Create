#--Imports--#

import turtle as trtl
import random as rand

#--Setups--#

startx = 0
starty = 0

wn = trtl.Screen()
screen_width = 400
screen_height = 400

game = trtl.Turtle()
game.hideturtle()

scoreWriter = trtl.Turtle()
scoreWriter.hideturtle()

counter = trtl.Turtle()
counter.hideturtle()

timerUp = False
counterInterval = 1000
timer = 3

counter.penup()
counter.goto(-475,-400)

score = 0

fontSetup = ("Arial BOLD", 30, "normal")

letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "W", "X", "Y", "Z"]
shape_game = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
color_game = ["red", "blue", "green", "orange", "purple", "gold"]

game.speed("fastest")
counter.speed("fastest")
scoreWriter.speed("fastest")



#--Start-Screen--#

def startscreen():
    game.penup()

    game.goto(-300, 300)
    game.write("Test Of Quick Reactions Game", font=("Arial", 35, "bold"))

    game.goto(-50, 250)
    game.write("RULES", font=("Arial", 30, "bold"))

    game.goto(-300, 200)
    game.write("This is a game that will test your reaction time", font=("Arial", 20, "bold"))
    game.goto(-250, 175)
    game.write("A Shape will appear that's colored", font=("Arial", 20, "bold"))
    game.goto(-450, 100)
    game.write("Type into the console, the color and shape (Ex. red octagon)", font=("Arial", 20, "bold"))
    game.goto(-400, 75)
    game.write("The objects are there to distract you or to pay attention to", font=("Arial", 20, "bold"))
    game.goto(-325, 50)
    game.write("Theres a countdown telling the time you have left", font=("Arial", 20, "bold"))
    game.goto(-450, 25)
    game.write("If you do not complete type in time you'll lose.", font=("Arial", 20, "bold"))
    game.goto(-100, -50)
    game.write("Dont mess up what you type either", font=("Arial", 25, "bold"))
    game.goto(-130, -100)
    game.write("Press * to BEGIN", font=("Arial", 25, "bold"))
    game.goto(-160, -130)
    game.write("(don't press multiple times)", font=("Arial", 20, "italic"))
startscreen()

#--Shapes-Objects-Lines-#

#-Lines-#

def line1():
    game.pensize(10)
    game.forward(50)
    game.pensize(20)
    game.forward(100)
    game.pensize(30)
    game.forward(150)

def line2():
    game.pensize(20)
    game.backward(110)
    game.left(30)
    game.forward(100)
    game.left(70)
    game.forward(80)

def line3():
    game.pensize(50)
    game.forward(50)
    game.pensize(20)
    game.right(53)
    game.forward(30)
    game.pensize(12)
    game.forward(23)
    game.right(45)
    game.pensize(17)
    game.forward(40)
#Shapes/Objects#
def square_shape():
    game.shape('square')

def arrow_object():
    game.shape('arrow')

def turtle_object():
    game.shape('turtle')

def circle_shape():
    game.shape('circle')

def triangle_shape():
    game.shape('triangle')

def square_object():
    game.pendown()
    game.forward(50)
    game.right(90)
    game.forward(50)
    game.right(90)
    game.forward(50)
    game.right(90)
    game.forward(50)
    game.right(90)
    game.pendown()

def righttriangle_object():
    game.forward(100)
    game.left(90)
    game.forward(100)
    game.left(135)
    game.forward(142)

#--Random-Screens--#

def random_screen1():
    game.showturtle()
    game.pencolor("red")
    game.pendown()
    line2()
    game.penup()
def random_screen2():

    game.showturtle()
    game.pendown()
    game.pencolor("orange")
    line3()
    triangle_shape()
    game.pencolor("red")
    game.fillcolor("red")
    game.goto(0,50)
    game.penup()
    game.goto(-175,-122)
    game.pendown()
    square_object()
    game.penup()
    game.goto(-265, -58)
    game.pendown()
    game.speed("normal")
    square_object()
    game.penup()
    game.speed("fastest")
    game.pencolor("Cyan")
    game.pensize(50)
    game.goto(465, 300)
    game.speed("normal")
    game.pendown()
    square_object()
    game.speed("fastest")
    game.goto(350, 168)
    game.right(90)
    game.forward(170)
    game.right(180)
    wn.bgcolor("Blue")
    game.penup()
    game.goto(38, 29)
    game.pendown()
    game.pensize(10)
    game.pencolor("Purple")
    game.fillcolor('Purple')
    game.begin_fill()
    righttriangle_object()
    game.end_fill()
    turtle_object()
    game.pencolor("Green")
    game.fillcolor("Green")
    game.pensize(40)
    game.forward(100)
    game.right(90)
    game.forward(150)
    game.right(90)
    game.forward(200)
    game.right(90)
    game.forward(250)
    game.right(90)
    game.forward(300)
    game.right(90)
    game.forward(350)
    game.right(90)
    game.forward(400)
    game.right(90)
    game.pensize(10)
    game.forward(450)

    print("What as the [COLOR] and [SHAPE] of the drawer, when the Cyan shapes and lines were drawn.")
    type = input('')
    if type.lower() == 'red triangle':
        print("Nice")
        scoreChange()

        #-Stop-Timer-and-Proceed-#

    else:
        print("Nope that is not correct")
        print("Printing Final Score....")
        print("Score:",(score))
        print("") #-Line-Of-Space-#
        wn.bye()
    
    def countdown():
        global timer, timerUp
        counter.clear()
        if timer <= 0:
            counter.write("Time's Up", font=fontSetup)
            wn.bye()
            timerUp = True
        else:
            counter.write("Timer: " + str(timer), font=fontSetup)
            timer -= 1
            counter.getscreen().ontimer(countdown, counterInterval)


    wn.ontimer(countdown, counterInterval)

def scoreChange():
    global score
    score += 1





def random_screen3():
    game.showturtle()
    game.pencolor("green")


def random_screen4():
    game.showturtle()
    game.pencolor("blue")

def random_screen5():
    game.showturtle()
    game.pencolor("purple")

screenslist = [random_screen5, random_screen4, random_screen3, random_screen2, random_screen1]

def pickrandom_screen():
    rand.choice(screenslist)()

#--Start-Game--#

def startresetgame():
    game.clear()
    game.showturtle()
    pickrandom_screen()


#--Events--#

wn.onkeypress(startresetgame,"*")
wn.onkeypress("a")
wn.onkeypress("b")
wn.onkeypress("c")
wn.onkeypress("d")
wn.onkeypress("e")
wn.onkeypress("f")
wn.onkeypress("g")
wn.onkeypress("h")
wn.onkeypress("i")
wn.onkeypress("j")
wn.onkeypress("k")
wn.onkeypress("l")
wn.onkeypress("m")
wn.onkeypress("n")
wn.onkeypress("o")
wn.onkeypress("p")
wn.onkeypress("q")
wn.onkeypress("r")
wn.onkeypress("s")
wn.onkeypress("t")
wn.onkeypress("u")
wn.onkeypress("v")
wn.onkeypress("w")
wn.onkeypress("x")
wn.onkeypress("y")
wn.onkeypress("z")

wn.listen()

wn.mainloop()