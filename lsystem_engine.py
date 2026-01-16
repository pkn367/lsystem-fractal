def generate_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current:
            next_string += rules.get(char, char)
        current = next_string
    return current
