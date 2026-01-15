import tkinter as tk
import turtle

from lsystem_engine import generate_lsystem
from turtle_renderer import draw_lsystem


def run():
    root = tk.Tk()
    root.title("L-System Fractal Architect")

    # ===== Layout =====
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack(side=tk.LEFT)

    control = tk.Frame(root, padx=10)
    control.pack(side=tk.RIGHT, fill=tk.Y)

    # ===== Turtle setup (EMBEDDED) =====
    screen = turtle.TurtleScreen(canvas)
    t = turtle.RawTurtle(screen)

    # ===== Inputs =====
    tk.Label(control, text="Axiom").pack()
    axiom_entry = tk.Entry(control)
    axiom_entry.insert(0, "F")
    axiom_entry.pack()

    tk.Label(control, text="Rule (F:...)").pack()
    rule_entry = tk.Entry(control)
    rule_entry.insert(0, "F:F+F--F+F")
    rule_entry.pack()

    tk.Label(control, text="Angle").pack()
    angle_entry = tk.Entry(control)
    angle_entry.insert(0, "60")
    angle_entry.pack()

    tk.Label(control, text="Iterations").pack()
    iter_entry = tk.Entry(control)
    iter_entry.insert(0, "3")
    iter_entry.pack()

    # ===== Button Action =====
    def on_generate():
        axiom = axiom_entry.get()
        rule_text = rule_entry.get()
        angle = float(angle_entry.get())
        iterations = int(iter_entry.get())

        symbol, replacement = rule_text.split(":")
        rules = {symbol: replacement}

        result = generate_lsystem(axiom, rules, iterations)
        draw_lsystem(t, result, angle)

    tk.Button(control, text="Generate", command=on_generate).pack(pady=10)

    root.mainloop()
