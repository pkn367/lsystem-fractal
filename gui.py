import tkinter as tk
from tkinter import ttk
from lsystem_engine import generate_lsystem
from turtle_renderer import draw_lsystem
import threading

class LSystemGUI:
    def __init__(self, root):
        self.root = root
        root.title("L-System Fractal Architect")
        root.geometry("350x500")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Axiom").pack()
        self.axiom = ttk.Entry(self.root)
        self.axiom.pack()

        ttk.Label(self.root, text="Rule (comma separated)").pack()
        self.rules = ttk.Entry(self.root)
        self.rules.pack()

        ttk.Label(self.root, text="Angle").pack()
        self.angle = ttk.Entry(self.root)
        self.angle.pack()

        ttk.Label(self.root, text="Iterations").pack()
        self.iterations = ttk.Entry(self.root)
        self.iterations.pack()

        ttk.Button(self.root, text="Generate", command=self.generate).pack(pady=10)

        ttk.Label(self.root, text="Drawing Speed").pack()
        self.speed = ttk.Scale(self.root, from_=1, to=10, orient="horizontal")
        self.speed.set(5)
        self.speed.pack()

        ttk.Label(self.root, text="Presets").pack(pady=10)
        ttk.Button(self.root, text="🌿 Tree", command=self.tree).pack()
        ttk.Button(self.root, text="❄ Koch Snowflake", command=self.koch).pack()
        ttk.Button(self.root, text="🐉 Dragon Curve", command=self.dragon).pack()

    def generate(self):
        axiom = self.axiom.get()
        angle = float(self.angle.get())
        iterations = int(self.iterations.get())
        speed = float(self.speed.get())

        rules = {}
        for rule in self.rules.get().split(","):
            key, value = rule.split("=")
            rules[key.strip()] = value.strip()

        instructions = generate_lsystem(axiom, rules, iterations)

        threading.Thread(
            target=draw_lsystem,
            args=(instructions, angle, 5, speed),
            daemon=True
        ).start()

    def tree(self):
        self.axiom.delete(0, tk.END)
        self.rules.delete(0, tk.END)
        self.angle.delete(0, tk.END)
        self.iterations.delete(0, tk.END)

        self.axiom.insert(0, "F")
        self.rules.insert(0, "F=F[+F]F[-F]F")
        self.angle.insert(0, "25")
        self.iterations.insert(0, "5")

    def koch(self):
        self.axiom.delete(0, tk.END)
        self.rules.delete(0, tk.END)
        self.angle.delete(0, tk.END)
        self.iterations.delete(0, tk.END)

        self.axiom.insert(0, "F--F--F")
        self.rules.insert(0, "F=F+F--F+F")
        self.angle.insert(0, "60")
        self.iterations.insert(0, "4")

    def dragon(self):
        self.axiom.delete(0, tk.END)
        self.rules.delete(0, tk.END)
        self.angle.delete(0, tk.END)
        self.iterations.delete(0, tk.END)

        self.axiom.insert(0, "FX")
        self.rules.insert(0, "X=X+YF+,Y=-FX-Y")
        self.angle.insert(0, "90")
        self.iterations.insert(0, "10")
