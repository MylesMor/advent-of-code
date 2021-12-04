import timeit
from statistics import mode
from copy import copy
import numpy as np


def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    with open(input, "r") as file:
        numbers = file.readline().strip().split(",")
        numbers = [int(number) for number in numbers]

        # Split into seperate grids
        grids = "".join(file.readlines()).split("\n\n")

        # Remove new lines, double spaces and split into seperate numbers
        grids = [line.replace("\n", " ").replace("  ", " ").split(" ") for line in grids]

        # Remove empty strings from grid and convert remaining to ints
        for line in grids:
            for item in line:
                if len(item) == 0:
                    line.remove(item)
                    continue
                item = int(item)

        # Create NumPy arrays for each grid
        arrays = []
        for item in grids:
            arrays.append(np.array(item).astype(int).reshape((5, 5)))
    return (numbers, arrays)


def bingo(numbers, arrays, last=False):
    winners = []
    last_score = 0
    for number in numbers:
        for count, array in enumerate(arrays):
            if count not in winners:

                # Find number in array grids
                itemindex = np.where(array==number)

                if len(itemindex[0]) != 0:
                    columns = array.T[0:len(array[0])]

                    # Set item to be marked
                    array[itemindex[0][0]][itemindex[1][0]] = 0

                    for item in range(len(array[0])):

                        # ROWS
                        if len([x for x in array[item] if x == 0]) == 5:
                            if not last:
                                return array.sum() * number
                            winners.append(count)
                            last_score = array.sum() * number

                        # COLUMNS
                        if len([x for x in columns[item] if x == 0]) == 5:
                            if not last:
                                return array.sum() * number
                            winners.append(count)
                            last_score = array.sum() * number
    return last_score


if __name__ == "__main__":
    test_data = read_file('test_input.txt')
    assert bingo(test_data[0], test_data[1]) == 4512

    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print(f'Challenge 1 Answer: {bingo(data[0], data[1])}')
    print(f'Challenge 2 Answer: {bingo(data[0], data[1], last=True)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))