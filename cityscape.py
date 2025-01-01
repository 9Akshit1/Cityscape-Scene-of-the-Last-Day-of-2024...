'''
ICS3U Turtles Function Assignment
Name: Akshit Erukulla
Date Started: November 10, 2024
Date Completed: November 19, 2024
Course Code: ICS3U
Program Title: A Christmas Cityscape Scene
Description: This program uses python's turtle library to draw a cityscape scene during winter. It consists of many different objects like buildings, perople, cars, trees, and even animations of clouds & snow. It is supposed to symbolize a city during wintertime.
Functions Written by Me: draw_van, draw_phone, draw_empire_state_building, draw_snowflake, draw_museum, draw_christmas_tree, draw_house, draw_observatory, draw_different_building, draw_person, draw_tree, draw_cloud, draw_xy_axis, draw_sun, draw_road_sidewalk_grass, draw_fence, draw_animated_clouds_snowflakes
Functions from other students (with student name): building_4 from Aaron Sethi, the three pizza building functions (pizza_shop, circle_square, pizza_build) from Swanish Baweja, the snowfall animation functions (create_snowflake, move_snowflake, snowfall_animation) from Aryan Grover, the draw_moon and draw_space_debris functions from Amol Sriprasadh
'''

import turtle, math, random, time

turtle.TurtleScreen._RUNNING = True
screen = turtle.Screen()
BG_COLOR = "#93F4FA"
screen.bgcolor(BG_COLOR) 
screen.tracer(0)     # Removes turtle movements. So, if you want to see the turtle drawing stuff, then comment this line

t = turtle.Pen()
t.shape("turtle")

