import timeit
from collections import defaultdict
from copy import deepcopy    


def read_file(filename):
    stacks = defaultdict(lambda: [])
    instructions = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines[::-1]:
            line = line.replace("\n", "")
            if '[' in line:
                row = [line[x:x+3].strip() for x in range(0, len(line), 4)]
                for x in range(len(row)):
                    if row[x] != "":
                        stacks[x+1].extend([row[x][1]])
        for line in lines:
            if line.startswith("move"):
                parts = line.strip().split(" ")
                instructions.append([int(parts[1]), int(parts[3]), int(parts[5])])
    return [stacks, instructions]


def supply_stacks(lines, part_one=True):
    stacks, instructions = lines[0], lines[1]
    for instruction in instructions:
        popped = []
        for _ in range(instruction[0]):
            popped.append(stacks[instruction[1]].pop())
        if part_one:
            stacks[instruction[2]].extend(popped)
        else:
            stacks[instruction[2]].extend(popped[::-1])
    final_string = ""
    for stack in stacks.values():
        if len(stack) > 0:
            final_string += stack.pop()
    return final_string


if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert supply_stacks(deepcopy(test_lines), True) == 'CMZ'
    assert supply_stacks(test_lines, False) == 'MCD'

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {supply_stacks(deepcopy(lines), True)}')
    print(f'Challenge 2 Answer: {supply_stacks(lines, False)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
