import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color to white

# Create the turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(4)  # Set drawing speed

# Function to draw the heart shape
def draw_heart():
    pen.color("red")  # Heart color
    pen.begin_fill()  # Start filling the color

    pen.left(50)  # Turn the pen to the left by 50 degrees
    pen.forward(133)  # Move the pen forward
    pen.circle(50, 200)  # Draw a part of the circle (semi-circle)
    pen.right(140)  # Turn the pen to the right by 140 degrees
    pen.circle(50, 200)  # Draw another part of the circle (semi-circle)
    pen.forward(133)  # Move the pen forward to complete the heart shape

    pen.end_fill()  # End the filling of the heart color

# Write a message to the girlfriend
pen.penup()  # Lift the pen to move it without drawing
pen.goto(0, 200)  # Move the pen to a position above the heart
pen.pendown()  # Put the pen down to start drawing
pen.color("black")  # Set the color for text
pen.write("To My Lovely Girlfriend", align="center", font=("Arial", 16, "bold"))

# Draw the heart shape
pen.penup()  # Lift the pen to move it without drawing
pen.goto(0, -100)  # Move the pen to the starting position for the heart
pen.pendown()  # Put the pen down to start drawing
draw_heart()  # Call the function to draw the heart

# Hide the turtle (pen)
pen.hideturtle()

# Finish and keep the window open
turtle.done()
