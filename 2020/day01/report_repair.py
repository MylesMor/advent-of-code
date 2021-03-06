import itertools
import functools
import operator

def read_file(filename):
    '''Returns a list of integers from a file.'''
    with open(filename, "r") as file:
        numbers = [int(line) for line in file]
    return numbers

def report_repair(numbers, n, value):
    '''Finds n numbers in a list that sum to value.'''
    for combination in itertools.combinations(numbers, n):
        if sum(combination) == value:
            print("Answer: " + str(functools.reduce(operator.mul, combination)))
            return 

if __name__ == "__main__":
    numbers = read_file("input.txt")
    report_repair(numbers, 2, 2020)
    report_repair(numbers, 3, 2020)


