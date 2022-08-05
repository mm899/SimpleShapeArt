from canvas import Canvas
from shapes import Square, Rectangle

# Get the canvas width and height
canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))

# Make a dictionary of colour codes and prompt for colour
colours = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_colour = input("Enter the desired canvas colour (either white or black): ")

# Create the canvas with the defined parameters
canvas = Canvas(height=canvas_height, width=canvas_width, colour=colours[canvas_colour])

while True:
    shape_type = input("What would you like to draw (either 'rectangle' or 'square')? Enter quit to quit. ")

    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter the x value of the rectangle: "))
        rec_y = int(input("Enter the y value of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green should the rectangle have? "))
        blue = int(input("How much blue should the rectangle have? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, colour=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter the x value of the square: "))
        sqr_y = int(input("Enter the y value of the square: "))
        sqr_side = int(input("Enter the side length of the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green should the square have? "))
        blue = int(input("How much blue should the square have? "))

        # Create the rectangle
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, colour=(red, green, blue))
        s1.draw(canvas)

    # Break the loop if the user entered 'quit'
    if shape_type == 'quit':
        break

canvas.make("canvas.png")
