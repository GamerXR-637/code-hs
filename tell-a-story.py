import random

""" 
 Draws the first scene on the canvas and outputs the first
 section of text for the story.
"""
def backg(color):
    bg = Rectangle(get_width(),get_height())
    bg.set_color(color)
    bg.set_position(0,0)
    add(bg)

def draw_scene1():
    bg = Rectangle(600,500)
    bg.set_color(Color.green)
    bg.set_position(-100,400)
    backg(Color.blue)
    add(bg)
    
    print("This is scene 1")

""" 
 Draws the second scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene2():
    bg = Rectangle(600,500)
    bg.set_color(Color.green)
    bg.set_position(-100,400)
    backg("#e79414")
    
    sun = Circle(100)
    sun.set_position(get_width()/2,350)
    sun.set_color(Color.yellow)
    add(sun)
    add(bg)
    
    print("This is scene 2")

""" 
 Draws the third scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene3():
    bg = Rectangle(600,500)
    bg.set_color(Color.green)
    bg.set_position(-100,400)
    backg("#041A40")
    
    moon = Circle(50)
    moon.set_position(get_width()/5,70)
    moon.set_color(Color.white)
    add(moon)
    add(bg)
    print("This is scene 3")

""" 
 Draws the fourth scene on the canvas and outputs the second
 section of text for the story.
"""
def line(x,y,x_1,y_1,color):
    line = Line(x,y,x_1,y_1)
    line.set_color(color)
    add(line)

def square(z,x,y,color):
    squ = Rectangle(z,z)
    squ.set_position(x,y)
    squ.set_color(color)
    add(squ)

def rec(w,h,x,y,color):
    squ = Rectangle(w,h)
    squ.set_position(x,y)
    squ.set_color(color)
    add(squ)

def firefly(x,y,s):
    rec(s * 2,s,x,y,Color.yellow)
    square(s,x,y,Color.black)

def size(s):
    if s < 20:
        return 10
    elif s > 40:
        return 5
    elif s > 20 and s < 40:
        return 15
    else:
        return 8

def loop_fire(size_v):
    s = size(size_v)
    print(s)
    for i in range(size_v + 1):
        x_pos = random.randint(0,get_width() - s*2)
        y_pos = random.randint(0,get_height()-s*2)
        # r = random.randint(1,100)
        # rd = random.randint(1,20)
        # rs = random.randint(1,10)
        firefly(x_pos,y_pos, s)


print(get_height())
print(get_width())

def draw_scene4():
    bg = Rectangle(600,500)
    bg.set_color(Color.green)
    bg.set_position(-100,400)
    backg("#041A40")
    moon = Circle(50)
    moon.set_position(get_width()/5,70)
    moon.set_color(Color.white)
    add(moon)
    moonq = Circle(50)
    moonq.set_position(get_width()/5 + 20,70)
    moonq.set_color("#041A40")
    add(moonq)
    loop_fire(40)
    # rec(170,170,0,0,"#041A40")
    add(bg)
    
    
    print("This is scene 4")

"""
 This is set up code that makes the story advance from
 scene to scene. Feel free to check out this code and
 learn how it works!
 But be careful! If you modify this code the story might
 not work anymore.
"""

scene_counter = 0

# When this function is called the next scene is drawn.

def draw_next_screen(x, y):
    global scene_counter 
    scene_counter += 1

    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    else:
        draw_scene4()

welcome = Text("Click to Begin!")
welcome.set_position(get_width() / 2 - welcome.get_width() / 2, get_height() / 2)
add(welcome)

add_mouse_click_handler(draw_next_screen)
# draw_scene4()
