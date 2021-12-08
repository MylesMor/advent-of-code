import timeit
import numpy as np
from copy import copy
from collections import defaultdict
import math

SEGMENTS = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    data = []
    with open(input, "r") as file:
        for line in file:
            line = line.strip().split(" | ")
            data_line = []
            data_line.append(line[0].split(" "))
            data_line.append(line[1].split(" "))
            data.append(data_line)
    return data


def easy_digits(data):
    lengths = [SEGMENTS[1], SEGMENTS[4], SEGMENTS[7], SEGMENTS[8]]
    count = 0
    for item in data:
        for output in item[1]:
            if len(output) in lengths:
                count += 1
    return count


def seven_segment_search(data):
    outputs = []
    for item in data:
        lengths = defaultdict(list)
        positions = defaultdict(list)
        sorted_list = sorted(item[0], key=len)
        numbers = {}
        for pattern in sorted_list:
            lengths[len(pattern)].append(pattern)
        for length, pattern in lengths.items():
            if length == 2:
                # NUMBER 1
                positions['NE'].extend([char for char in pattern[0]])
                positions['SE'].extend([char for char in pattern[0]])
            if length == 3:
                # NUMBER 7
                positions['N'].extend([char for char in pattern[0] if char not in positions['NE']])
            if length == 4:
                # NUMBER 4
                positions['M'].extend([char for char in pattern[0] if char not in positions['NE']])
                positions['NW'].extend([char for char in pattern[0]  if char not in positions['NE']])
            if length == 5:
                for p in pattern:
                    matches = [char for char in p if char in positions['NE']]
                    if len(matches) == 2:
                        # NUMBER 3
                        m_position = [char for char in p if char not in positions['NE'] and char in positions['M']]
                        positions['M'] = m_position
                        positions['NW'].remove(m_position[0])
                        positions['S'] = [char for char in p if char not in positions['NE'] and char not in positions['M'] and char not in positions['N']]
                        break
                for p in pattern:
                    matches = [char for char in p if char in positions['NW']]
                    if len(matches) == 1:
                        # NUMBER 5
                        positions['SE'] = [char for char in p if char not in positions['N'] and char not in positions['S'] and char not in positions['M'] and char not in positions['NW']]
                        positions['NE'].remove(positions['SE'][0])
                        break
                for p in pattern:
                    matches = [char for char in p if char not in positions['N'] and char not in positions['S'] and char not in positions['M'] and char not in positions['SE'] and char not in positions['NE'] and char not in positions['NW']]
                    if len(matches) == 1:
                        # NUMBER 2
                        positions['SW'] = matches
                        break
        n, m, s = positions['N'][0], positions['M'][0], positions['S'][0]
        ne, nw = positions['NE'][0], positions['NW'][0]
        se, sw = positions['SE'][0], positions['SW'][0]
        numbers[0] = n + ne + se + s + sw + nw
        numbers[1] = ne + se
        numbers[2] = n + ne + m + sw + s
        numbers[3] = n + ne + m + se + s
        numbers[4] = nw + ne + m + se
        numbers[5] = n + nw + m + se + s
        numbers[6] = n + nw + m + se + s + sw
        numbers[7] = numbers[1] + n
        numbers[8] = numbers[0] + m
        numbers[9] = n + ne + se + m + nw + s
        output = ""
        for coded_output in item[1]:
            for key, value in numbers.items():
                if (sorted(coded_output) == sorted(value)):
                    output += str(key)
        outputs.append(int(output))
    return sum(outputs)



if __name__ == "__main__":
    test_data1 = read_file('test_input1.txt')
    test_data2 = read_file('test_input2.txt')
    assert easy_digits(test_data2) == 26
    assert seven_segment_search(test_data1) == 5353
    assert seven_segment_search(test_data2) == 61229

    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print(f'Challenge 1 Answer: {easy_digits(data)}')
    print(f'Challenge 2 Answer: {(seven_segment_search(data))}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
