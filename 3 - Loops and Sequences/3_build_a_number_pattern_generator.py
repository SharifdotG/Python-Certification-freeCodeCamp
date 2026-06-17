def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    generated_numbers = []
    for i in range(n):
        generated_numbers.append(str(i + 1))

    return " ".join(generated_numbers)
