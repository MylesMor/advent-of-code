import timeit


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            pairs = line.strip().split(",")
            pair_line = []
            for item in pairs:
                elf_string = item.split("-")
                pair_line.append([x for x in range(int(elf_string[0]), int(elf_string[1])+1, 1)])
            lines.append(pair_line)
    return lines


def camp_cleanup(pairs_list):
    fully_contains = 0
    for pair in pairs_list:
        if pair[0] == pair[1]:
            fully_contains += 1
        elif len(pair[0]) == len(pair[1]):
            pass
        else:
            largest_pair = 0 if len(pair[0]) > len(pair[1]) else 1
            if (set(pair[abs(largest_pair-1)]).issubset(set(pair[largest_pair]))):
                fully_contains += 1
    return fully_contains


def camp_cleanup_2(pairs_list):
    overlapping = 0
    for pair in pairs_list:
        largest_pair = 0 if len(pair[0]) > len(pair[1]) else 1
        for item in pair[abs(largest_pair-1)]:
            if item in pair[largest_pair]:
                overlapping += 1
                break
    return overlapping


if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert camp_cleanup(test_lines) == 2
    assert camp_cleanup_2(test_lines) == 4

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {camp_cleanup(lines)}')
    print(f'Challenge 2 Answer: {camp_cleanup_2(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
