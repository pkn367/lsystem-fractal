import tkinter as tk
import math
import time
import turtle

screen = turtle.Screen()
screen.tracer(0, 0)   # manual screen updates

t = turtle.Turtle()   # ✅ THIS LINE WAS MISSING
t.hideturtle()
t.penup()
t.goto(0, -250)
t.setheading(90)
t.pendown()

# ---------------- L-SYSTEM LOGIC ---------------- #

def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current


def gradient_color(t):
    r = int(50 + 100 * t)
    g = int(150 + 80 * (1 - t))
    b = int(50 + 150 * t)
    return (r, g, b)


# ---------------- DRAWING ---------------- #

def draw_lsystem(turtle, instructions, angle, step, speed):
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(0)

    turtle.penup()
    turtle.goto(-200, 0)
    turtle.setheading(0)
    turtle.pendown()

    stack = []

    screen.tracer(0, 0)   # FULL SPEED MODE

    for cmd in instructions:
        if cmd in "FG":
            turtle.forward(step)
        elif cmd == "+":
            turtle.right(angle)
        elif cmd == "-":
            turtle.left(angle)
        elif cmd == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            turtle.penup()
            turtle.goto(pos)
            turtle.setheading(heading)
            turtle.pendown()

    screen.update()  # draw everything at once
# Create main window
root = tk.Tk()
root.title("L-System Fractal Architect")

# LEFT: drawing canvas frame
canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# RIGHT: control panel frame  ✅ THIS WAS MISSING
control_frame = tk.Frame(root, width=300)
control_frame.pack(side=tk.RIGHT, fill=tk.Y)

def generate_lsystem(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        new_result = ""
        for char in result:
            new_result += rules.get(char, char)
        result = new_result
    return result

rules_entry = tk.Entry(control_frame, width=25)
rules_entry.insert(0, "F=F+F--F+F")  # default value
rules_entry.pack(pady=5)


# ---------------- GENERATE BUTTON ---------------- #

def generate():
    try:
        axiom = axiom_entry.get()
        rules_text = rules_entry.get()
        angle = float(angle_entry.get())
        iterations = int(iter_entry.get())
        speed = speed_slider.get()

        rules = {}
        for rule in rules_text.split(","):
            key, value = rule.split("=")
            rules[key.strip()] = value.strip()

        instructions = generate_lsystem(axiom, rules, iterations)

        draw_lsystem(
            turtle=t,
            instructions=instructions,
            angle=angle,
            step=5,
            speed=speed
        )

    except Exception as e:
        print("Error:", e)


# ---------------- PRESETS ---------------- #

def load_preset(name):
    presets = {
        "tree": ("F", "F=F[+F]F[-F]F", "25", "4"),
        "koch": ("F--F--F", "F=F+F--F+F", "60", "4"),
        "dragon": ("FX", "X=X+YF+,Y=-FX-Y", "90", "10")
    }

    ax, ru, ang, it = presets[name]
    axiom_entry.delete(0, tk.END)
    rule_entry.delete(0, tk.END)
    angle_entry.delete(0, tk.END)
    iter_entry.delete(0, tk.END)

    axiom_entry.insert(0, ax)
    rule_entry.insert(0, ru)
    angle_entry.insert(0, ang)
    iter_entry.insert(0, it)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1100x650")

canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

control_frame = tk.Frame(root, width=250)
control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

canvas = tk.Canvas(canvas_frame)
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")
screen.colormode(255)

turtle = turtle.RawTurtle(screen)
turtle.hideturtle()
turtle.width(2)

# ---------------- CONTROLS ---------------- #

tk.Label(control_frame, text="Axiom").pack()
axiom_entry = tk.Entry(control_frame)
axiom_entry.pack()

tk.Label(control_frame, text="Rule (comma separated)").pack()
rule_entry = tk.Entry(control_frame)
rule_entry.pack()

tk.Label(control_frame, text="Angle").pack()
angle_entry = tk.Entry(control_frame)
angle_entry.pack()

tk.Label(control_frame, text="Iterations").pack()
iter_entry = tk.Entry(control_frame)
iter_entry.pack()

tk.Button(control_frame, text="Generate", command=generate).pack(pady=10)

tk.Label(control_frame, text="Drawing Speed").pack()
speed_slider = tk.Scale(control_frame, from_=0.001, to=0.05,
                        resolution=0.001, orient=tk.HORIZONTAL)
speed_slider.set(0.01)
speed_slider.pack()

tk.Label(control_frame, text="Presets").pack(pady=10)

tk.Button(control_frame, text="🌿 Tree",
          command=lambda: load_preset("tree")).pack(pady=2)

tk.Button(control_frame, text="❄ Koch Snowflake",
          command=lambda: load_preset("koch")).pack(pady=2)

tk.Button(control_frame, text="🐉 Dragon Curve",
          command=lambda: load_preset("dragon")).pack(pady=2)

# Default preset
load_preset("tree")

root.mainloop()
