# Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)

# Constants for eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14


def draw_head(x,y,color):
    c = Circle(HEAD_RADIUS)
    c.set_position(x,y)
    c.set_color(color)
    add(c)

def draw_legs(x,y,color):
    leg = Circle(FOOT_RADIUS)
    leg.set_position(x,y)
    leg.set_color(color)
    add(leg)
    

def draw_eyes(x,y):
    c = Circle(EYE_RADIUS)
    c.set_position(x,y)
    c.set_color(Color.white)
    
    # Pupil
    pl = Circle(PUPIL_RADIUS)
    pl.set_position(x + 8,y)
    pl.set_color(Color.blue)
    
    add(c)
    add(pl)
    
def draw_ghost(center_x,center_y,color):
    
    rect = Rectangle(BODY_WIDTH,BODY_HEIGHT)
    rect.set_position(center_x,center_y)
    rect.set_color(color)
    
    draw_head(center_x + BODY_WIDTH/2,center_y,color)
    
    add(rect)
    draw_eyes(center_x + BODY_WIDTH/3,center_y)
    draw_eyes(center_x + 2 * (BODY_WIDTH/3),center_y)

    draw_legs(center_x + BODY_WIDTH/6,center_y + BODY_HEIGHT,color)
    draw_legs(center_x + 3 * (BODY_WIDTH/6),center_y + BODY_HEIGHT,color)
    draw_legs(center_x + 5 * (BODY_WIDTH/6),center_y + BODY_HEIGHT,color)
    
center_x = get_width()/2
center_y = get_height()/2
draw_ghost(center_x,center_y,Color.red)
draw_ghost(100,100,Color.green)
draw_ghost(40,200,Color.orange)
