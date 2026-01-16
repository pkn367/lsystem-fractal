import turtle
import time


def draw_lsystem(canvas, commands, angle):
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("white")

    # 🔥 ENABLE ANIMATION (delay controls speed)
    screen.tracer(1, 10)  # (steps, delay in ms)

    t = turtle.RawTurtle(screen)
    t.hideturtle()
    t.speed(0)  # fastest turtle speed (still animated due to tracer)

    # Starting position
    t.penup()
    t.goto(-200, -250)
    t.setheading(90)
    t.pendown()

    stack = []
    step = 6

    for cmd in commands:
        if cmd == 'F':
            t.forward(step)

        elif cmd == '+':
            t.right(angle)

        elif cmd == '-':
            t.left(angle)

        elif cmd == '[':
            stack.append((t.position(), t.heading()))

        elif cmd == ']':
            if stack:
                pos, heading = stack.pop()
                t.penup()
                t.goto(pos)
                t.setheading(heading)
                t.pendown()

        # OPTIONAL: tiny delay for extra smoothness
        # time.sleep(0.001)
