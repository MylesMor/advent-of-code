import timeit
import networkx as nx
from collections import defaultdict

def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            chars = []
            for char in line:
                chars.append(char)
            lines.append(chars)
    return lines


def switch_to_number(item):
    item = item[0]
    if item == 'S':
        return 0
    elif item == 'E':
        return 27
    return item


def calculate_shortest_path(lines):
    g = nx.DiGraph()
    items = defaultdict(lambda: 0)
    fixed_lines = []

    for row in lines:
        line = []
        for item in row:
            g.add_node(f'{item}{items[item]}')
            line.append(f'{item}{items[item]}')
            items[item] += 1
        fixed_lines.append(line)

    for y in range(0, len(fixed_lines)):
        for x in range(0, len(fixed_lines[y])):
            up = fixed_lines[y-1][x] if y-1 >= 0 else None
            down = fixed_lines[y+1][x] if y+1 < len(fixed_lines) else None
            left = fixed_lines[y][x-1] if x-1 >= 0 else None
            right = fixed_lines[y][x+1] if x+1 < len(fixed_lines[y]) else None
            directions = [up, down, left, right]
            for item in directions:
                if item is not None:
                    next_item_char = switch_to_number(item)
                    current_item_char = switch_to_number(fixed_lines[y][x])
                    next_item = ord(next_item_char)-96 if isinstance(next_item_char, str) else next_item_char
                    current_item = ord(current_item_char)-96 if isinstance(current_item_char, str) else current_item_char
                    if next_item-current_item <= 1:
                        g.add_edge(fixed_lines[y][x], item, weight=1)
    return nx.shortest_path_length(g, 'S0', 'E0')

if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert calculate_shortest_path(test_lines) == 31
    #assert (test_lines) == 4

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {calculate_shortest_path(lines)}')
    print(f'Challenge 2 Answer: {1}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
