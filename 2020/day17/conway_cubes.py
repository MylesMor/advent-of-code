import timeit
import itertools
from collections import defaultdict


def read_file(filename):
    '''Returns the processed data from the file.'''
    with open(filename, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def active_positions(data, dimensions):
    '''Returns the positions of cubes that are active.'''
    active_positions = []
    for x in range(len(data)):
        for y in range(len(data)):
            if data[x][y] == "#":
                active_positions.append((x, y, *([0]*(dimensions-2))))
    return active_positions


def find_active_neighbours(active, dimensions):
    '''Returns the number of active neighbours for each position.
    
    Loops through each current active position and adds one
    to all their neighbour's counts, effectively identifying and
    counting all required positions for each cycle.
    '''
    neighbours = defaultdict(lambda: 0)
    for active_position in active:
        for change in itertools.product([x for x in range(-1, 2)], repeat=dimensions):
            if change != tuple(0 for x in range(dimensions)):
                tup = tuple(i+j for i, j in zip(active_position, change))
                neighbours[tup] += 1
    return neighbours


def run_cycles(data, dimensions, number_of_cycles):
    '''Returns the number of active positions after number_of_cycles cycles.'''
    active = active_positions(data, dimensions)
    for _ in range(number_of_cycles):
        new_active = []
        neighbors = find_active_neighbours(active, dimensions)
        for k, v in neighbors.items():
            if (v == 2 and k in active) or v == 3:
                new_active.append(k)
        active = new_active
    return len(new_active)
    
    

if __name__ == "__main__":
    test_data = read_file(("test_input.txt"))
    assert run_cycles(test_data, 3, 6) == 112
    assert run_cycles(test_data, 4, 6) == 848

    start_time = timeit.default_timer()
    data = read_file(("input.txt"))
    print("Challenge 1 Answer:", run_cycles(data, 3, 6))
    print("Challenge 2 Answer:", run_cycles(data, 4, 6))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))