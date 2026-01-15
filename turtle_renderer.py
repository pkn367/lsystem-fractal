def draw_lsystem(t, instructions, angle):
    screen = t.getscreen()

    t.clear()
    t.hideturtle()
    t.speed(0)

    # Bigger line size
    step = 10

    # Better starting position
    t.penup()
    t.goto(-350, 0)
    t.setheading(0)
    t.pendown()

    screen.tracer(0)

    stack = []

    for cmd in instructions:
        if cmd == "F":
            t.forward(step)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            stack.append((t.position(), t.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

    screen.update()


