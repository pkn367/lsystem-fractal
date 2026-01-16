import turtle

def draw_lsystem(t, instructions, angle, step):
    stack = []

    turtle.tracer(0, 0)

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

    turtle.update()


