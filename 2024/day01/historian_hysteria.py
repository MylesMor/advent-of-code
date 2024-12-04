import timeit
import re
from collections import defaultdict


def read_file(filename):
    lists = [[], []]
    with open(filename, "r") as file:
        for line in file:
            numbers = line.rstrip().split("   ")
            lists[0].append(int(numbers[0]))
            lists[1].append(int(numbers[1]))
       
    return lists


def part_one(lists):
    sorted_list_1 = sorted(lists[0])
    sorted_list_2 = sorted(lists[1])
    distances = 0
    for i in range(len(sorted_list_1)):
        distances += abs(sorted_list_1[i] - sorted_list_2[i])
    return distances


def part_two(lists):
    counts = defaultdict(lambda: 0)
    for item in lists[1]:
        counts[item] += 1
    answer = sum(x * counts[x] for x in lists[0])
    return answer


if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    test_answer = part_one(test_lines)
    assert test_answer == 11
    test_answer_2 = part_two(test_lines)
    assert test_answer_2 == 31

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    answer_1 = part_one(lines)
    answer_2 = part_two(lines)
    print(f'Challenge 1 Answer: {answer_1}')
    print(f'Challenge 2 Answer: {answer_2}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
