import tkinter as tk
from tkinter import ttk
import turtle
import math

# =======================
# Gradient color function
# =======================
def gradient_color(t):
    """
    t should be between 0 and 1
    """
    r = int(40 + 80 * t)
    g = int(120 + 100 * (1 - t))
    b = int(60 + 120 * t)
    return (r, g, b)

# =======================
# L-System expansion
# =======================
def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string
    return current

# =======================
# Draw L-System
# =======================
def draw_lsystem(instructions, angle, step, speed):
    t = turtle.Turtle(visible=False)
    screen = turtle.Screen()

    screen.tracer(1, 0)          # IMPORTANT: enables animation
    screen.colormode(255)

    t.speed(speed)
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    stack = []
    total = len(instructions)

    for i, cmd in enumerate(instructions):
        color = gradient_color(i / total)
        t.pencolor(color)

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

        screen.update()   # visible motion

# =======================
# Generate button handler
# =======================
def generate():
    turtle.clearscreen()

    axiom = axiom_entry.get()
    rule_text = rule_entry.get()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())
    speed = speed_slider.get()

    rules = {}
    if "=" in rule_text:
        left, right = rule_text.split("=")
        rules[left.strip()] = right.strip()

    instructions = expand_lsystem(axiom, rules, iterations)

    draw_lsystem(
        instructions=instructions,
        angle=angle,
        step=5,
        speed=speed
    )

# =======================
# Tkinter UI
# =======================
root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("360x450")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Axiom").pack(anchor="w")
axiom_entry = ttk.Entry(frame)
axiom_entry.insert(0, "F")
axiom_entry.pack(fill="x")

ttk.Label(frame, text="Rule (F=...)").pack(anchor="w", pady=(10, 0))
rule_entry = ttk.Entry(frame)
rule_entry.insert(0, "F=F[+F]F[-F]F")
rule_entry.pack(fill="x")

ttk.Label(frame, text="Angle").pack(anchor="w", pady=(10, 0))
angle_entry = ttk.Entry(frame)
angle_entry.insert(0, "25")
angle_entry.pack(fill="x")

ttk.Label(frame, text="Iterations").pack(anchor="w", pady=(10, 0))
iter_entry = ttk.Entry(frame)
iter_entry.insert(0, "4")
iter_entry.pack(fill="x")

ttk.Label(frame, text="Drawing Speed (1 slow → 10 fast)").pack(anchor="w", pady=(10, 0))
speed_slider = ttk.Scale(frame, from_=1, to=10, orient="horizontal")
speed_slider.set(5)
speed_slider.pack(fill="x")

ttk.Button(frame, text="Generate", command=generate).pack(pady=20)

root.mainloop()
