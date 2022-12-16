import timeit
from collections import defaultdict

def read_file(filename):
    '''Returns a list of integers from a file.'''
    numbers = []
    with open(filename, "r") as file:
        total = 0
        for line in file:
            if line != "\n":
                total += int(line)
            else:
                numbers.append(total)
                total = 0
    return numbers


def calorie_counting(numbers):
    return max(numbers)

def calorie_counting_2(numbers):
    return sum(sorted(numbers, reverse=True)[:3])

if __name__ == "__main__":
    start_time = timeit.default_timer()
    numbers = read_file("input.txt")
    print(f'Challenge 1 Answer: {calorie_counting(numbers)}')
    print(f'Challenge 2 Answer: {calorie_counting_2(numbers)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
