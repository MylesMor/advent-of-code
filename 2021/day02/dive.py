import timeit 

def read_file(input):
    '''Reads the file and returns data in suitable format.'''
    data = []
    with open(input, "r") as file:
        for line in file:
            split_line = line.split(" ")
            if (split_line[0] == "up"):
                data.append({"depth": -int(split_line[1])})
            elif (split_line[0] == "down"):
                data.append({"depth": int(split_line[1])})
            elif (split_line[0] == "forward"):
                data.append({"forward": int(split_line[1])})
    return data


def calculate_final_position(data):
    position = {"forward": 0, "depth": 0}
    for instruction in data:
        for k, v in instruction.items():
            position[k] += v
    return position['forward'] * position['depth']


def calculate_final_position_with_aim(data):
    position = {"forward": 0, "depth": 0, "aim": 0}
    for instruction in data:
        for k, v in instruction.items():
            if k == "forward":
                position[k] += v
                position['depth'] += position['aim'] * v
            else:
                position['aim'] += v
    return position['forward'] * position['depth']


if __name__ == "__main__":
    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print(f'Challenge 1 Answer: {calculate_final_position(data)}')
    print(f'Challenge 2 Answer: {calculate_final_position_with_aim(data)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))