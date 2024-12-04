import timeit
import re


def read_file(filename):
    reports = []
    with open(filename, "r") as file:
        for line in file:
            reports.append([int(x) for x in line.strip().split(" ")])
    return reports

def part_one(lines):
    valid = 0
    for line in lines:
        diff = get_differences(line)
        valid += get_validity_of_report(diff)
    return valid

def part_two(lines):
    valid = 0
    for line in lines:
        for i in range(len(line)):
            diff = get_differences(line[:i] + line[i+1:])
            is_valid = get_validity_of_report(diff)
            if is_valid == 1:
                valid += 1
                break
    return valid

def get_differences(report):
    return [value-report[count+1] for (count, value) in enumerate(report[:len(report)-1])]

def get_validity_of_report(diff):
    valid_count = 0
    increasing = True if diff[0] > 0 else False
    for item in diff:
        if abs(item) not in [1,2,3] or (increasing and item < 0) or (not increasing and item > 0):
            break
        valid_count += 1
    if valid_count == len(diff):
        return 1
    return 0

if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    test_answer = part_one(test_lines)
    assert test_answer == 2
    test_answer_2 = part_two(test_lines)
    assert test_answer_2 == 4

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    answer_1 = part_one(lines)
    answer_2 = part_two(lines)
    print(f'Challenge 1 Answer: {answer_1}')
    print(f'Challenge 2 Answer: {answer_2}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))

