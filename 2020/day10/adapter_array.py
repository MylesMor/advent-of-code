import timeit
from collections import defaultdict

def read_file(filename):
    '''Returns a list of numbers (one on each line) in the file.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        number_list = [int(line.strip()) for line in lines]            
    return number_list


def adapter_array(adapters, start_joltage):
    '''Returns the product of the total number of 1 jolt and 3 jolt differences.'''
    list_of_adapters = adapters.copy()
    list_of_adapters.append(start_joltage)
    sorted_adapters = sorted(list_of_adapters)
    jolt_difference_1, jolt_difference_3 = 0, 1
    for count, adapter in enumerate(sorted_adapters):
        if count < len(sorted_adapters)-1:
            if sorted_adapters[count+1] - adapter == 1:
                jolt_difference_1 += 1
            elif sorted_adapters[count+1] - adapter == 3:
                jolt_difference_3 += 1
    return jolt_difference_1 * jolt_difference_3


def adapter_array2(adapters, start_joltage):
    '''Counts and returns the total number of valid adapter arrangements.'''
    list_of_adapters = adapters.copy()
    list_of_adapters.append(start_joltage)
    sorted_adapters = sorted(list_of_adapters)
    sorted_adapters.append(max(adapters) + 3)
    possibilities = {}
    for count, adapter in enumerate(sorted_adapters):
        position = []
        for adapter_2 in sorted_adapters[count:count+4]:
            if 0 < adapter_2 - adapter <= 3:
                position.append(adapter_2)
        if len(position) != 0:
            possibilities[adapter] = position
    final_list = defaultdict(lambda: 0)
    final_list[0] = 1
    for key, value in possibilities.items():
        for possibility in value:
            final_list[possibility] += final_list[key]
    return final_list[max(final_list)]


if __name__ == "__main__":
    test_adapters = read_file("test_input.txt")
    assert adapter_array(test_adapters, 0) == 35
    assert adapter_array2(test_adapters, 0) == 8
    test_adapters = read_file("test_input2.txt")
    assert adapter_array(test_adapters, 0) == 220
    assert adapter_array2(test_adapters, 0) == 19208

    start_time = timeit.default_timer()
    adapters = read_file("input.txt")
    print("Challenge 1 Answer:", adapter_array(adapters, 0))
    print("Challenge 2 Answer:", adapter_array2(adapters, 0))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
    