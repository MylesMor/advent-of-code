import timeit
import itertools

def read_file(filename):
    '''Returns a list of numbers (one on each line) in the file.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        number_list = [int(line.strip()) for line in lines]            
    return number_list


def encoding_error(numbers, preamble_length):
    '''Returns the number that is not the sum of two of the previous 25 numbers.'''
    max_index = preamble_length
    for min_index in range(len(numbers)):
        found = False
        sum_of_two = numbers[max_index]
        numbers_to_check = [number for number in numbers[min_index:max_index] if number <= sum_of_two]
        for combination in itertools.combinations(numbers_to_check, 2):
            if sum(combination) == sum_of_two:
                max_index += 1
                found = True
                break
        if not found:
            return sum_of_two


def encoding_error2(numbers, invalid_number):
    '''Returns the max + min value of a list of contiguous 
    numbers in numbers that add to invalid number.'''
    for min_index in range(len(numbers)):
        counter = 0
        contiguous_numbers = []
        for number in numbers[min_index:]:
            counter += number
            if counter > invalid_number:
                break
            contiguous_numbers.append(number)
            if counter == invalid_number:
                return min(contiguous_numbers) + max(contiguous_numbers)


if __name__ == "__main__":
    test_numbers = read_file("test_input.txt")
    test_invalid_entry = encoding_error(test_numbers, 5)
    assert test_invalid_entry == 127
    assert encoding_error2(test_numbers, test_invalid_entry) == 62

    start_time = timeit.default_timer()
    numbers = read_file("input.txt")
    invalid_entry = encoding_error(numbers, 25)
    print("Challenge 1 Answer:", invalid_entry)        
    print("Challenge 2 Answer:", encoding_error2(numbers, invalid_entry))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))