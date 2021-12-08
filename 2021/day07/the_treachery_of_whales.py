import timeit
import numpy as np
from copy import copy
from collections import defaultdict
import math


def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    data = []
    with open(input, "r") as file:
        for line in file:
            line = line.strip().split(",")
            data.extend([int(item) for item in line])
    return data


def the_treachery_of_whales(data, increased_fuel_usage=False):
    max_height, min_height = max(data), min(data)
    fuel = defaultdict(lambda: 0)
    for i in range(min_height, max_height+1):
        print(f"{i}/{max_height+1}")
        for crab in data:
            if not increased_fuel_usage:
                fuel[i] += abs(crab - i)
            else:
                difference = abs(crab - i)
                fuel[i] += sum([i for i in range(1, difference+1)])
    return min(fuel.values())


if __name__ == "__main__":
    test_data = read_file('test_input.txt')
    assert the_treachery_of_whales(test_data) == 37
    assert the_treachery_of_whales(test_data, increased_fuel_usage=True) == 168


    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print(f'Challenge 1 Answer: {the_treachery_of_whales(data)}')
    print(f'Challenge 2 Answer: {the_treachery_of_whales(data, increased_fuel_usage=True)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
