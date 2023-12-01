import timeit
import re


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]
    return lines

def trebuchet(lines):
    final_calibration = 0
    for line in lines:
        numbers = re.sub('[A-z]', '', line)
        if len(numbers) > 0:
            final_calibration += int(f'{numbers[0]}{numbers[-1]}')
    return final_calibration

def trebuchet_2(lines):
    valid_word_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    final_calibration = 0
    for line in lines:
        number_positions = []

        # Find position of word numbers
        for count, word in enumerate(valid_word_numbers):
            occurrences = line.count(word)
            last_index = 0
            for _ in range(0, occurrences):
                index = line[last_index:].find(word)
                if index != -1:
                    number_positions.append([count+1, index + last_index])
                    last_index += index+1
        
        # Find postion of digit numbers
        for count, letter in enumerate(line):
            try:
                number_positions.append([int(letter), count])
            except:
                pass
        
        # Sort positions so the numbers are in order
        number_positions.sort(key=lambda x: x[1])
        numbers = [x[0] for x in number_positions]

        if len(numbers) > 0:
            final_calibration += int(f'{numbers[0]}{numbers[-1]}')
    return final_calibration


def trebuchet_2_clever(lines):
    valid_word_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    final_calibration = 0
    for line in lines:

        # Insert number as second letter of number word (e.g, o1ne, t2wo, t3hree)
        for count, word in enumerate(valid_word_numbers):
            line.replace(word, f'{word[1:]}{count+1}{word[1:]}')
        
        numbers = re.sub('[A-z]', '', line)
        if len(numbers) > 0:
            final_calibration += int(f'{numbers[0]}{numbers[-1]}')
    return final_calibration
    

if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    test_lines_2 = read_file("test_input_2.txt")
    assert (trebuchet(test_lines)) == 142
    assert (trebuchet_2(test_lines_2)) == 281

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {trebuchet(lines)}')
    print(f'Challenge 2 Answer: {trebuchet_2(lines)}')
    print(f'Challenge 2 (clever) Answer: {trebuchet_2(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
