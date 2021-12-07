import timeit
import numpy as np
from copy import copy
from collections import deque


def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    data = []
    with open(input, "r") as file:
        for line in file:
            line = line.strip().split(",")
            data.extend([int(item) for item in line])
    return data


def lanternfish(initial_state, days):
    day = 1
    fish_list = initial_state.copy()
    while day <= days:
        print(len(fish_list))
        for i in range(len(fish_list)):
            if fish_list[i] == 0:
                fish_list[i] = 6
                fish_list.append(8)
                continue
            fish_list[i] -= 1
        day += 1
    return len(fish_list)


def unlimited_lanternfish(data, days):
    fish_ages = [0 for _ in range(9)]
    for item in data:
        fish_ages[item] += 1
    for _ in range(days):

        # Shift all fish ages to the left each day
        fish_ages = fish_ages[1:] + fish_ages[:1]

        # Add one 6 if a new fish has been created
        if fish_ages[8] > 0:
            fish_ages[6] += 1 * fish_ages[8]
    return sum(fish_ages)


if __name__ == "__main__":
    test_data = read_file('test_input.txt')
    assert lanternfish(test_data, 18) == 26
    assert lanternfish(test_data, 80) == 5934

    assert unlimited_lanternfish(test_data, 18) == 26
    assert unlimited_lanternfish(test_data, 80) == 5934
    assert unlimited_lanternfish(test_data, 256) == 26984457539

    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print(f'Challenge 1 Answer: {unlimited_lanternfish(data, 80)}')
    print(f'Challenge 2 Answer: {unlimited_lanternfish(data, 256)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
