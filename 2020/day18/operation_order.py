import timeit


def read_file(filename):
    '''Returns the processed data from the file.'''
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def sum_all_equations(equations, challenge1=True):
    count = 0
    for item in equations:
        if challenge1:
            count += calculate_equation(item)
        else:
            count += eval(item)
    return count


def convert_equations(equations):
    converted_equations = []
    for equation in equations:
        equation = equation.split(" ")
        indices = [i for i, j in enumerate(equation) if j == '+']
        for i in indices:
            equation[i-1] = '(' + equation[i-1]
            equation[i+1] = equation[i+1] + ')'
        converted_equations.append(" ".join(equation))
    return converted_equations


def calculate_equation(equation):
    value = 0
    sign = ""
    i = 0
    while i < len(equation):
        char = equation[i]
        if char == " ":
            i += 1
            continue
        if char == "(":
            parenthesis_value = calculate_equation(equation[i+1:])
            if sign == "+":
                value += parenthesis_value[1]
            elif sign == "*":
                value *= parenthesis_value[1]
            else:
                value = parenthesis_value[1]
            i += parenthesis_value[0] + 1
        elif char == ")":
            return (i, value)
        elif char == "*":
            sign = "*"
        elif char == "+":
            sign = "+"
        else:
            if sign == "+":
                value += int(char)
            elif sign == "*":
                value *= int(char)
            else:
                value = int(char)
        i += 1
    return value


if __name__ == "__main__":
    test_equations = read_file("test_input.txt")
    assert sum_all_equations(test_equations) == 26335
    test_converted_equations = convert_equations(test_equations)
    assert sum_all_equations(test_converted_equations, False) == 693891
    
    equations = read_file("input.txt")
    start_time = timeit.default_timer()
    print("Challenge 1 Answer:", sum_all_equations(equations))
    converted_equations = convert_equations(equations)
    print("Challenge 2 Answer:", sum_all_equations(converted_equations, False))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))


