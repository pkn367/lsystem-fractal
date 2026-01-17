def generate_lsystem(axiom, rules, iterations):
    result = axiom
    for _ in range(iterations):
        next_string = []
        for ch in result:
            next_string.append(rules.get(ch, ch))
        result = "".join(next_string)
    return result

