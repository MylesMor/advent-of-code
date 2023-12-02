import timeit


def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file.readlines():
            line = line.split(": ")[1].strip()
            parts = line.split('; ')
            sets = []
            for part in parts:
                colour_dict = {}
                colours = part.split(', ')
                for colour in colours:
                    number_colours = colour.split(' ')
                    colour_dict[number_colours[1]] = int(number_colours[0])
                sets.append(colour_dict)
            lines.append(sets)  
    return lines


def cube_conundrum(lines):
    number_of_cubes = {
        "red": 12,
        "blue": 14,
        "green": 13
    }
    game_counter = 0
    for count, game in enumerate(lines):
        game_valid = True
        for set in game:
            for colour, number in set.items():
                if number > number_of_cubes[colour]:
                    game_valid = False
                    break 
            if not game_valid:
                break
        if game_valid:
            game_counter += (count+1)
    return game_counter


def cube_conundrum_2(lines):
    set_power = 0
    for game in lines:
        r, g, b = 0, 0, 0
        for set in game:
            if "red" in set.keys() and set['red'] > r:
                r = set['red']
            if "green" in set.keys() and set['green'] > g:
                g = set['green']
            if "blue" in set.keys() and set['blue'] > b:
                b = set['blue']
        set_power += r * g * b
    return set_power



if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert cube_conundrum(test_lines) == 8
    assert cube_conundrum_2(test_lines) == 2286

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {cube_conundrum(lines)}')
    print(f'Challenge 2 Answer: {cube_conundrum_2(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
