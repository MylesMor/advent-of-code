import timeit
import numpy as np


def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    data = []
    x = []
    y = []
    with open(input, "r") as file:
        for line in file:
            halves = line.strip().split(' -> ')
            coords = []
            for item in halves:
                coords_set = item.split(",")
                x.append(int(coords_set[0]))
                y.append(int(coords_set[1]))
                coords.append([int(number) for number in coords_set])
            data.append(coords)
    shape = (max(x)+1, max(y)+1)
    return data, shape


def hydrothermal_venture(data, shape, diagonal=False):
    array = np.zeros(shape)
    for item in data:
        x1, y1 = item[0][0], item[0][1]
        x2, y2 = item[1][0], item[1][1]

        # VERTICAL
        if x1 == x2:
            if (y1 > y2):
                start, stop, jump = y1, y2-1, -1
            else:
                start, stop, jump = y1, y2+1, 1
            for i in range(start, stop, jump):
                array[i][x1] += 1

        # HORIZONTAL
        elif y1 == y2:
            if (x1 > x2):
                start, stop, jump = x1, x2-1, -1
            else:
                start, stop, jump = x1, x2+1, 1
            for i in range(start, stop, jump):
                array[y1][i] += 1

        # DIAGONAL
        elif diagonal:
            x_direction = -1 if x1 > x2 else 1
            y_direction = -1 if y1 > y2 else 1
            for i in range(abs(x1 - x2)+1):
                array[y1][x1] += 1
                x1 += x_direction
                y1 += y_direction
    count = (array > 1).sum()
    return count


if __name__ == "__main__":
    test_data, shape = read_file('test_input.txt')
    assert hydrothermal_venture(test_data, shape) == 5
    assert hydrothermal_venture(test_data, shape, diagonal=True) == 12

    start_time = timeit.default_timer()
    data, shape = read_file("input.txt")
    print(f'Challenge 1 Answer: {hydrothermal_venture(data, shape)}')
    print(f'Challenge 2 Answer: {hydrothermal_venture(data, shape, diagonal=True)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
