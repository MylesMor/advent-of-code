import timeit
from collections import defaultdict
import itertools

def read_file(filename):
    '''Returns the instructions from the file.'''
    with open(filename, "r") as file:
        data = []
        for line in file.readlines():
            if line.startswith("mask"):
                data.append(line.strip().split(" = ")[1])
            elif line.startswith("mem"):
                split = line.strip().split("] = ")
                data.append([int(split[0].split("[")[1]), int(split[1])])
    return data


def docking_data(data, challenge):
    '''Sorts data by challenge and returns final result.'''
    current_mask = None
    mem_dict = defaultdict(lambda: 0)
    for d in data:
        if isinstance(d, str):
            current_mask = d
        else:
            if challenge == 1:
                result = challenge_1(d, current_mask)
            else:
                result = challenge_2(d, current_mask)
            for item in result:
                mem_dict[item[0]] = item[1]
    final_count = 0
    for v in mem_dict.values():
        if v != 0:
            final_count += v
    return final_count


def challenge_1(single_data, current_mask):
    '''Returns final memory position and data after calculation.'''
    position = single_data[0]
    binary = str(bin(single_data[1]))[2:]
    char_list = ["0" for char in range(len(current_mask)-len(binary))]
    char_list.extend(list(binary))
    for count, char in enumerate(current_mask):
        if char != "X":
            char_list[count] = char
    dec = int(''.join(char_list), 2)
    return [[position, dec]]


def challenge_2(single_data, current_mask):
    '''Returns final memory positions and data after calculation.'''
    binary = str(bin(single_data[0]))[2:]
    char_list = ["0" for char in range(len(current_mask)-len(binary))]
    char_list.extend(list(binary))
    for count, char in enumerate(current_mask):
        if char != "0":
            char_list[count] = char
    number_of_X = current_mask.count("X")
    list_of_mems = [char_list.copy() for _ in range(2**number_of_X)]
    combinations = list(itertools.product([0, 1], repeat=number_of_X))
    for count_mem, mem in enumerate(list_of_mems):
        count_x = 0
        for count_char, char in enumerate(mem):
            if char == "X":
                mem[count_char] = str(combinations[count_mem][count_x])
                count_x += 1
    final_list = []
    for mem in list_of_mems:
        dec = int(''.join(mem), 2)
        final_list.append([dec, single_data[1]])
    return final_list


if __name__ == "__main__":
    test_data = read_file("test_input.txt")
    assert docking_data(test_data, 1) == 165

    test_data = read_file("test_input2.txt")
    assert docking_data(test_data, 2) == 208
    
    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print("Challenge 1 Answer:", docking_data(data, 1))
    print("Challenge 2 Answer:", docking_data(data, 2))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))