def generate_lsystem(axiom, rules, iterations):
    current = axiom

    for _ in range(iterations):
        next_string = ""
        for char in current:
            if char in rules:
                next_string += rules[char]
            else:
                next_string += char
        current = next_string

    return current

