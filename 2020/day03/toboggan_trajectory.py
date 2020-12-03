def read_file(filename):
    '''Returns a list of lines from a file.'''
    with open(filename, "r") as file:
        rows = [line.rstrip() for line in file]
    return rows

def toboggan_trajectory(rows, right, down):
    '''Returns the number of trees encountered on a map with a specified slope.'''
    currentPosRight, currentPosDown = 0, 0
    num_trees = 0
    for row in rows:
        currentPosDown += down
        currentPosRight += right
        # If the end of a row has been reached
        if (currentPosRight+1 > len(row)):
            # Carry the remainder of the counter over to the start of a new row
            currentPosRight = abs(currentPosRight - len(row))
        # Break if end of the rows array has been reached
        if (currentPosDown+1 > len(rows)):
            break
        if rows[currentPosDown][currentPosRight] == "#":
            num_trees += 1
    return num_trees


if __name__ == "__main__":
    rows = read_file("input.txt")
    # Part 1
    slope_3_1 = toboggan_trajectory(rows, 3, 1)
    print("Part 1 Answer:", slope_3_1)
    # Part 2
    slope_1_1 = toboggan_trajectory(rows, 1, 1)
    slope_5_1 = toboggan_trajectory(rows, 5, 1)
    slope_7_1 = toboggan_trajectory(rows, 7, 1)
    slope_1_2 = toboggan_trajectory(rows, 1, 2)
    print("Part 2 Answer:", slope_1_1 * slope_3_1 * slope_5_1 * slope_7_1 * slope_1_2)

    