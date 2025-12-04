# This program should draw a stop light

LIGHT_RADIUS = 25
STOPLIGHT_WIDTH = 100
STOPLIGHT_HEIGHT = 250
BUFFER = 75

def draw_circle(y_pos, color):
    x_pos = get_width() / 2
    circ = Circle(LIGHT_RADIUS)
    circ.set_color(color)
    circ.set_position(x_pos, y_pos)
    add(circ)


y_center = get_height() / 2

rect = Rectangle(STOPLIGHT_WIDTH, STOPLIGHT_HEIGHT)
rect.set_color(Color.gray)
rect.set_position(get_width()/4 + 50, get_height()/4)
add(rect)

draw_circle(y_center + BUFFER, Color.red)
draw_circle(y_center, Color.yellow)
draw_circle(y_center - BUFFER, Color.green)


print(get_width())
print(get_height())
