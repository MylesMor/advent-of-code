import timeit


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            parts = ['noop', 0] if line == 'noop' else line.split(" ")
            lines.append([parts[0], int(parts[1])])
    return lines


def find_signal_strengths(lines, start_cycle=20, cycle_interval=40):
    signal_strengths = []
    drawing = ""
    x = 1
    current_cycle = 0
    for line in lines:
        instruction, number = line[0], line[1]
        if instruction == 'addx':
            for _ in range(1, 3):
                drawing += check_drawing(current_cycle, x)
                current_cycle += 1
                signal_strengths.extend(check_cycle(current_cycle, start_cycle, cycle_interval, x))
            x += number 
        else:
            drawing += check_drawing(current_cycle, x)
            current_cycle += 1
            signal_strengths.extend(check_cycle(current_cycle, start_cycle, cycle_interval, x))
    return [sum(signal_strengths), drawing]


def check_cycle(current_cycle, start_cycle, cycle_interval, x):
    if current_cycle == start_cycle or ((current_cycle - start_cycle) % cycle_interval) == 0:
        return [x * current_cycle]
    return []

def check_drawing(current_cycle, x):
    if current_cycle % 40 in [x for x in range(x-1, x+2)]:
        return '#'
    else:
        return '.'
    

if __name__ == "__main__":

    part_two_test_solution = '''
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
'''

    test_lines = read_file("test_input.txt")
    test_solution = find_signal_strengths(test_lines, 20, 40)
    assert test_solution[0] == 13140
    assert test_solution[1] == part_two_test_solution.replace("\n", "").strip()

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    solution = find_signal_strengths(lines, 20, 40)

    print(f'Challenge 1 Answer: {solution[0]}')
    print(f'Challenge 2 Answer:')
    for cycle_range in range(0, len(solution[1]), 40):
        print(solution[1][cycle_range:cycle_range+40].replace(".", " "))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
