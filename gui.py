import tkinter as tk
from lsystem_engine import generate_lsystem
from turtle_renderer import draw_lsystem


def run():
    root = tk.Tk()
    root.title("L-System Fractal Architect")

    canvas = tk.Canvas(root, width=900, height=600)
    canvas.pack(side=tk.LEFT)

    panel = tk.Frame(root)
    panel.pack(side=tk.RIGHT, padx=10)

    tk.Label(panel, text="Axiom").pack()
    axiom_entry = tk.Entry(panel)
    axiom_entry.insert(0, "F")
    axiom_entry.pack()

    tk.Label(panel, text="Rules (F=...)").pack()
    rules_entry = tk.Entry(panel)
    rules_entry.insert(0, "F=F[+F]F[-F]F")
    rules_entry.pack()

    tk.Label(panel, text="Angle").pack()
    angle_entry = tk.Entry(panel)
    angle_entry.insert(0, "25")
    angle_entry.pack()

    tk.Label(panel, text="Iterations").pack()
    iter_entry = tk.Entry(panel)
    iter_entry.insert(0, "4")
    iter_entry.pack()

    def on_generate():
        canvas.delete("all")  # 🚨 CLEAR CANVAS

        axiom = axiom_entry.get()
        angle = float(angle_entry.get())
        iterations = int(iter_entry.get())

        # Parse rules
        rules = {}
        rule_text = rules_entry.get()
        left, right = rule_text.split("=")
        rules[left.strip()] = right.strip()

        result = generate_lsystem(axiom, rules, iterations)

        draw_lsystem(canvas, result, angle)

    tk.Button(panel, text="Generate", command=on_generate).pack(pady=10)

    root.mainloop()

