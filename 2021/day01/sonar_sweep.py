import timeit 

def read_file(filename):
    '''Returns a list of integers from a file.'''
    with open(filename, "r") as file:
        numbers = [int(line) for line in file]
    return numbers


def count_increases(numbers):
    increased = 0
    for count, item in enumerate(numbers[1:]):
        if item > numbers[count]:
            increased += 1
    return increased


def count_window_increases(numbers, window_size):
    increased = 0
    for i in range(window_size, len(numbers)):
        if (sum(numbers[i+1-window_size:i+1]) > sum(numbers[i-window_size:i])):
            increased += 1
    return increased


if __name__ == "__main__":
    start_time = timeit.default_timer()
    numbers = read_file("input.txt")
    print(f'Challenge 1 Answer: {count_increases(numbers)}')
    print(f'Challenge 2 Answer: {count_window_increases(numbers, 3)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
