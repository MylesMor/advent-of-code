import timeit

def read_file(filename):
    '''Returns a list of lines.'''
    with open(filename, "r") as file:
        lines = [line for line in file.readlines()]
    return lines


def binary_boarding(instructions, number_of_rows, number_of_columns):
    '''Identifies the seat number from a list of instructions.'''
    seat_ids = []
    for line in instructions:
        max_number_rows, max_number_cols = number_of_rows, number_of_columns
        min_number_rows, min_number_cols = 0, 0
        for letter in line:
            if letter == "F":
                max_number_rows -= (max_number_rows-min_number_rows) / 2
            elif letter == "B":
                min_number_rows += (max_number_rows-min_number_rows) / 2
            elif letter == "L":
                max_number_cols -= (max_number_cols-min_number_cols) / 2
            elif letter == "R":
                min_number_cols += (max_number_cols-min_number_cols) / 2
        seat_ids.append(int((min_number_rows * 8) + min_number_cols))
    return seat_ids


def find_my_seat(seat_ids):
    '''Returns the missing number (that is not +1 from the last) in the list.'''
    sorted_seat_ids = sorted(seat_ids)
    for seat in range(0, len(sorted_seat_ids)-2):
        if sorted_seat_ids[seat]+1 != sorted_seat_ids[seat+1]:
            return sorted_seat_ids[seat]+1


if __name__ == "__main__":
    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    seat_ids = binary_boarding(lines, 128, 8)
    print("Challenge 1 Answer:", max(seat_ids))
    print("Challenge 2 Answer:", find_my_seat(seat_ids))
    print("Time taken: %s" % (timeit.default_timer() - start_time))
    
            
            
