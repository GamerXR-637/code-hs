def grow_my_circlele(event):
    r = my_circle.get_radius() 
    if event.key == "ArrowRight":
        if my_circle.get_radius() > 390:
            my_circle.set_radius(r)
        else:
            my_circle.set_radius(r + 10)
            print(my_circle.get_radius())

    if event.key == "ArrowLeft":
        if my_circle.get_radius() < 20:
            my_circle.set_radius(r)
        else:
            my_circle.set_radius(r - 10)
            print(my_circle.get_radius())

my_circle = Circle(100)
my_circle.set_color(Color.red)
my_circle.set_position(250, 250)
add(my_circle)

add_key_down_handler(grow_my_circlele)
