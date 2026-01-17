import turtle

def compute_bounds(instructions, angle, step):
    import math

    x = y = 0
    heading = 90
    stack = []

    min_x = max_x = 0
    min_y = max_y = 0

    for cmd in instructions:
        if cmd == "F":
            rad = math.radians(heading)
            x += step * math.cos(rad)
            y += step * math.sin(rad)
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)

        elif cmd == "+":
            heading += angle
        elif cmd == "-":
            heading -= angle
        elif cmd == "[":
            stack.append((x, y, heading))
        elif cmd == "]":
            x, y, heading = stack.pop()

    return min_x, max_x, min_y, max_y

def draw_lsystem(instructions, angle, step, speed_factor):
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.title("Python Turtle Graphics")
    

    # Compute bounds
    min_x, max_x, min_y, max_y = compute_bounds(instructions, angle, step)

    width = max_x - min_x
    height = max_y - min_y

    # Scale to fit screen
    scale = min(900 / width, 700 / height)
    step *= scale

    # Recompute bounds after scaling
    min_x, max_x, min_y, max_y = compute_bounds(instructions, angle, step)

    # Center drawing
    start_x = -(min_x + max_x) / 2
    start_y = -(min_y + max_y) / 2


    t = turtle.Turtle()
    t.hideturtle()
    t.speed(3)
    t.color("black")
    t.penup()
    t.goto(0, -300)
    t.setheading(90)  # Face upwards
    t.pendown()

    screen.tracer(1,0)  # 🚀 performance boost

    stack = []
    counter = 0
    update_batch = max(50, int(500 / speed_factor))

    for cmd in instructions:
        if cmd == "F":
            t.forward(step)
        elif cmd == "+":
            t.left(angle)
        elif cmd == "-":
            t.right(angle)
        elif cmd == "[":
            stack.append((t.position(), t.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

        counter += 1
        if counter % update_batch == 0:
            screen.update()

    screen.update()
    turtle.done()
