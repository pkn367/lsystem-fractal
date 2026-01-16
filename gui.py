import tkinter as tk
import turtle

from lsystem_engine import generate_lsystem
from turtle_renderer import draw_lsystem


def run():
    root = tk.Tk()
    root.title("L-System Fractal Architect")

    # Canvas for turtle
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack(side=tk.LEFT)

    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)
    t.speed(0)
    t.hideturtle()

    # Control panel
    panel = tk.Frame(root, padx=10)
    panel.pack(side=tk.RIGHT, fill=tk.Y)

    tk.Label(panel, text="Axiom").pack()
    axiom_entry = tk.Entry(panel)
    axiom_entry.insert(0, "F")
    axiom_entry.pack()

    tk.Label(panel, text="Rules (F=F+F--F+F)").pack()
    rules_entry = tk.Entry(panel)
    rules_entry.insert(0, "F=F+F--F+F")
    rules_entry.pack()

    tk.Label(panel, text="Angle").pack()
    angle_entry = tk.Entry(panel)
    angle_entry.insert(0, "60")
    angle_entry.pack()

    tk.Label(panel, text="Iterations").pack()
    iter_entry = tk.Entry(panel)
    iter_entry.insert(0, "3")
    iter_entry.pack()

    def generate():
        t.clear()
        t.penup()
        t.goto(-300, 0)
        t.setheading(0)
        t.pendown()

        axiom = axiom_entry.get()
        angle = float(angle_entry.get())
        iterations = int(iter_entry.get())

        rules_input = rules_entry.get()
        rules = {}
        for rule in rules_input.split(","):
            k, v = rule.split("=")
            rules[k] = v

        result = generate_lsystem(axiom, rules, iterations)
        draw_lsystem(t, result, angle, step=5)

    tk.Button(panel, text="Generate", command=generate).pack(pady=10)

    root.mainloop()
