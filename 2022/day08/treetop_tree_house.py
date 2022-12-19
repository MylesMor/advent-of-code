import timeit

def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            lines.append([int(char) for char in line])
    return lines

def find_visible(grid):
    visible = [[0 for _ in x] for x in grid]

    for x in range(0,2):
        # Check rows when x = 1, and columns when x = 2
        for row in range(0, len(grid)):
            current_high = -1
            for column in range(0, len(grid)):
                if x == 0:
                    current_high = check_item(grid, row, column, current_high, visible)
                else:
                    current_high = check_item(grid, column, row, current_high, visible)
            current_high = -1
            for column in range(len(grid)-1, 0, -1):
                if x == 0:
                    current_high = check_item(grid, row, column, current_high, visible)
                else:
                    current_high = check_item(grid, column, row, current_high, visible)
    visible_trees = sum([sum(x) for x in visible])
    return visible_trees


def check_item(grid, row, column, current_high, visible):
    item = grid[row][column]
    if item > current_high:
        current_high = item
        visible[row][column] = 1
    return current_high


def best_tree_house(grid):
    scenic_scores = [[0 for _ in x] for x in grid]

    for row in range(1, len(grid)-1):
        for column in range(1, len(grid[row])-1):
            viewing_distance = 1
            position = grid[row][column]
            # Heading left
            for left in range(column-1, -1, -1):
                if grid[row][left] >= position:
                    viewing_distance *= column - left
                    break
                elif left == 0:
                    viewing_distance *= column - left
            # Heading right
            for right in range(column+1, len(grid[row]), 1):
                if grid[row][right] >= position:
                    viewing_distance *= right - column
                    break
                elif right == len(grid[row])-1:
                    viewing_distance *= right - column
            # Heading up
            for up in range(row-1, -1, -1):
                if grid[up][column] >= position:
                    viewing_distance *= row - up
                    break
                elif up == 0:
                    viewing_distance *= row - up
            # Heading down
            for down in range(row+1, len(grid), 1):
                if grid[down][column] >= position:
                    viewing_distance *= down - row
                    break
                elif down == len(grid)-1:
                    viewing_distance *= down - row
            scenic_scores[row][column] = viewing_distance
    return max([max(x) for x in scenic_scores])


if __name__ == "__main__":

    test_lines = read_file("test_input.txt")

    assert find_visible(test_lines) == 21
    assert best_tree_house(test_lines) == 8

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {find_visible(lines)}')
    print(f'Challenge 2 Answer: {best_tree_house(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
