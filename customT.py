import turtle
def drawSquare():
	window = turtle.Screen()
	window.bgcolor("blue")

	nate = turtle.Turtle()
	nate.shape("turtle")
	nate.color("white")


	for i in range(4):
		nate.forward(200)
		nate.right(90)

	window.exitonclick()


drawSquare()