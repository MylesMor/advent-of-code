import timeit
from collections import defaultdict

def read_file(filename):
    '''Returns the data from the file.'''
    with open(filename, "r") as file:
        data = []
        for line in file.readlines():
            data.extend(int(x) for x in line.strip().split(","))
    return data


def rambunctious_recitation(data, value_to_find):
    '''Returns the value_to_find'th number in the sequence.'''
    numbers = defaultdict(lambda: 0)
    number_list = data.copy()
    count = 1
    for number in data:
        numbers[number] = count
        count += 1
    while count < value_to_find + 2:
        last_number = number_list[count-2]
        if last_number not in numbers:
            number_list.append(0)
        else:
            number_list.append((count-1) - numbers[last_number])
        numbers[last_number] = count-1
        count += 1
    return number_list[value_to_find-1]


if __name__ == "__main__":
    test_data = read_file("test_input.txt")
    assert rambunctious_recitation(test_data, 2020) == 436

    data = read_file("input.txt")
    start_time = timeit.default_timer()
    print("Challenge 1 Answer:", rambunctious_recitation(data, 2020))
    print("Challenge 2 Answer:", rambunctious_recitation(data, 30000000))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))