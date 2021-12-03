import timeit 
from statistics import mode
from copy import copy

def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    with open(input, "r") as file:
        data = [line.strip() for line in file]
    return data


def calculate_power_consumption(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        items = [item[i] for item in data]
        gamma += max(items, key=items.count)
        epsilon += min(items, key=items.count)
    return int(gamma, 2) * int(epsilon, 2)


def calculate_life_support_rating(data):
    return_data = []
    for i in range(2):
        data_copy = copy(data)
        for j in range(len(data[0])):
            items = [item[j] for item in data_copy]
            max_bit = max(items, key=items.count)
            min_bit = min(items, key=items.count)
            if (i == 0):
                bit_to_use = "1" if max_bit == min_bit else max_bit
            else:
                bit_to_use = "0" if max_bit == min_bit else min_bit
            data_copy = [item for item in data_copy if item[j] == bit_to_use]
            if len(data_copy) == 1:
                return_data.append(int(data_copy[0], 2))
                break
    return return_data[0] * return_data[1]

if __name__ == "__main__":
    test_data = read_file('test_input.txt')
    assert calculate_life_support_rating(test_data) == 230

    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print(f'Challenge 1 Answer: {calculate_power_consumption(data)}')
    print(f'Challenge 2 Answer: {calculate_life_support_rating(data)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))