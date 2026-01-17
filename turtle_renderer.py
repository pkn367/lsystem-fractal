import turtle

def draw_lsystem(instructions, angle, step, speed_factor):
    screen = turtle.Screen()
    screen.setup(width=900, height=700)
    screen.title("Python Turtle Graphics")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()
    t.goto(0, -300)
    t.setheading(90)  # Face upwards
    t.pendown()

    screen.tracer(0)  # 🚀 performance boost

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
