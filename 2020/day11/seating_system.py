from collections import Counter, defaultdict
import timeit

def read_file(filename):
    '''Returns a list of numbers (one on each line) in the file.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        rows = [line.strip() for line in lines]     
    return rows


def seating_system(seat_matrix, directional=False):
    seats_to_change = None
    while seats_to_change != []:
        seats_to_change = []
        for x, row in enumerate(seat_matrix):
            for y, column in enumerate(row):
                if column == "L" or column == "#":
                    adjacent_seats = get_adjacent_seats(seat_matrix, x, y, directional)
                    count_adjacent = Counter(adjacent_seats)
                    if column == "L" and count_adjacent['#'] == 0:
                        seats_to_change.append([x, y])
                    elif column == "#":
                        if directional:
                            if count_adjacent['#'] >= 5:
                                seats_to_change.append([x, y])
                        else:
                            if count_adjacent['#'] >= 4:
                                seats_to_change.append([x, y])
        for seat in seats_to_change:
            x, y = seat[0], seat[1]
            seat_val = seat_matrix[x][y]
            change_to = "#" if seat_val == "L" else "L"
            new_string = seat_matrix[x][:y] + change_to + seat_matrix[x][y+1:]
            seat_matrix[x] = new_string
    count_occupied = 0
    for row in seat_matrix:
        count_occupied += Counter(row)['#']
    return count_occupied
                    

def get_adjacent_seats(seat_matrix, x, y, directional):
    '''Find all adjacent seats to the seat at x,y in seat_matrix.'''
    adjacent_seats = []
    for x_val in range(x-1, x+2):
        for y_val in range(y-1, y+2):
            if not (x_val == x and y_val == y):
                if 0 <= x_val < len(seat_matrix) and 0 <= y_val < len(seat_matrix[x]):
                    if directional and (seat_matrix[x_val][y_val]) == ".":
                        value = check_for_dot(seat_matrix, x, y, [x_val-x, y_val-y])
                        if value is not None:
                            adjacent_seats.append(value)
                    else:
                        adjacent_seats.append(seat_matrix[x_val][y_val])
    return adjacent_seats



def check_for_dot(seat_matrix, x, y, change):
    '''Keep searching in specified direction vector (change) until a seat is found.'''
    change_x, change_y = change[0], change[1]
    while (0 <= (x+change_x) < len(seat_matrix) and 0 <= (y+change_y) < len(seat_matrix[x])):
        x += change_x
        y += change_y
        if seat_matrix[x][y] == ".":
            continue
        elif seat_matrix[x][y] != None:
            return seat_matrix[x][y]
        else:
            return None


if __name__ == "__main__":
    test_seat_matrix = read_file("test_input.txt")
    test_matrix_copy = test_seat_matrix.copy()
    assert seating_system(test_seat_matrix) == 37
    assert seating_system(test_matrix_copy, True) == 26

    seat_matrix = read_file("input.txt")
    seat_matrix_copy = seat_matrix.copy()
    start_time = timeit.default_timer()
    print("Challenge 1 Answer:", seating_system(seat_matrix))
    print("Challenge 2 Answer:", seating_system(seat_matrix_copy, True))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
