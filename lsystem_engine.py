def generate_lsystem(axiom, rules, iterations):
    current = axiom

    for _ in range(iterations):
        next_string = ""
        for ch in current:
            next_string += rules.get(ch, ch)
        current = next_string

    return current