# My Functions:
def draw_van(T, x, y, size, color):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): length of van
    color (string): color of van
    
    This function draws a van of any color 
    The bottom left of the van is at coordinate (0,0)
    '''
    # Drawing the Upper Body
    T.fillcolor(color)
    T.penup()
    T.pensize(1)
    T.setheading(0)
    T.goto(x, y)
    T.pendown()
    T.begin_fill()
    T.forward(size)    
    T.circle(size//120, 90)
    T.forward(size*1//3)
    T.circle(size//120, 90)
    T.forward(size*2//3)
    T.circle(size//120, 45)
    T.forward((2**0.5)*size*1//6)   #using 45-45-90 triangle
    T.right(45)
    T.forward(size//6)
    T.circle(size//120, 90)
    T.forward(size//6)
    T.end_fill()

    # Headlight & backlight
    T.fillcolor("#F8E76E")
    T.begin_fill()
    T.penup()
    T.goto(x, y + size//9)
    T.setheading(90)
    T.pendown()
    for i in range(4):
        T.forward(size//37)
        T.right(90)
    T.end_fill()

    T.fillcolor("#D3332A")
    T.begin_fill()
    T.penup()
    T.goto(x + size*36//37, y + size//27)
    T.setheading(90)
    T.pendown()
    for i in range(4):
        T.forward(size//37)
        T.right(90)
    T.end_fill()

    # Windows
    T.penup()
    T.goto(x + size*35//37, y + size//6)
    T.pendown()
    T.setheading(90)
    T.fillcolor("#425CB3")
    T.begin_fill()
    for i in range(2):
        T.forward(size*5//37)
        T.left(90)
        T.forward(size*7//37)
        T.left(90)
    T.end_fill()
    T.penup()
    T.forward(size*5//37)
    T.left(90)
    T.forward(size*8//37)
    T.pendown()
    T.fillcolor("#425CB3")
    T.begin_fill()
    for i in range(2):
        T.forward(size*7//37)
        T.left(90)
        T.forward(size*5//37)
        T.left(90)
    T.end_fill()
    T.penup()
    T.forward(size*8//37)
    T.pendown()
    T.fillcolor("#425CB3")
    T.begin_fill()
    T.left(90)
    T.forward(size*5//37)
    T.right(90)
    T.forward(size*10//37)
    T.right(135)
    T.forward((2**0.5)*(size*5//37))   #45-45-90 triangle
    T.right(45)
    T.forward(size*10//74)
    T.end_fill()

    # Design/Lining before the wheels
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.color('#F8E76E')
    T.fillcolor('#F8E76E')
    T.begin_fill()
    T.setheading(0)
    T.forward(size*5//37)
    T.forward(size*27//37)
    T.forward(size*4//37)
    T.forward(size//37)
    T.left(90)
    T.forward(size//37)
    T.left(90)
    T.forward(size)
    T.end_fill()

    T.penup()
    T.goto(x + size*10//37, y)
    T.pendown()
    T.color('#F8E76E')
    T.setheading(0)
    T.fillcolor('#F8E76E')
    T.begin_fill()
    T.left(90)
    T.circle(size*4//37, 180)
    T.left(90)
    T.end_fill()
    T.forward(size*27//37)
    T.forward(size*6//37)
    T.fillcolor('#F8E76E')
    T.begin_fill()
    T.left(90)
    T.circle(size*4//37, 180)
    T.right(90)
    T.end_fill()

    # Two wheels
    T.penup()
    T.setheading(90)
    T.goto(x + size*9//37, y)
    T.pendown()
    T.color('black')
    T.fillcolor('black')
    T.begin_fill()
    T.circle(size*3//37)
    T.end_fill()
    T.penup()
    T.goto(x + size*8//37, y)
    T.pendown()
    T.color(color)
    T.fillcolor(color)
    T.begin_fill()
    T.circle(size*2//37)
    T.end_fill()

    T.penup()
    T.goto(x + size*34//37, y)
    T.pendown()
    T.color('black')
    T.fillcolor('black')
    T.begin_fill()
    T.circle(size*3//37)
    T.end_fill()
    T.penup()
    T.goto(x + size*33//37, y)
    T.pendown()
    T.color(color)
    T.fillcolor(color)
    T.begin_fill()
    T.circle(size*2//37)
    T.end_fill()

def draw_phone(T, x, y, size, color):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): height of phone
    color (string): color of phone
    
    This function draws a phone of any color.
    The bottom left of the phone is at coordinate (x, y).
    '''
    T.hideturtle()
    T.penup()
    T.pensize(1)
    T.goto(x,y) # (0,0) is the center of the screen
    T.setheading(90) #E is 0, N is 90, W is 180, S is 270
    T.forward(size//8)
    T.pendown()

    # Phone body
    T.fillcolor(color)
    T.begin_fill()
    T.forward(size)
    T.right(90)
    T.forward(size//2)
    T.right(90)
    T.forward(size)
    T.right(90)
    T.forward(size//2)
    T.end_fill()

    # Phone button
    T.penup()
    T.right(180)
    T.forward(size//4)  #goto middle of width
    T.setheading(90) #E is 0, N is 90, W is 180, S is 270
    T.forward(size//8)
    T.right(90)
    T.forward(size//16)
    T.left(90)
    T.pendown()
    T.fillcolor("#000000")
    T.begin_fill()
    t.circle (size//16)
    T.left(90)
    T.penup()
    T.forward(size//16)   #center of button
    T.right(90)
    T.end_fill()

    # Phone screen
    T.forward(size//8)
    T.left(90)
    T.fillcolor("#000000")
    T.begin_fill()
    T.pendown()
    T.forward(size//5)
    T.right(90)
    T.forward(size//1.5)
    T.right(90)
    T.forward(2*size//5)
    T.right(90)
    T.forward(size//1.5)
    T.right(90)
    T.forward(size//5)
    T.end_fill()
    T.penup()

    # Phone camera
    T.setheading(90) #E is 0, N is 90, W is 180, S is 270
    T.forward(size//1.4)
    T.right(90)
    T.forward(size//50)
    T.pendown()
    T.fillcolor("#000000")
    T.begin_fill()
    T.left(90)
    T.circle(size//50)
    T.penup()
    T.end_fill()

def draw_empire_state_building(T, x, y, size):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): height of building
    
    This function draws a cool down-town looking building.
    The bottom left of the building is at coordinate (x, y).
    It returns the tower tip's coordinate which is used by the decorative big snowflake.
    '''

    T.hideturtle()
    T.speed(100)
    T.pensize(1)
    T.width(1)
    T.penup()
    T.goto(x,y) # (0,0) is the center of the screen
    T.setheading(90) #E is 0, N is 90, W is 180, S is 270
    T.color("black")
    T.pendown()

    # Building body
    T.fillcolor("#F9DA9A")
    T.begin_fill()
    T.forward(size//15)
    T.right(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//15)
    T.pensize(1)

    # Leftmost rectangle
    T.left(90)
    T.forward(size//8)
    T.right(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//15)
    T.pensize(1)

    # Righter & Higher Rectangle
    T.left(90)
    T.forward(size//10)
    T.right(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//30)
    T.pensize(1)

    # Righter & Higher Rectangle
    T.left(90)
    T.forward(size//3)
    T.right(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//40)
    T.pensize(1)

    # Righter & Higher Rectangle
    T.left(90)
    T.forward(size//15)
    T.right(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//40)
    T.pensize(1)

    # Top rectangle tower base
    T.left(90)
    T.forward(size//15)
    top_flat_x, top_flat_y = T.pos()
    T.right(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//8)
    T.pensize(1)
    T.right(90)
    T.forward(size//15)

    # Righter & Lower Rectangle
    T.left(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//40)
    T.pensize(1)
    T.right(90)
    T.forward(size//15)

    # Righter & Lower Rectangle
    T.left(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//40)
    T.pensize(1)
    T.right(90)
    T.forward(size//3)

    # Righter & Lower Rectangle
    T.left(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//30)
    T.pensize(1)
    T.right(90)
    T.forward(size//10)

    # Righter & Lower Rectangle
    T.left(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//15)
    T.pensize(1)
    T.right(90)
    T.forward(size//8)

    # Rightmost Rectangle
    T.left(90)
    T.pensize(5)
    T.color("#62432C")
    T.forward(size//15)
    T.pensize(1)
    T.right(90)
    T.forward(size//15)
    T.color("#F9DA9A")

    # Building base
    T.right(90)
    T.forward(size//2)
    T.end_fill()

    #Extra line details
    T.penup()
    T.color("black")
    T.pensize(1)
    T.goto(x, y) 
    T.setheading(90) 
    T.pendown()
    T.forward(size//15)
    T.right(90)
    width = 2*(size//15 + size//15 + size//30 + + size//40 + size//40) + size//8
    T.color("#62432C")
    T.pensize(5)
    T.forward(width)
    T.pensize(1)
    T.color("black")
    T.backward(2*size//15)
    T.left(90)
    T.forward(size//8 + 2/5 * size//10)
    T.left(90)
    T.color("#62432C")
    T.pensize(5)
    T.forward(3*size//30)
    T.pensize(1)
    T.color("black")
    T.left(90)
    T.forward(size//8 + 2/5 * size//10)
    T.left(90)
    T.backward(width - 7*size//15 + 3*size//30)   
    T.left(90)
    T.forward(size//8 + 2/5 * size//10)
    T.right(90)
    T.color("#62432C")
    T.pensize(5)
    T.forward(3*size//30)
    T.pensize(1)
    T.color("black")
    T.right(90)
    T.forward(size//8 + 2/5 * size//10)
    T.backward(size//8 + 2/5 * size//10)
    T.left(90)
    T.backward(2*size/30)
    T.left(90)
    T.forward(3/5 * size//10 + size//3)
    T.right(90)
    T.color("#62432C")
    T.pensize(5)
    T.forward(3*size//40)
    T.pensize(1)
    T.color("black")
    T.right(90)
    T.forward(size//3 + 1/5 * size//10)
    T.left(90)
    T.forward(3*size//40)
    T.left(90)
    T.forward(size//3 + 1/5 * size//10)
    T.right(90)
    T.color("#62432C")
    T.pensize(5)
    T.forward(3*size//40)
    T.pensize(1)
    T.color("black")
    T.right(90)
    T.forward(3/5 * size//10 + size//3)
    T.backward(3/5 * size//10 + size//3)
    T.left(90)
    T.backward(2*size/40)
    T.left(90)
    T.forward(size//15)
    T.backward(size//15)
    T.right(90)
    T.backward(size//40)
    T.left(90)
    T.backward(size//3 + 1/5 * size//10)
    T.left(90)
    T.color("#62432C")
    T.pensize(5)
    T.forward(3*size//40)
    T.pensize(1)
    T.color("black")
    T.right(90)
    T.forward(size//3 + 1/5 * size//10)
    T.left(90)
    T.forward(size//40)
    T.right(90)
    T.forward(size//15)
    T.left(90)

    # Tower tip
    T.penup()
    T.goto(top_flat_x, top_flat_y)
    T.setheading(0)
    T.pendown()
    T.fillcolor("#61432B")
    T.begin_fill()
    T.left(60)
    T.forward(2*size//30)
    T.left(35)
    T.forward(2*size//140)
    T.right(35)
    T.forward(2*size//45)
    T.left(25)
    T.forward(2*size//15)
    tower_tip_pos = T.pos()
    T.right(170)
    T.forward(2*size//15)
    T.left(25)
    T.forward(2*size//45)
    T.right(35)
    T.forward(2*size//140)
    T.left(35)
    T.forward(2*size//30)
    T.right(120)
    T.forward(2*(size//45 + 2*size/2//30))   #using 30-60-90 triangle
    T.end_fill()

    # Windows (a really troublesome part here)
    window_height = (size//15 - size//100)*1//2
    window_width = window_height
    window_vertical_between_space = 1.6*window_height
    window_horizontal_between_space = window_width//2
    window_layers_left_bottom_corner_pos = [(x, y), 
                                            
                                            (x + size//15 + size//120, y + size//15 + 2), 
                                            (x + size//15 + size//15 + size//120, y + size//15 + 2), 
                                            (x + size//15 + size//15 + 3*size//30 + 2*size//120, y + size//15 + 2), 
                                            (x + size//15 + size//15 + 3*size//30 + size//120 + 2.4*size//30, y + size//15 + 2), 
                                            (x + size//15 + size//15 + 3*size//30 + size//120 + 2.4*size//30 + 3*size//30, y + size//15 + 2), 

                                            (x + size//15 + size/15 - size//240, y + size//15 + size//8 + size//30 + 4), 
                                            (x + size//15 + size/15 + size//30 + size//120, y + size//15 + size//8 + size//30 + 4), 
                                            (x + size//15 + size/15 + size//30 + 3*size//40 + 2.4*size//30, y + size//15 + size//8 + size//30 + 4),
                                            (x + size//15 + size/15 + size//30 + 3*size//40 + 2.4*size//30 + 2*size//40 + 1.8*size/120, y + size//15 + size//8 + size//30 + 4),

                                            (x + size//15 + size//15 + 3*size//30 + 2*size//120, y + size//15 + size//8 + size//30 + size//23 + 4), 

                                            (x + size//15 + size/15 + size//30 + size//60 + size//240, y + size//15 + size//8 + size//10 + size//3 + size//180 + 2),
                                            (x + size//15 + size/15 + size//30 + 1.4*size//30 + 0.7*size//60, y + size//15 + size//8 + size//10 + size//3 + size//60), 
                                            (x + size//15 + size/15 + size//30 + 1.4*size//30 + size//8, y + size//15 + size//8 + size//10 + size//3 + size//180 + 2)]
    window_layers_rows_columns = [(1, 13), 
                                  
                                  (2, 1), 
                                  (3, 2),
                                  (4, 1),
                                  (3, 2),
                                  (2, 1),

                                  (1, 1.7),
                                  (8, 1),
                                  (8, 1),
                                  (1, 1.7),

                                  (8, 1),

                                  (1, 1.5),
                                  (2, 3.8),
                                  (1, 1.5)]
    for i in range(0, 14):
        rows, columns = window_layers_rows_columns[i][0], window_layers_rows_columns[i][1]
        for r in range(0, rows):
            T.penup()
            T.goto(window_layers_left_bottom_corner_pos[i][0], window_layers_left_bottom_corner_pos[i][1])
            T.setheading(90)
            T.forward(window_height//2 + window_vertical_between_space*r)
            T.setheading(0)
            for c in range(int(columns)):
                if isinstance(columns, float):    # Basically a signal that the windows should be smaller so they fit within the building's space
                    scale_factor = columns - int(columns)
                else:
                    scale_factor = 1

                T.forward(window_horizontal_between_space*scale_factor)
                T.left(90)

                T.pencolor("#AE9C8C")
                T.fillcolor("#AE9C8C")
                T.begin_fill()
                T.pendown()
                T.forward(window_height*scale_factor)
                T.right(90)
                T.forward(window_width*scale_factor)
                T.right(90)
                T.forward(window_height*scale_factor)
                T.right(90)
                T.forward(window_width*scale_factor)
                T.end_fill()

                T.penup()
                T.right(180)
                T.forward(window_width*scale_factor)
                
    return tower_tip_pos

def draw_snow_flake(T, x , y, size, thickness):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): size of snow flake
    thickess (int): thickness of pen which affects snowflake line thickness
    
    This function draws a snow flake at coordinate (x,y) with a specified size.
    '''

    T.hideturtle()
    T.speed(1000000)
    T.penup()
    T.goto(x,y) 
    T.color("#FFFFFF")
    T.width(3)
    T.pensize(thickness)
    T.pendown()

    # Lines
    for i in range(0, 3):
        T.setheading(90) 
        T.right(60*i)

        # Long appendage
        T.forward(size//2)
        T.backward(size//6)
        T.right(50)

        #Short appendages
        T.forward(size//6)
        T.backward(size//6)
        T.left(100)
        T.forward(size//6)
        T.backward(size//6)
        T.right(50)

        # Long appendage
        T.backward(size//2 + 2*size//6)
        T.right(180)   
        T.backward(size//6)
        T.right(50)

        # Short appendages
        T.forward(size//6)
        T.backward(size//6)
        T.left(100)
        T.forward(size//6)
        T.backward(size//6)
        T.right(50)
        T.backward(2*size//6)

def draw_museum(T, x, y, size):  
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): size of museum
    
    This function draws a musesum at coordinate (x,y) with a specified size.
    '''

    #Dome
    T.penup()
    T.pensize(1)
    T.speed(100)
    T.setheading(0)
    T.goto(x, y)  
    T.pendown()
    T.color("saddlebrown")
    T.begin_fill()
    T.circle(size//4)
    T.end_fill()
    T.goto(x - size//80, y + 3*size//10)
    T.color("white")
    t.write("M", align="center", font=("Arial", size//9, "bold"))

    #Bottom rectangle
    T.pensize(1)
    T.color("black")
    T.penup()
    T.goto(x - size//2, y - 11*size//20)
    T.pendown()
    T.begin_fill()
    for i in range(2):
        T.forward(size)
        T.left(90)
        T.forward(size//20)
        T.left(90)
    T.end_fill()

    #Second from bottom rectangle
    T.penup()
    T.goto(x - 7*size//16, y - size//2)  
    T.pendown()
    T.color("chocolate")
    T.begin_fill()
    for i in range(2):
        T.forward(7*size//8)
        T.left(90)
        T.forward(size//20)
        T.left(90)
    T.end_fill()

    #Main part of building
    T.penup()
    T.goto(x - 3*size//8, y - 9*size//20)
    T.pendown()
    T.color("sandybrown")
    T.begin_fill()
    for i in range(2):
        T.forward(3*size//4)
        T.left(90)
        T.forward(5*size//8)
        T.left(90)
    T.end_fill()

    #Second from top rectangle
    T.penup()
    T.goto(x - 7*size//16, y + 7*size//40)
    T.pendown()
    T.color("chocolate")
    T.begin_fill()
    for i in range(2):
        T.forward(7*size//8)
        T.left(90)
        T.forward(size//20)
        T.left(90)
    T.end_fill()

    #Top rectangle
    T.penup()
    T.goto(x - 3*size//8, y + 9*size//40)
    T.pendown()
    T.color("sienna")
    T.begin_fill()
    for i in range(2):
        T.forward(3*size//4)
        T.left(90)
        T.forward(size//20)
        T.left(90)
    T.end_fill()

    #Windows
    x_window = x - 5*size//16
    y_window = y + size//40
    T.color("khaki")

    #Windows
    for i in range(3): 
        for i in range(4): 
            T.penup()
            T.goto(x_window, y_window)
            T.pendown()
            T.begin_fill()
            for i in range(4):
                T.forward(size//10)
                T.left(90)
            T.end_fill()
            x_window += 7*size//40    # Move right to next window

        x_window = x - 5*size//16 
        y_window -= 17*size//80   # Move down to next row of windows

def draw_christmas_tree(T,x,y,size):  
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): height of christmas tree

    This function draws a christmas tree at coordinate (x, y) with a specified size.
    '''

    # Top triangle
    T.penup()
    T.pensize(1)
    T.setheading(0)
    T.setposition(x-3*size//13,y+5*size//13)
    T.pendown()
    T.fillcolor('green')
    T.begin_fill()
    T.forward(6*size//13)
    T.left(130)  
    T.forward(19*size//52)
    T.left(100)  
    T.forward(19*size//52)
    T.end_fill()

    # Middle trapezoid
    T.setx(x-7*size//52)
    T.fillcolor('green')
    T.begin_fill()
    T.forward(5*size//13)
    T.left(130)  
    T.forward(10*size//13)
    T.left(130)  
    T.forward(5*size//13)
    T.end_fill()

    # Bottom trapezoid
    T.penup()
    T.setposition(x-9*size//52,y+6*size//65)
    T.pendown()
    T.fillcolor('green')
    T.begin_fill()
    T.left(100)  
    T.forward(size//2)
    T.left(130)  
    T.forward(size)
    T.left(130) 
    T.forward(size//2)
    T.end_fill()

    # Trunk
    T.penup()
    T.setposition(x-3*size//26,y-15*size//52)
    T.pendown()
    T.fillcolor('brown')
    T.begin_fill()
    T.left(140) 
    T.forward(5*size//26)
    T.left(90)   
    T.forward(6*size//26)
    T.left(90)  
    T.forward(5*size//26)
    T.end_fill()

    # Star on the top
    T.penup()
    T.setposition(x-size//10,y+19*size//26)
    T.right(90)
    T.pendown()
    T.fillcolor('yellow')
    T.begin_fill()
    for i in range(5):
        T.forward(size//13)
        T.left(72)
        T.forward(size//13)
        T.right(144)
    T.end_fill()
    T.hideturtle()

    # Lights
    L1=turtle.Turtle()
    L2=turtle.Turtle()
    L3=turtle.Turtle()

    L1.penup()
    L1.setposition(x,y-size//13)
    L1.pendown()
    L1.hideturtle()

    L2.penup()
    L2.setposition(x,y+3*size//13)
    L2.pendown()
    L2.hideturtle()

    L3.penup()
    L3.setposition(x,y+size//2)
    L3.pendown()
    L3.hideturtle()

    # Turning lights "on"
    L1.dot(size//13,'red')
    L2.dot(size//13,'yellow')
    L3.dot(size//13,'cyan')

def draw_house(T, x, y, size):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): length of base of house, though base is slightly shorter than it
    
    This function draws a house with a roof, a door, and windows.
    The bottom left of the house is at coordinate (x,y).
    '''
    T.penup()
    T.goto(x, y)
    T.pensize(1)
    T.pendown()

    T.pencolor("#947748")
    T.pensize(2)

    # Base
    T.setheading(0)
    T.forward(9/10*size)
    T.backward(1/4*size)
    T.left(90)

    # Rightmost section
    T.color("#49524b")
    T.begin_fill()
    T.forward(1/5*size)
    T.left(90)
    T.forward(1/300*size)
    T.right(90)
    T.forward(1/200*size)
    T.left(90)
    T.forward(1/200*size)
    T.right(90)
    T.forward(1/200*size)
  
    T.left(90)
    T.forward(3/20*size)
    T.left(120)
    T.forward(1/40*size)
    T.right(120)
    T.forward(1/50*size)
    T.left(90)
    T.forward(19/100*size)
    T.end_fill()

    T.right(90)
    T.forward(7/40*size)

    # Middle section
    T.speed(5)
    T.color("#1b211d")
    T.begin_fill()
    T.right(90)
    T.forward(19/100*size)
    T.left(90)
    T.forward(1/200*size)
    T.left(90)
    T.forward(19/100*size)

    T.color("#49524b")
    T.left(90)
    T.forward(173/1000*size)  
    T.left(135)
    T.forward(250/1000*size)
    T.end_fill()
    T.backward(250/1000*size)
    T.right(135)

    T.pencolor("#1b211d")
    T.fillcolor("#49524b")  
    T.begin_fill()
    T.left(90)
    T.forward(19/100*size)
    T.right(90)
    T.forward(1/200*size)
    T.right(90)
    T.forward(19/100*size)

    T.backward(19/100*size)
    T.right(90)
    T.forward(1/500*size)
    T.forward(9/50*size)
    T.end_fill()

    # Leftmost Section
    T.speed(5)
    T.color("#49524b")
    T.begin_fill()
    T.forward(48/250*size)
    T.left(90)
    T.forward(19/100*size)
    T.left(90)
    T.forward(193/1000*size)
    T.end_fill()
    T.left(90)
    T.forward(19/100*size)

    T.speed(5)
    T.color("#1b211d")
    T.begin_fill()
    T.left(90)
    T.forward(39/200*size)
    T.left(90)
    T.forward(19/100*size)
    T.right(90)
    T.forward(7/1000*size)
    T.right(90)
    T.forward(19/100*size)
    T.left(90)
    T.forward(3/1000*size)
    T.right(90)
    T.forward(1/200*size)
    T.left(90)
    T.forward(3/1000*size)
    T.right(90)
    T.forward(7/1000*size)
    T.right(90)
    T.forward(47/250*size)
    T.right(135)
    T.forward(4/250*size)
    T.end_fill()
    T.right(225)

    # Roof
    T.speed(5)
    T.color("#b84221")
    T.begin_fill()
    T.right(-45)
    T.forward(9/50*size)
    T.right(94)
    T.forward(17/100*size)
    T.right(131)
    T.forward(12/50*size)
    T.end_fill()

    T.speed(5)
    T.begin_fill()
    T.right(-225)
    T.forward(33/100*size)
    T.right(94)
    T.forward(57/200*size)
    T.right(131)
    T.forward(3/10*size)
    T.end_fill()

    T.speed(5)
    T.left(90)
    T.forward(1/100*size)
    T.right(90)
    T.forward(31/100*size)

    T.begin_fill()
    T.right(-225)
    T.forward(13/100*size)
    T.right(45)
    T.forward(2/10*size)
    T.right(-225)
    T.forward(13/100*size)
    T.end_fill()

    T.speed(5)
    T.color("#18191f")
    T.right(45)
    T.forward(2/10*size)
    T.right(-225)
    T.forward(13/100*size)
    T.right(45)
    T.forward(39/200*size)
    T.right(-45)
    T.forward(19/100*size)
    T.right(94)
    T.forward(287/1000*size)
    T.right(-229)
    T.forward(39/200*size)
    T.right(225)
    T.forward(7/250*size)
    T.right(-225)
    T.forward(5/20*size)
    T.right(135)
    T.forward(9/50*size)
    T.right(91)
    T.forward(17/100*size)

    T.right(134)
    T.forward(6/25*size)

    # Windows
    T.speed(5)
    T.penup()
    T.left(90)
    T.forward(1/20*size)
    T.pendown()
    T.color("#91bfbe")
    T.begin_fill()
    T.forward(11/200*size)
    T.right(90)
    T.forward(13/100*size)
    T.right(90)
    T.forward(11/200*size)
    T.right(90)
    T.forward(13/100*size)
    T.end_fill()

    T.speed(10)
    T.color("#38393d")
    T.right(90)
    T.forward(11/200*size)
    T.right(90)
    T.forward(13/100*size)
    T.right(90)
    T.forward(11/200*size)
    T.right(90)
    T.forward(13/100*size)

    T.right(90)
    T.forward(11/200*size)
    T.right(90)
    T.forward(13/200*size)
    T.right(90)
    T.forward(11/200*size)

    T.right(90)
    T.forward(13/200*size)
    T.right(90)
    T.forward(11/400*size)
    T.right(90)
    T.forward(13/100*size)

    # Door
    T.color("#473728")
    T.penup()
    T.left(90)
    T.forward(23/200*size)
    T.left(90)
    T.forward(9/40*size)
    T.pendown()

    T.begin_fill()
    T.left(90)
    T.forward(27/200*size)
    T.right(90)
    T.forward(13/200*size)
    T.right(90)
    T.forward(27/200*size)
    T.end_fill()

    T.penup()
    T.left(90)
    T.forward(19/200*size)
    T.left(90)
    T.forward(1/10*size)
    T.pendown()

    T.color("#91bfbe")
    T.begin_fill()
    T.forward(1/20*size)
    T.right(90)
    T.forward(19/200*size)
    T.right(90)
    T.forward(1/20*size)
    T.right(90)
    T.forward(19/200*size)
    T.end_fill()

    T.color("#38393d")
    T.right(90)
    T.forward(1/20*size)
    T.right(90)
    T.forward(19/200*size)
    T.right(90)
    T.forward(1/20*size)
    T.right(90)
    T.forward(19/200*size)

    T.right(90)
    T.forward(1/40*size)
    T.right(90)
    T.forward(19/200*size)
    T.right(90)
    T.forward(1/40*size)
    T.right(90)
    T.forward(19/400*size)
    T.right(90)
    T.forward(1/20*size)

def draw_observatory(T, x, y, size, layers=9):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    layers (int): number of decorative layers
    size (float): height of observatory
    
    This function draws a observatory at coordinate (x,y) with a specified size and an amount of decorative layers
    '''
    T.up()
    T.goto(x, y)
    T.pendown()
    T.pensize(0)
    T.color("#609D9F")

    # Body
    T.setheading(90)
    T.fillcolor("#609D9F")
    T.begin_fill()
    T.forward(4*size//5)
    T.right(90)
    T.forward(size//2)
    T.right(90)
    T.forward(4*size//5)
    T.right(90)
    T.forward(size//2)
    T.end_fill()

    # Circular Roof
    T.setheading(90)
    T.penup()
    T.forward(3.8*size//5)
    T.right(90)
    T.forward(size//2)
    T.forward(size//40)
    T.left(90)
    T.fillcolor("#324E55")
    T.begin_fill()
    T.circle(size//4 + size//40, 90)
    T.end_fill()
    T.left(90)
    T.forward(size//40)  
    T.right(90)
    T.pendown()
    T.fillcolor("#609D9F")
    T.begin_fill()
    T.circle(size//4)
    T.end_fill()

    # Telescope Part 1: Thin cylinder
    T.setheading(0)
    T.penup()
    T.forward(size//6)
    T.right(90)
    T.forward(size//12)
    T.setheading(45)
    T.forward(size//30)
    T.pendown()
    T.fillcolor("#AEC4DD")
    T.begin_fill()
    T.forward(size//30)
    T.right(90)
    T.forward(size//45)
    T.right(90)
    T.forward(size//30)
    T.right(90)
    T.forward(size//45)
    T.right(90)
    T.end_fill()
    T.forward(size//30)
    T.left(90)

    # Telescope Part 2: Medium cylinder
    T.fillcolor("#AEC4DD")
    T.begin_fill()
    T.forward(size//70) 
    T.right(90)
    T.forward(size//15)  
    T.right(90)
    T.forward(2*size//70 + size//45)  
    T.right(90)
    T.forward(size//15) 
    T.right(90) 
    T.forward(size//70 + size//45)
    T.end_fill()
    T.forward(size//70)
    T.right(90)
    T.forward(size//15) 
    T.left(90)
    
    # Telescope Part 3: Big cylinder
    T.fillcolor("#AEC4DD")
    T.begin_fill()
    T.forward(size//70) 
    T.right(90)
    T.forward(1.5*size//15)  
    T.right(90)
    T.forward(4*size//70 + size//45)  
    T.right(90)
    T.forward(1.5*size//15) 
    T.right(90) 
    T.forward(3*size//70 + size//45)
    T.end_fill()
    T.forward(size//70)
    T.right(90)
    T.forward(1.5*size//15) 
    T.right(90)
    T.forward(5.2*size//70)
    T.left(90)

    # Telescope Part 4: Circular lens
    T.fillcolor("#FFFFFF")
    T.begin_fill()
    T.circle(2.6*size//70, 180)
    T.end_fill()
    T.right(90)
    T.forward(size//90)

    # Telescope Part 5: Flat lens base
    T.fillcolor("#AEC4DD")
    T.begin_fill()
    T.forward(size//70) 
    T.right(90)
    T.forward(size//45)  
    T.right(90)
    T.forward(6*size//70 + size//45)  
    T.right(90)
    T.forward(size//45) 
    T.right(90) 
    T.forward(5*size//70 + size//45)
    T.end_fill()
    T.forward(size//70)
    T.right(90)
    T.forward(size//45) 
    T.right(90)
    T.forward(5.6*size//70)
    T.left(90)

    # Door 1
    T.penup()
    T.goto(x, y)
    T.setheading(0)
    T.forward(size//4)  
    T.left(90)
    T.fillcolor("#98CFCE")
    T.begin_fill()
    T.forward(size//6)
    T.right(90)
    T.forward(size//8)
    T.right(90)
    T.forward(size//6)
    T.right(90)
    T.forward(size//8)
    T.end_fill()

    #Door 2
    T.fillcolor("#98CFCE")
    T.begin_fill()
    T.forward(size//8)
    T.right(90)
    T.forward(size//6)
    T.right(90)
    T.forward(size//8)
    T.right(90)
    T.forward(size//6)
    T.end_fill()

    # Window 1
    T.penup()
    T.backward(size//6)
    T.left(90)
    T.backward(size//12)
    T.right(90)
    T.forward(size//9)
    T.left(90)
    T.pendown()
    T.fillcolor("#C7C5C6")
    T.begin_fill()
    T.forward(size//16)
    T.left(90)
    T.forward(size//12)
    T.left(90)
    T.forward(size//16)
    T.left(90)
    T.forward(size//12)
    T.end_fill()

    # Window 2
    T.penup()
    T.left(90)
    T.forward(2*size//12)
    T.left(90)
    T.pendown()
    T.fillcolor("#C7C5C6")
    T.begin_fill()
    T.forward(size//12)
    T.left(90)
    T.forward(size//16)
    T.left(90)
    T.forward(size//12)
    T.left(90)
    T.forward(size//16)
    T.end_fill()

    # Layers
    for i in range(0, layers):
        T.penup()
        layer_height = size//15
        T.goto(x, y + size//5 + i * layer_height)   # Append above doors
        T.setheading(90)

        # Light Blue Rectangle Layer
        T.pendown()
        T.fillcolor("#ABF1ED")
        T.begin_fill()
        T.forward(layer_height)
        T.right(90)
        T.forward(size//2)
        T.right(90)
        T.forward(layer_height)
        T.right(90)
        T.forward(size//2)
        T.right(90)
        T.end_fill()

        # Dark Blue thin Band
        T.forward(2/3 * layer_height)
        T.fillcolor("#108585")
        T.begin_fill()
        T.right(90)
        T.backward(1/6 * layer_height)
        T.left(90)
        T.forward(1/3 * layer_height)
        T.right(90)
        T.forward(size//2 + 2*1/6 * layer_height)
        T.right(90)
        T.forward(1/3 * layer_height)
        T.right(90)
        T.forward(size//2 + 2*1/6 * layer_height)
        T.end_fill()

        # Circular edges for thin band
        T.right(90)
        T.forward(1/3 * layer_height)
        T.left(90)
        T.fillcolor("#108585")
        T.begin_fill()
        T.circle(1/6 * layer_height)
        T.end_fill()
        T.right(180)
        T.forward(size//2 + 2*1/6 * layer_height)
        T.right(90)
        T.forward(1/3 * layer_height)
        T.left(90)
        T.fillcolor("#108585")
        T.begin_fill()
        T.circle(1/6 * layer_height)
        T.end_fill()

def draw_different_building(T, x, y, size, color):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): height of building
    color (string): main body color of building
    
    This function draws a building with windows at bottom-left coordinate (x,y) with a specified size and color
    '''
    T.up()
    T.goto(x, y)
    T.pendown()
    T.pensize(1)

    #Main body
    T.setheading(90)
    T.fillcolor(color)
    T.begin_fill()
    T.forward(9*size//10)
    T.right(90)
    T.forward(size//10)
    T.left(90)
    T.forward(size//10)
    T.right(90)
    T.forward(3*size//10)
    T.right(90)
    T.forward(size//10)
    T.left(90)
    T.forward(2*size//10)
    T.right(90)
    T.forward(9*size//10)
    T.right(90)
    T.forward(6*size//10)
    T.end_fill()

    #Roof/Edges
    T.penup()
    T.goto(x, y)
    T.setheading(90)
    T.forward(2*size//10)
    T.left(90)
    T.forward(size//50)
    T.right(90)
    T.pendown()
    T.fillcolor("#E1D9B6")
    T.begin_fill()
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 6*size//10)
    T.right(90)
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 6*size//10)
    T.end_fill()

    T.penup()
    T.setheading(90)
    T.forward(5*size//10)
    T.pendown()
    T.fillcolor("#E1D9B6")
    T.begin_fill()
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 6*size//10)
    T.right(90)
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 6*size//10)
    T.end_fill()

    T.penup()
    T.setheading(90)
    T.forward(2*size//10)
    T.pendown()
    T.fillcolor("#E1D9B6")
    T.begin_fill()
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 6*size//10)
    T.right(90)
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 6*size//10)
    T.end_fill()

    T.penup()
    T.goto(x + size//10, y + size)
    T.setheading(90)
    T.left(90)
    T.forward(size//50)
    T.right(90)
    T.pendown()
    T.fillcolor("#E1D9B6")
    T.begin_fill()
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 3*size//10)
    T.right(90)
    T.forward(size//50)
    T.right(90)
    T.forward(2*size//50 + 3*size//10)
    T.end_fill()

    #Windows
    window_height = 1/3 * 2*size//10
    window_width = size//20
    window_x_spaces = [size//20, 4/5 * size//10, size//80, size//80, size//80, 4/5 * size//10]
    window_y_pos = [1/3 * 2*size//10, 2*size//10 + 1/3 * 2*size//10, 3*size//10 + 1/3 * 2*size//10, 4*size//10 + 1/3 * 2*size//10, 5*size//10 + 1/3 * 2*size//10, 7*size//10 + 1/3 * 2*size//10]
    for g in range(0, len(window_y_pos)):
        T.penup()
        T.goto(x, y + window_y_pos[g])
        for j in range(0, len(window_x_spaces)):
            T.penup()
            T.setheading(0)
            T.forward(window_x_spaces[j])
            T.setheading(90)
            T.pendown()
            T.fillcolor("#EBAD38")
            T.begin_fill()
            for i in range(2):
                T.forward(window_height)
                T.right(90)
                T.forward(window_width)
                T.right(90)
            T.end_fill()
            T.setheading(0)
            T.forward(window_width)

def draw_person(T, x, y, size, gender):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): starting x-coordinate
    y (float): starting y-coordinate
    size (float): height of the person
    gender (string): "male" or "female" which affects clothing and hairstyle

    This function draws a person with male or female clothing. Left toe is the (x, y). Ignore the stereotypicalness of the clothing.
    '''
    # Hair
    if gender == "female":  
        # Draw trapezoidal long hair
        T.penup()
        T.goto(x + size*2.2/3, y + size*7/3)
        T.setheading(90)
        T.pendown()
        T.color("brown")
        T.fillcolor("brown")
        T.begin_fill()
        T.circle(size*2/5, 180)
        T.goto(x - size*2/5, y + size*4/3)
        T.goto(x + size*2/5, y + size*4/3)
        T.goto(x + size*2.2/3, y + size*7/3)
        T.end_fill()
    elif gender == "male":
        #Draw short circular hair
        T.penup()
        T.goto(x + size*2.2/3, y + size*7/3)
        T.setheading(90)
        T.pendown()
        T.color("brown")
        T.fillcolor("brown")
        T.begin_fill()
        T.circle(size*2/5, 180)
        T.end_fill()

    # Draw stickman 
    T.penup()
    T.color("black")
    T.pensize(2)
    T.goto(x, y)
    T.hideturtle()
    T.setheading(90)
    T.pendown()

    # Legs
    T.right(30)
    T.forward(size*2//3)
    T.right(120)
    T.forward(size*2//3)
    T.backward(size*2//3)
    T.left(150)

    # Abdomen
    T.forward(size)

    # Arms
    T.left(135)
    T.forward(size*2//3)
    T.backward(size*2//3)
    T.right(270)
    T.forward(size*2//3)
    T.backward(size*2//3)
    T.left(135)

    # T-shirt
    T.color("yellow")
    T.setheading(0)
    T.pendown()
    T.begin_fill()
    T.forward(size//6)
    T.right(45)
    T.forward(size//3)
    T.right(90)
    T.forward(size//6)
    T.right(90)
    T.forward(size//3 - size//6)
    T.left(135)
    T.forward(size//2)
    T.right(90)
    T.forward(size//3)
    T.right(90)
    T.forward(size//2)
    T.left(135)
    T.forward(size//3 - size//6)
    T.right(90)
    T.forward(size//6)
    T.right(90)
    T.forward(size//3)
    T.right(45)
    T.forward(size//6)
    T.end_fill()

    # Neck
    T.pencolor("black")
    T.setheading(90)
    T.forward(size//3)

    # Head
    T.penup()
    T.forward(size//3)
    T.right(90)
    T.forward(size//3)
    T.left(90)
    T.fillcolor("#FFD3AC")
    T.begin_fill()
    T.circle(size//3)
    T.end_fill()

    # Eyes
    T.penup()
    T.left(90)
    T.forward(size//4)
    T.right(90)
    T.forward(size//15)
    T.pendown()
    T.dot(size//15)
    T.penup()
    T.left(90)
    T.forward(size//7)
    T.pendown()
    T.dot(size//15)
    T.penup()

    # Smile/Mouth
    T.backward(size//7)
    T.right(90)
    T.backward(size//7)
    T.setheading(180)
    T.forward(size//5)
    T.setheading(90)
    T.backward(size//10)
    T.fillcolor("#FFD3AC")
    T.begin_fill()
    T.color("black")
    T.setheading(-60)
    T.circle(size//6, 120)
    T.end_fill()

    # Clothing
    if gender == "female":  
        # Draw skirt
        T.penup()
        T.goto(x + size*2.5//3, y + size*1.5//3)
        T.setheading(90)
        T.color("pink")
        T.fillcolor("pink")
        T.pendown()
        T.begin_fill()
        T.left(30)
        T.forward(size*2//3)
        T.left(60)
        T.forward(size//3)
        T.left(60)
        T.forward(size*2//3)
        T.left(120)
        T.forward(size)
        T.end_fill()
    elif gender == "male":
        # Draw blue jeans
        T.penup()
        T.goto(x + size//6, y + size*1.5//3)
        T.color("blue")
        T.fillcolor("blue")
        T.setheading(30)
        T.pendown()
        T.begin_fill()
        for i in range(2):
            T.forward(size//3)
            T.right(90)
            T.forward(size*2//3)
            T.right(90)
        T.end_fill()
        T.penup()
        T.goto(x + size*3//6, y + size*1.5//3)
        T.color("blue")
        T.fillcolor("blue")
        T.setheading(150)
        T.pendown()
        T.begin_fill()
        for i in range(2):
            T.forward(size//3)
            T.left(90)
            T.forward(size*2//3)
            T.left(90)
        T.end_fill()
        
def draw_tree(T, x, y, start_len):
    """
    Parameters:  
    T (turtle.Turtle): Turtle object
    x (float): Starting x-coordinate of the tree
    y (float): Starting y-coordinate of the tree
    start_len (int): Initial length of the tree's trunk

    Draws a tree (with bottom-right of trunk being (x,y)) using recursion to draw branches randomly.
    """

    T.penup()
    T.goto(x, y)
    T.pendown()
    T.setheading(90)
    T.color("brown")
    T.pensize(5)

    def draw_branch(len):    # A recursive function
        if len > 5:
            T.color("brown")
            T.forward(len)     # Main trunk
            T.right(25)
            draw_branch(len - random.randint(4, 10))
            T.left(50)
            draw_branch(len - random.randint(4, 10))
            T.right(25)
            T.color("brown")
            T.backward(len)
        else:
            # Leaves
            T.color("green", "green")
            T.begin_fill()
            T.circle(10 + random.randint(0, 5))
            T.end_fill()

    draw_branch(start_len)

def draw_cloud(T, x, y, size):
    """
    Parameters:
        T: Turtle object
        x: X-coordinate of the cloud's center
        y: Y-coordinate of the cloud's center
        size: Base length of the cloud 

    Draws a cloud with a base at coordinates (x,y) with a specified size.
    """
    T.penup()
    T.goto(x, y)
    T.speed(0)

    T.fillcolor("#D5FBFC") 
    T.pencolor("#D5FBFC")
    T.begin_fill()
    T.setheading(0)
    T.forward(size)      # Flat base
    T.circle(size*7//27, 180)  #Rightmost bump
    T.right(160)
    T.circle(size*6//27, 180)  #Lefter & Higher bump
    T.right(110)
    T.circle(size*9//27, 180)  #Top bump
    T.right(122)
    T.circle(size*6//27, 180)  #Lefter & Lower bump
    T.right(150)
    T.circle(size*75//270, 180)  #Leftmost bump
    T.forward(size*24//270)
    T.end_fill()

def draw_xy_axis(T, scrn):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    scrn (turtle.Screen): Turtle screen object
    
    This function draws the x and y axis lines for object centering.
    A completely optional function and mainly just for organizing/testing the scene.
    '''
    T.penup()
    T.pensize(1)

    if day_or_night.lower() == "d":
        T.pencolor("black")
    else:
        T.pencolor("white")

    T.speed(100)
    T.goto(0, scrn.window_height()//2)  
    T.setheading(270)
    T.pendown()
    T.forward(scrn.window_height())   # Y-axis line
    T.penup()
    T.goto(-scrn.window_width()//2, 0)
    T.setheading(0)
    T.pendown()
    T.forward(scrn.window_width())     # X-axis line
    T.penup()

def draw_sun(T, scrn, num_rays, ray_length, ray_width):
    '''
    Parameters:
    T: Turtle object
    scrn (turtle.Screen): Turtle screen object
    num_rays (int): The number of sunrays should have (ideally 12)
    ray_length (int): The length of the ray (ideally 50)
    ray_width (int): The width of the ray (ideally 20)
    
    This function draws a basic sun in the corner of the screen with sunray lines.
    '''

    # Sun
    T.penup()
    T.goto(-scrn.window_width()//2 + 80, scrn.window_height()//2)
    T.setheading(90)
    T.fillcolor("#F8EB71")
    T.begin_fill()
    T.circle(80)
    T.end_fill()

    # Sunrays
    for i in range(0, num_rays + 1):
        T.penup()
        T.goto(-scrn.window_width()//2 + 15, scrn.window_height()//2 - 15) 
        T.setheading(270 + (90 / num_rays) * i)      # Ray Angle
        T.forward(80)  

        # Sunray rectangle
        T.pendown()
        T.begin_fill()
        T.forward(ray_length)  
        T.right(90) 
        T.forward(ray_width)
        T.right(90)
        T.forward(ray_length)
        T.right(90)
        T.forward(ray_width)
        T.end_fill()

def draw_road_sidewalk_grass(T, scrn):
    '''
    Parameters:
    T (turtle.Turtle): Turtle object
    scrn (turtle.Screen): Turtle screen object
    
    This function draws the road, the sidewalk, and the grass.
    It returns the top y-coordinate of the grass rectangle which is used by almost all other objects in the scene for positioning.
    '''

    # Road
    T.penup()
    ground_y = -scrn.window_height()//2 + 100
    T.goto(-scrn.window_width()//2, ground_y)  
    T.pendown()
    T.color("#556975")  
    T.begin_fill()
    T.setheading(0)
    T.forward(scrn.window_width())
    T.right(90)
    T.forward(100)
    T.right(90)
    T.forward(scrn.window_width())
    T.right(90)
    T.forward(100)
    T.end_fill()

    # Sidewalk
    T.penup()
    sidewalk_y = ground_y + 8
    T.goto(-scrn.window_width()//2, sidewalk_y)
    T.pendown()
    T.color("#9DA8AC")
    T.begin_fill()
    T.setheading(0)
    T.forward(scrn.window_width())
    T.right(90)
    T.forward(8)  
    T.right(90)
    T.forward(scrn.window_width())
    T.right(90)
    T.forward(8)
    T.end_fill()

    # Grass
    grass_y = sidewalk_y + 4  
    T.penup()
    T.goto(-scrn.window_width()//2, grass_y)
    T.pendown()
    T.color("#498F43")  
    T.begin_fill()
    T.setheading(0)
    T.forward(scrn.window_width())
    T.right(90)
    T.forward(4)  
    T.right(90)
    T.forward(scrn.window_width())
    T.right(90)
    T.forward(4)
    T.end_fill()

    # Draw the white rectangles in the middle of the road
    T.penup()
    T.color("white")
    T.shape("square")
    T.shapesize(stretch_wid=0.5, stretch_len=4)  

    road_center_y = ground_y - 50
    rect_width = 80
    space_between = 60
    start_x = -scrn.window_width()//2 + rect_width//2

    x = start_x
    while x < scrn.window_width()//2:
        T.goto(x, road_center_y)
        T.setheading(0)
        T.stamp()
        x += rect_width + space_between
    
    return grass_y

def draw_fence(T, x, y, size, color):
    """
    Parameters:
    T (turtle.Turtle): Turtle object
    x (float): X-coordinate of the fence's bottom left corner
    y (float): Y-coordinate of the fence's bottom left corner
    size (integer): Hieght of the fence
    color (string): color of the fence

    Draws a simple fence at coordinates (x,y) with a specified size.
    """
    T.penup()
    T.goto(x, y)
    T.pencolor("black")
    T.pensize(1)
    T.setheading(90)
    T.pendown()

    # Simple Fence (long rectangle with triangualr tip)
    T.fillcolor(color)
    T.begin_fill()
    T.forward(3*size//4)
    T.right(45)
    T.forward((2*0.5)*size//4)   # Using 45-45-90 triangle
    T.right(90)
    T.forward((2*0.5)*size//4)   # Using 45-45-90 triangle
    T.right(45)
    T.forward(3*size//4)
    T.end_fill()

def draw_animated_clouds_snowflakes(scrn):
    '''
    Parameters:
    scrn (turtle.Screen): Turtle screen object
    
    This function animates multiple clouds movement across screen's sky and animates snowflakes falling.
    '''

    global clouds_on, snowflake_on

    # User Input for clouds and snowflakes
    clouds_on = input("\nDo you want to display clouds? (Y/N): ")

    if clouds_on.lower() == "y":
        clouds_on = True
    elif clouds_on.lower() == "n":
        clouds_on = False

    snowflake_on = input("\nDo you want to display snowfall? (Y/N): ")

    if snowflake_on.lower() == "y":
        snowflake_on = True
    elif snowflake_on.lower() == "n":
        snowflake_on = False

    # Draw initial clouds
    if clouds_on:
        clouds = []
        for _ in range(8):
            cloud_turtle = turtle.Turtle()
            cloud_turtle.penup()
            cloud_turtle.hideturtle()
            x = random.randint(-200, 200)
            y = random.randint(80, 230)
            size = random.randint(40, 50)
            direction = random.choice([-1, 1])  
            speed = random.uniform(0.5, 2) 
            draw_cloud(cloud_turtle, x, y, size)
            clouds.append({"turtle": cloud_turtle, "x": x, "y": y, "size": size, "direction": direction, "speed": speed})

        # Draw initial snowflakes
        if snowflake_on:
            # This is my own version of animating the snowflakes. 
            # It is under clouds_on because they are compatible unlike Aryan Grover's snowfall function.
            snowflake_turtle = turtle.Turtle()
            snowflake_turtle.hideturtle()
            snowflake_turtle.speed(0)
            snowflakes = []
            snowflake_count = 20
            new_snowflake_rate = 2

            for _ in range(snowflake_count):
                x = random.randint(-scrn.window_width()//2, scrn.window_width()//2)
                y = random.randint(0, scrn.window_height()//2)
                size = random.randint(5, 6)
                speed = random.randint(2, 7)
                snowflakes.append([x, y, size, speed])

    def animate():
        # Move the clouds in their direction by a little bit
        if clouds_on:
            for cloud in clouds:
                cloud_turtle = cloud["turtle"]
                cloud["x"] += cloud["direction"] * cloud["speed"]
                if cloud["x"] > 300 or cloud["x"] < -300:      #If the clouds touches the edges of the screen, then make it restart from opposite end
                    cloud["x"] = -300 if cloud["direction"] == 1 else 300
                cloud_turtle.clear()
                draw_cloud(cloud_turtle, cloud["x"], cloud["y"], cloud["size"])

        if snowflake_on:
            if clouds_on:     # If both are on, then we need to use my snowfall version rather than Aryan's
                # This is my version of the snowfall and it is compatible with my aniamted clouds
                snowflake_turtle.clear()
                for snowflake in snowflakes:
                    x, y, size, speed = snowflake
                    draw_snow_flake(snowflake_turtle, x, y, size, 1)       # Thickness is 1 because these snowflakes are small and should be thin
                    snowflake[1] -= snowflake[3]
                    if snowflake[1] < -scrn.window_height()//2:     #If the snowflake reaches the bottom of the screen, then make it restart from the top
                        snowflake[1] = scrn.window_height()//2

                if random.randint(1, 1000) % 3 == 0:       # Making it less probable for new_snoflakes to appear (as more snowflakes = more laggy)
                    for _ in range(new_snowflake_rate):
                        x = random.randint(-scrn.window_width()//2, scrn.window_width()//2)
                        y = scrn.window_height()//2
                        size = random.randint(5, 6)
                        speed = random.randint(2, 7)
                        snowflakes.append([x, y, size, speed])
            else:
                # This is Aryan Grover's snowfall function, which is less laggy. 
                # However, it is not compatible with my animated clodus, so it is in this section.
                snowfall_animation()

        screen.update()
        screen.ontimer(animate, 100)

    animate()


# Aaron Sethi's function:
def building_4(T, x, y, color, size):
    '''
    This function makes the fourth building of my image with unique windows.
    Input: T (turtle object), x, y (position coordinates of the building), color, size (scaling factor for measurements)
    Output: A large building with unique windows with the size parameter to scale the building.
    '''
    #Structure of the building
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.setheading(90)
    T.begin_fill()
    T.fillcolor(color)
    T.forward(400 * size)  
    T.right(90)
    T.forward(100 * size)
    T.right(90)
    T.forward(400 * size)
    T.right(90)
    T.forward(100 * size)
    T.end_fill()
    T.begin_fill()
    T.fillcolor(color)
    T.forward(50 * size)
    T.right(90)
    T.forward(150 * size)
    T.right(90)
    T.forward(50 * size)
    T.right(90)
    T.forward(150 * size)
    T.end_fill()
    T.left(90)
    T.forward(100 * size)
    T.begin_fill()
    T.fillcolor(color)
    T.forward(50 * size)
    T.left(90)
    T.forward(200 * size)
    T.left(90)
    T.forward(50 * size)
    T.left(90)
    T.forward(200 * size)
    T.end_fill()
    T.right(180)
    T.forward(200 * size)
    T.begin_fill()
    T.fillcolor("#efd84a")
    T.forward(7 * size)
    T.right(90)
    T.forward(57 * size)
    T.right(90)
    T.forward(7 * size)
    T.right(90)
    T.forward(57 * size)
    T.end_fill()
    T.penup()
    T.right(90)
    T.forward(7 * size)
    T.begin_fill()
    T.fillcolor("#172e68")
    T.forward(42 * size)
    T.right(135)
    T.forward(60 * size)
    T.right(135)
    T.forward(50 * size)
    T.end_fill()
    T.penup()
    T.left(90)
    T.forward(200 * size)
    T.right(90)
    T.forward(93 * size)
    T.right(90)
    T.forward(143 * size)
    T.pendown()
    T.begin_fill()
    T.fillcolor("#efd84a")
    T.forward(7 * size)
    T.left(90)
    T.forward(57 * size)
    T.left(90)
    T.forward(7 * size)
    T.left(90)
    T.forward(57 * size)
    T.end_fill()
    T.left(90)
    T.forward(7 * size)
    T.begin_fill()
    T.fillcolor("#172e68")
    T.forward(43 * size)
    T.left(135)
    T.forward(60 * size)
    T.left(135)
    T.forward(43 * size)
    T.end_fill()
    T.penup()
    T.left(90)
    T.forward(243 * size)
    T.pendown()
    T.begin_fill()
    T.fillcolor("#efd84a")
    T.left(90)
    T.forward(7 * size)
    T.right(90)
    T.forward(7 * size)
    T.right(90)
    T.forward(114 * size)
    T.right(90)
    T.forward(7 * size)
    T.right(90)
    T.forward(107 * size)
    T.end_fill()
    T.penup()
    T.right(90)
    T.forward(7 * size)
    T.right(90)
    T.forward(12 * size)
    T.left(90)
    T.right(45)
    T.begin_fill()
    T.fillcolor("#172e68")
    T.forward(35 * size)
    T.right(45)
    T.forward(29 * size)
    T.right(45)
    T.forward(35 * size)
    T.right(135)
    T.forward(70 * size)
    T.right(45)
    T.end_fill()

    # Windows grid:
    for col in range(1):
        for row in range(18):
            x = -259  + col * 20 * size
            y = -370 + row * 20 * size
            T.penup()
            T.goto(x, y)
            T.pendown()
            T.begin_fill()
            T.fillcolor("#eeee80")
            T.setheading(90)
            T.right(75)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.end_fill()
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.begin_fill()
            T.fillcolor("#3095ee")
            T.right(120)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.right(90)
            T.forward(18.5 * size)
            T.right(90)
            T.forward(5 * size)
            T.end_fill()
            T.right(90)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.left(90)
            T.begin_fill()
            T.fillcolor("#eeee80")
            T.right(-25)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.end_fill()
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.right(90)
            T.begin_fill()
            T.fillcolor("#3095ee")
            T.right(20)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.right(90)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.end_fill()
            T.right(90)
            T.forward(20 * size)
            T.left(90)
            T.right(70)
            T.begin_fill()
            T.fillcolor("#eeee80")
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.right(90)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.end_fill()

    for col in range(1):
        for row in range(6):
            x = -304 + col * 20 * size
            y = -370 + row * 20 * size
            T.penup()
            T.goto(x, y)
            T.pendown()
            T.begin_fill()
            T.fillcolor("#eeee80")
            T.setheading(90)
            T.right(75)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.end_fill()
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.begin_fill()
            T.fillcolor("#3095ee")
            T.right(120)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.right(90)
            T.forward(18.5 * size)
            T.right(90)
            T.forward(5 * size)
            T.end_fill()

    for col in range(1):
        for row in range(8):
            x = -154  + col * 20 * size
            y = -370  + row * 20 * size
            T.penup()
            T.goto(x, y)
            T.pendown()
            T.begin_fill()
            T.fillcolor("#eeee80")
            T.setheading(90)
            T.right(75)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.end_fill()
            T.left(90)
            T.forward(20 * size)
            T.left(90)
            T.forward(5 * size)
            T.begin_fill()
            T.fillcolor("#3095ee")
            T.right(120)
            T.forward(20 * size)
            T.right(90)
            T.forward(5 * size)
            T.right(90)
            T.forward(18.5 * size)
            T.right(90)
            T.forward(5 * size)
            T.end_fill()


# Swanish Baweja's Pizza Building Functions
def pizza_shop(S,x,y,size,floors):
    """
    This script uses Python Turtle to draw a simple representation
    of a pizza shop building. It includes the main structure, a door, and a window
    to make a basic pizza shop storefront.

    S (turtle.Turtle): The turtle object used for drawing.
    x (float): Starting x-coordinate of the bottom right corner of the building.
    y (float): Starting y-coordinate of the bottom right corner of the building.
    size (float): The size of the base (which affects the rest of the building too).
    floors (int): The number of floors in the building.
    """

    # Red base at the bottom
    S.setheading(0)
    S.goto(x,y)
    S.right(180)
    S.fillcolor("#9f260c") # Filling it to be maroon
    S.pendown()
    S.begin_fill()
    
    # Loop to draw the small red base
    for i in range(2):  # Two long sides and two short sides
        S.forward(size)
        S.right(90)
        S.forward(size / 37.5)
        S.right(90)
        
    S.left(90)
    S.end_fill()
   
    # First floor
    S.penup()
    S.fillcolor("#eadaa4")
    S.right(180)
    S.forward(size/37.5)
    S.left(90)
    S.forward(size/10)
    S.pendown()
    S.begin_fill()
    
    # Loop to draw the first floor
    for _ in range(2):  
        S.forward(size - 2 * (size / 10))  # Long side
        S.right(90)
        S.forward(size / (150 / 70))  # Short side
        S.right(90)

    S.end_fill()
    S.penup()
    
    # moving to the next location
    S.forward((size/3)*2)
   
    # The Door
    S.fillcolor("green")
    S.begin_fill()
    S.pendown()
    
    # drawing the door part
    S.right(90)
    S.forward(size/(150/35))
    S.right(90)
    S.forward(size/6)
    S.right(90)
    S.forward(size/(150/35))
    S.end_fill()
    S.penup()
    
    # moving to the next location
    S.right(180)
    S.forward(size/15)
    S.left(90)
    S.forward(size/20)
    S.pendown()
   
    # Window in the door
    S.fillcolor("white")
    S.begin_fill()
    
    # drawing the door part
    for _ in range(2):
        S.forward(size / 12)  # Short side
        S.right(90)
        S.forward(size / 7.5)  # Long side
        S.right(90)
        
    S.left(90)
    S.end_fill()
    S.penup()
    
    # trying to go back to the original point
    S.left(90)
    S.forward(size/20 + ((size/3)*2-(size/6)))
    S.left(90)
    S.forward(size/(150/70)-(size/7.5-size/15))
    S.left(90)
    S.forward(size-2*(size/10))
    S.left(90)
    S.right(180)
    
    # saving exact coordinates to go back to later
    initial_x = S.xcor()
    initial_y = S.ycor()
   
    # moving back
    S.right(90)
    S.forward(size/2)
    S.right(90)
    S.forward(size/(150/35))
   
    # Window part on the right side of the first floor
    S.pendown()
    S.fillcolor("white")
    S.begin_fill()
    
    # Rectangle-drawing section with a loop
    for _ in range(2):  # Looping for the two pairs of sides
        S.forward(size / 7.5)  # Short side
        S.left(90)
        S.forward(size / 4)  # Long side
        S.left(90)
        
    S.right(90)
    S.end_fill()
    
   
    # Window cill of the window on the first floor
    S.fillcolor("green")
    S.penup()
    S.left(90)
    S.forward(size/7.5)
    S.right(90)
   
    S.begin_fill()
    S.pendown()
    S.forward(size/17)
    S.left(90)
    S.forward(size/50)
    S.left(90)
    S.forward(size/4+(2*(size/17)))
    S.left(90)
    S.forward(size/50)
    S.left(90)
    S.forward(size/4+size/17)
    S.end_fill()
    S.penup()
    S.right(90)
    
    # going back to the corner so the alignment is perfect
    S.goto(initial_x,initial_y)

    # Beige color
    S.fillcolor("#eadaa4")
    S.begin_fill()

    # Resetting variable
    counter_floors = 0

    # While loop to create the floors. It keeps on creating floors and keeps count until the specificed number of floors has been made
    while counter_floors < floors:
       
        # Base beige part
        S.begin_fill()
        S.pendown()
        S.forward(size/3)
        S.right(90)
        S.forward(size-2*(size/10))
        S.right(90)
        S.forward(size/3)
        S.penup()
        S.end_fill()
       
        # Moving
        S.right(90)
        S.forward((size-2*(size/10))/2)
        S.right(90)
        S.forward(size/25)
       
        # window cill
        S.fillcolor("green")
        S.begin_fill()
        S.pendown()
        S.left(90)
        S.forward((size-2*(size/10))/4)
        S.right(90)
        S.forward(size/50)
        S.right(90)
        S.forward((size-2*(size/10))/2)
        S.right(90)
        S.forward(size/50)
        S.right(90)
        S.forward((size-2*(size/10))/4)
        S.end_fill()
       
        # white part of the window on the first floor
        S.penup()
        S.right(90)
        S.forward(size/50)
        S.fillcolor("white")
        S.forward(size/(150/23))
        S.begin_fill()
        S.pendown()
        S.right(90)
        S.forward(size/6)
        S.right(90)
        S.forward(size/(150/23))
        S.right(90)
        S.forward(2*(size/6))
        S.right(90)
        S.forward(size/(150/23))
        S.right(90)
        S.forward(size/6)
        S.end_fill()
        
        # going back to the original point
        S.penup()
        S.right(90)
        S.forward(size/(150/23))
        S.right(90)
        S.forward((size-2*(size/10))/2)
        S.right(90)
        S.forward(size/(150/41))
        S.end_fill()
        
    
    # begin the fill for the next floors
        S.fillcolor("#eadaa4")
        S.begin_fill()
       
        # increase counter by 1
        counter_floors += 1

    # end
    S.penup()
    S.end_fill()

    # set heading to 0 to prevent mismatch
    S.setheading(0)

    # resetting variables
    x-= (size * 14/150)
    y+= (size/(150/63))
    radius = (size/30)
    counter = 0
    repeated = 0
    S.setheading(0)

    # creating the pattern of the red circle squares based on the number of floors
    while repeated < (floors+1):
       
        # getting how many can fit perfectly based on the size
        while counter <= ((size-2*(size/10))/(radius*2)):
                # using a counter and creating one by one
                circle_square(S,x,y,radius)
                x-=(radius*2)
                counter+=1

        S.penup()
       
        # increasing variables
        x+=(radius*2 + (size-2*(size/10)))
        y+=(size/3)
        repeated +=1
        counter = 0
       
def circle_square(S,x,y,radius):
    """
    This function draws the small, red, circle square pattern for the pizza building. It is purely cosmetic.
     
    S (turtle.Turtle): The turtle object used for drawing.
    x (float): The x-coordinate of the circle's center
    y (float): The y-coordinate of the circle's center.
    radius (float): The radius of the circle.
    """
    
    # start at the specified x,y 
    S.goto(x,y)
    S.fillcolor("red")
   
    # start making the circle
    S.begin_fill()
    S.pendown()
    S.circle(radius)
    S.end_fill()
    S.penup()
   
    # movement to align the square properly
    S.right(180)
    S.forward(radius)
    S.right(90)
    S.forward(radius)
   
    # making a square with a side length double the radius
    S.begin_fill()
    S.pendown()
    S.forward(radius*2)
    S.right(90)
    S.forward(radius*2)
    S.right(90)
    S.forward(radius*2)
    S.right(90)
    S.forward(radius*2)
    S.right(90)
    S.end_fill()
   
    # resetting the position
    S.setheading(0)

def pizza_build(S, x, y):
    """
    This script uses Python Turtle to draw a simple representation
    of a pizza. It includes the the sauce, the crust, and the toppings (pepperoni and mushrooms).

    S (turtle.Turtle): The turtle object used for drawing.
    x (float): Starting x-coordinate of the center of the pizza.
    y (float): Starting y-coordinate of the center of the pizza.
   
    """
    S.setheading(0)
    # define subfunction
    def pizza(x, y, radius, color):
        """
        This part of the function actually draws the pizza
       
         
        x (float): The x-coordinate of the pizza's center
        y (float): The y-coordinate of the pizza's center.
        radius (float): The radius of the circle for the pizza.
        color (str): The color of the pizza.
        """
       
        # drawing the actual circle based on the parameters
        S.pensize(0)
        S.penup()
        S.goto(x, y - radius)
        S.pendown()
        S.fillcolor(color)
        S.begin_fill()
        S.circle(radius)
        S.end_fill()

    # Draw the crust
    pizza(x, y, 30, "burlywood")

    # Draw the sauce
    pizza(x, y, 27, "tomato")

    # Draw the cheese
    pizza(x, y, 24, "gold")

    # Add pepperoni
    S.color("firebrick")
   
    # Defining the positions in a list
    pepperoni_positions = [(x - 10, y + 5), (x + 7, y - 4), (x +3, y + 4), (x + 17, y + 3), (x + 9, y - 8), (x - 2, y - 5)]
    for pos in pepperoni_positions: # putting the pepperoni on the pizza
        pizza(pos[0], pos[1], 2, "firebrick")

    # Add mushroom slices
    S.color("wheat")
   
    # Defining the positions in a list
    mushroom_positions = [(x + 12, y + 2), (x - 12, y - 12), (x + 13, y), (x - 16, y + 12), (x, y - 18)]
    for pos in mushroom_positions: # putting the pepperoni on the pizza
        pizza(pos[0], pos[1], 2, "wheat")
       
    S.penup()


# Aryan's Snowfalling functions:
def create_snowflake():
    """
    Creates a snowflake with random properties and returns its configuration.

    The snowflake is a dictionary containing the following attributes:
    - 'turtle': The Turtle object representing the snowflake.
    - 'size': The size of the snowflake (randomized between 0.2 and 0.8).
    - 'fall_speed': The speed at which the snowflake falls (randomized between 2 and 6).

    Parameters:
    None

    Returns:
    dict: A dictionary representing the snowflake's properties.
    """
    snowflake = turtle.Turtle()
    snowflake.shape("circle")
    snowflake.color("white")
    snowflake.penup()
    snowflake.speed(0)
    size = random.uniform(0.2, 0.8)  # Random size
    snowflake.shapesize(stretch_wid=size, stretch_len=size)
    snowflake.goto(random.randint(-400, 400), random.randint(200, 600))
    fall_speed = random.uniform(2, 6)  # Random fall speed
    return {
        "turtle": snowflake,
        "size": size,
        "fall_speed": fall_speed,
    }

def move_snowflake(snowflake):
    """
    Moves a snowflake downward on the screen and resets its position when it goes off-screen.

    The snowflake's vertical position is decremented based on its fall speed. If the snowflake
    moves below the screen, it is repositioned to a random location at the top, with a new random
    size.

    Parameters:
    snowflake (dict): A dictionary containing:
        - 'turtle': The Turtle object representing the snowflake.
        - 'size': The size of the snowflake.
        - 'fall_speed': The speed at which the snowflake falls.

    Returns:
    None
    """
    snowflake["turtle"].sety(snowflake["turtle"].ycor() - snowflake["fall_speed"])
    if snowflake["turtle"].ycor() < -300:
        snowflake["turtle"].goto(random.randint(-400, 400), random.randint(200, 600))
        snowflake["size"] = random.uniform(0.2, 0.8)
        snowflake["turtle"].shapesize(stretch_wid=snowflake["size"], stretch_len=snowflake["size"])

def snowfall_animation():
    """
    Sets up the screen and animates snowfall using Turtle graphics.

    This function initializes a screen with a black background, creates multiple snowflakes
    with varying sizes and falling speeds, and continuously animates them falling. When a
    snowflake moves off-screen, it resets its position to the top with a new random size.

    Parameters:
    None

    Returns:
    None
    """
    # Set up the screen
    #screen = turtle.Screen()
    #screen.bgcolor("black")
    #screen.title("Snowfall Animation")
    #screen.setup(width=800, height=600)
    #screen.tracer(0)  # Disable auto-updates for smooth animation

    # Create snowflakes
    snowflakes = [create_snowflake() for _ in range(50)]  # Generate 50 snowflakes

    # Animation loop
    while True:
        for snowflake in snowflakes:
            move_snowflake(snowflake)
        screen.update()  # Update the screen
        time.sleep(0.02)  # Pause for smooth animation

    screen.mainloop()


# Amol's Moon Function:
def draw_moon(T, x, y, size, num_of_craters, crescent, crescent_color, ring_color, rocket_pos_ratio, debris_count, debris_color="white"):
    """
    Draws a moon with optional craters, a crescent overlay, and a tiny rocket.

    Parameters:
    T (turtle.Turtle): The turtle object used for drawing.
    x (float): The x-coordinate of the moon's center.
    y (float): The y-coordinate of the moon's center.
    size (float): The radius of the moon.
    num_of_craters (int): The number of craters to draw on the moon.
    crescent (float): A value between 0 and 1 indicating the crescent's size (0 for no crescent, 1 for full crescent).
    crescent_color (str): The color of the crescent.
    rocket_pos_ratio (float): A value between 0 and 1 representing the vertical pos of the rocket as a ratio of the moon's radius (size) above the moon surface.
    debris_count (int): The positive number of debris to draw around the moon.
    debris_color (str): The color of the debris drawn around the moon.
    """
    T.hideturtle()
    T.speed(0)
    T.penup()

    # Draw the moon
    T.goto(x, y - size)
    T.color("light yellow")
    T.fillcolor("light yellow")
    T.begin_fill()
    T.circle(size)
    T.end_fill()

    # Draw craters on the moon
    T.color("light goldenrod")
    for i in range(num_of_craters):
        r = 0.7 * size * math.sqrt(random.random())
        theta = random.random() * 2 * math.pi
        crater_x = x + r * math.cos(theta)
        crater_y = y + r * math.sin(theta)
        crater_size = size * random.uniform(0.05, 0.15)
        T.goto(crater_x, crater_y - crater_size)
        T.begin_fill()
        T.circle(crater_size)
        T.end_fill()

    # Draw a line at a random angle (moon ring)
    T.penup()
    T.goto(x, y)
    T.setheading(random.uniform(0, 360))  #Random angle
    T.pendown()
    T.color(ring_color)
    T.forward(size*1.5)
    T.backward(size * 3)
    T.setheading(0)

    # Draw crescent
    if crescent != 1:
        coefficient = -1 if crescent > 0.5 else 0
        T.penup()
        T.goto(x + size * 2 * (crescent + coefficient), y - size)
        T.color(crescent_color)
        T.fillcolor(crescent_color)
        T.begin_fill()
        T.circle(size)
        T.end_fill()

    # Draw a tiny rocket sitting on the moon's border
    rocket_height = size * 0.45
    rocket_width = size * 0.2
    flame_height = rocket_height * 0.2

    T.penup()
    T.goto(x, y + size + size * rocket_pos_ratio)
    T.pendown()

    # Rocket body (rectangle)
    T.color("white")
    T.fillcolor("gray")
    T.begin_fill()
    for i in range(2):
        T.forward(rocket_width)
        T.left(90)
        T.forward(rocket_height)
        T.left(90)
    T.end_fill()

    # Rocket nose
    T.fillcolor("red")
    T.begin_fill()
    T.goto(x, y + size + rocket_height + size * rocket_pos_ratio)
    T.goto(x + rocket_width / 2, y + size + rocket_height + rocket_width / 2 + size * rocket_pos_ratio)
    T.goto(x + rocket_width, y + size + rocket_height + size * rocket_pos_ratio)
    T.goto(x, y + size + size * rocket_pos_ratio)
    T.end_fill()

    # Rocket window (circle)
    T.penup()
    T.goto(x + rocket_width / 2, y + size + rocket_height / 1.6 + size * rocket_pos_ratio)
    T.pendown()
    T.fillcolor("blue")
    T.begin_fill()
    T.circle(rocket_width / 3)
    T.end_fill()

    # Rocket fire (tiny overlapping triangles)
    T.penup()
    T.goto(x, y + size)
    T.color("black")
    T.pendown()
    for i in range(4):
        T.fillcolor("red" if i % 2 == 0 else "orange")
        T.begin_fill()
        T.goto(x + rocket_width / 2, y + size - (i + 1) * flame_height + size * rocket_pos_ratio)
        T.goto(x - rocket_width / 4, y + size - i * flame_height + size * rocket_pos_ratio)
        T.goto(x + rocket_width + rocket_width / 4, y + size - i * flame_height + size * rocket_pos_ratio)
        T.goto(x + rocket_width / 2, y + size - (i + 1) * flame_height + size * rocket_pos_ratio)
        T.end_fill()

    # Draw space debris within radius around moon
    draw_space_debris(T, x, y, size * 2, debris_count, debris_color)

def draw_space_debris(T, x, y, radius, count, color):
    """
    Draws random space debris around the moon within a given radius.

    Parameters:
    T (turtle.Turtle): The turtle object used for drawing.
    x (float): The x-coordinate of the moon's center.
    y (float): The y-coordinate of the moon's center.
    radius (float): The radius within which debris will be scattered.
    count (int): The number of debris objects to draw.
    color (str): The color of the debris.
    """
    T.penup()
    T.color(color)
    for i in range(count):
        r = random.uniform(0, radius)
        theta = random.uniform(0, 2 * math.pi)
        debris_x = x + r * math.cos(theta)
        debris_y = y + r * math.sin(theta)

        debris_type = random.choice(["circle", "line", "rectangle", "spiral", "triangle", "circle"])
       
        if debris_type == "circle":
            T.goto(debris_x, debris_y)
            T.dot(random.randint(2, 5), color)
        elif debris_type == "line":
            T.goto(debris_x, debris_y)
            T.setheading(random.randint(0, 360))
            T.pendown()
            T.forward(random.randint(5, 10))
            T.penup()
        elif debris_type == "rectangle":
            T.goto(debris_x, debris_y)
            T.setheading(random.randint(0, 360))
            T.pendown()
            for _ in range(2):
                T.forward(random.randint(3, 8))
                T.left(90)
                T.forward(random.randint(1, 5))
                T.left(90)
            T.penup()
        elif debris_type == "triangle":
            T.goto(debris_x, debris_y)
            T.setheading(random.randint(0, 360))
            T.pendown()
            for _ in range(3):
                T.forward(random.randint(5, 15))
                T.left(120)
            T.penup()
        elif debris_type == "spiral":
            T.goto(debris_x, debris_y)
            T.setheading(random.randint(0, 360))
            T.pendown()
            size = random.randint(5, 15)
            for j in range(size):
                T.forward(j * 0.5)
                T.right(20)
            T.penup()


global day_or_night
day_or_night = input("\nDo you want day or night? (D/N) ")
if day_or_night.lower() == "d":
    draw_sun(t, screen, 4, 50, 20)
else:
    screen.bgcolor("#000000")
    draw_moon(t, -250, 190, 55, 6, 0.42, "black", "red", 0.2, 25, "black")    # Amol Sriprasadh's function
grass_y = draw_road_sidewalk_grass(t, screen)   

# Using a while loop to draw a fence acrosss screen width
x = -screen.window_width()//2    
while x < screen.window_width() // 2:
    draw_fence(t, x, grass_y, 40, "#DFD3BF")
    x += 15   # Fence width is just 3/8 of its size/height parameter because we are using 45-45-90 triangles

draw_different_building(t, -200, grass_y, 150, "#837789") 
person_x, person_y, person_size = -150, grass_y - 60, 30
draw_person(t, person_x, person_y, person_size, "female")     
draw_phone(t, person_x + 20, person_y + 25, 2/3 * person_size, "light gray")
draw_tree(t, -screen.window_width()//2 + 10, grass_y, random.randint(40, 50))    
building_4(t, -75, grass_y, "light blue", 0.5)    # Aaron Sethi's function
pizza_build(t, -50, 70)    # Swanish Baweja's Function. The pizza is on top of Aaron Sethi's building_4.
draw_christmas_tree(t, -40, grass_y + 35, 80)    
draw_museum(t, 280, grass_y + 55, 100)     
draw_observatory(t, 140, grass_y, 180, layers=9)     
draw_house(t, -330, grass_y, 180)          
tower_tip_pos = draw_empire_state_building(t, 0, grass_y, 250)    
draw_snow_flake(t, tower_tip_pos[0], tower_tip_pos[1], 50, 5)    # My own complex-looking snowflake function. It is on top of the empire state building as christmas decoration. Thickness is 5 because this snowflake is big and needs to be thick
draw_van(t, -20, grass_y - 70, 150, "#F3AC17")         
#draw_xy_axis(t, screen)   # Just for testing scene organizing. Comment afterwards.
draw_animated_clouds_snowflakes(screen)    # To see Aryan Grover's snowfall function, say "N" to clouds but "Y" to snowfall. If you want both, then my snowfall methodology will activate but it is more laggy

screen.exitonclick()