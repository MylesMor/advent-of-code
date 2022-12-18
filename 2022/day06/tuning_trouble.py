import timeit


def read_file(filename):
    with open(filename, "r") as file:
        return file.readline().strip()


def tuning_trouble(buffer, marker_length):
    for x in range(0, len(buffer)):
        marker = buffer[x:x+marker_length]
        if len(set(marker)) == len(marker):
            return x+marker_length


if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert tuning_trouble(test_lines, 4) == 7
    assert tuning_trouble(test_lines, 14) == 19

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {tuning_trouble(lines, 4)}')
    print(f'Challenge 2 Answer: {tuning_trouble(lines, 14)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
