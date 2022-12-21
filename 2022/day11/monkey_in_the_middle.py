import timeit
import math
from copy import deepcopy
import math


def read_file(filename):
    monkeys = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for x in range(0, len(lines), 7):

            starting_items = [int(number) for number in lines[x+1].strip().split(": ")[1].split(', ')]
            operation = lines[x+2].strip().split(": new = ")[1]
            worry_decrease = 'old / 3'
            test = f'old % {lines[x+3].strip().split(" ")[-1]}'
            true = int(lines[x+4].strip().split(" ")[-1])
            false = int(lines[x+5].strip().split(" ")[-1])

            monkeys.append([starting_items, operation, worry_decrease, test, true, false])

    return monkeys


def perform_operation(operation_string, old):
    operation_string = operation_string.replace('old', str(old))
    parts = operation_string.split(" ")
    operation, var1, var2 = parts[1], int(parts[0]), int(parts[2])
    if '*' in operation:
        return var1 * var2
    if '+' in operation:
        return var1 + var2
    if '-' in operation:
        return var1 - var2
    if '/' in operation:
        return var1 / var2
    if '%' in operation:
        return var1 % var2


def monkey_in_the_middle(monkeys, rounds, worry_division=True):

    modulo = 1

    for monkey in monkeys:
        modulo *= int(monkey[3].split(" % ")[1])    
    
    monkey_inspection_counts = [0 for _ in range(len(monkeys))]
    for x in range(0, rounds):
        inspection = 0
        for monkey in monkeys:
            for starting_item_number in range(len(monkey[0])):

                monkey_inspection_counts[inspection] += 1
                worry = monkey[0][starting_item_number]
                worry = perform_operation(monkey[1], worry)
                
                if worry_division:
                    worry = math.floor(perform_operation(monkey[2], worry))

                worry = worry % modulo

                test_op = perform_operation(monkey[3], worry)
                test = True if test_op == 0 else False
                if test:
                    monkeys[monkey[4]][0].append(worry)
                else:
                    monkeys[monkey[5]][0].append(worry)
            inspection += 1
            monkey[0] = []

    print(monkey_inspection_counts)
    first_max = max(monkey_inspection_counts)
    monkey_inspection_counts.remove(first_max)
    second_max = max(monkey_inspection_counts)

    return first_max * second_max

if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert monkey_in_the_middle(deepcopy(test_lines), 20) == 10605
    assert monkey_in_the_middle(deepcopy(test_lines), 10000, False) == 2713310158

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {monkey_in_the_middle(deepcopy(lines), 20)}')
    print(f'Challenge 2 Answer: {monkey_in_the_middle(deepcopy(lines), 10000, False)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
