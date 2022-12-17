import timeit

def read_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def rucksack_reorganization(rucksack_list):
    shared_items = []
    for rucksack in rucksack_list:
        half = int(len(rucksack)/2)
        compartment_1 = rucksack[:half]
        compartment_2 = rucksack[half:]
        for item in compartment_1:
            if item in compartment_2:
                shared_items.append(item)
                break
    return sum(prioritize_items(shared_items))


def rucksack_reorganization_2(rucksack_list):
    badges = []
    for x in range(0, len(rucksack_list), 3):
        for item in rucksack_list[x]:
            if item in rucksack_list[x+1] and item in rucksack_list[x+2]:
                badges.append(item)
                break 
    return sum(prioritize_items(badges))


def prioritize_items(items):
    priority = []
    for item in items:
        char_code = ord(item)
        if char_code >= 97:
            priority.append(char_code - 96)
        elif char_code >= 65:
            priority.append(char_code - (64-26))
    return priority


if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert rucksack_reorganization(test_lines) == 157
    assert rucksack_reorganization_2(test_lines) == 70

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {rucksack_reorganization(lines)}')
    print(f'Challenge 2 Answer: {rucksack_reorganization_2(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
