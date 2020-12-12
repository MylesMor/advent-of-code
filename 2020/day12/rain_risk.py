import timeit

def read_file(filename):
    '''Returns a list of instructions from the file.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        instructions = [line.strip() for line in lines]            
    return instructions


def rain_risk(instructions):
    '''Returns Manhattan distance from start to end location after following instructions.'''
    current_pos = [90, 0, 0]
    for instruction in instructions:
        action = instruction[:1]
        amount = int(instruction[1:])
        if action == "N" or (action == "F" and current_pos[0] == 0):
            current_pos[1] += amount
            continue
        if action == "S" or (action == "F" and current_pos[0] == 180):
            current_pos[1] -= amount
            continue
        if action == "E" or (action == "F" and current_pos[0] == 90):
            current_pos[2] += amount
            continue
        if action == "W" or (action == "F" and current_pos[0] == 270):
            current_pos[2] -= amount
            continue
        if action == "R":
            new_direction = current_pos[0] + amount
            new_direction = new_direction - 360 if new_direction >= 360 else new_direction
            current_pos[0] = new_direction
            continue
        if action == "L":
            new_direction = current_pos[0] - amount
            new_direction = new_direction + 360 if new_direction < 0 else new_direction
            current_pos[0] = new_direction
            continue
    return abs(current_pos[1]) + abs(current_pos[2])


def rain_risk2(instructions):
    '''Returns Manhattan distance from start to end location after following instructions.'''
    current_pos = [90, 0, 0]
    relative_waypoint_pos = [0, 1, 10]
    for instruction in instructions:
        action = instruction[:1]
        amount = int(instruction[1:])
        if action == "N":
            relative_waypoint_pos[1] += amount
            continue
        if action == "S":
            relative_waypoint_pos[1] -= amount
            continue
        if action == "E":
            relative_waypoint_pos[2] += amount
            continue
        if action == "W":
            relative_waypoint_pos[2] -= amount
            continue
        if action == "F":
            current_pos[1] += amount * relative_waypoint_pos[1]
            current_pos[2] += amount * relative_waypoint_pos[2]
            continue
        if action == "R":
            new_direction = relative_waypoint_pos[0] + amount
            new_direction = new_direction - 360 if new_direction >= 360 else new_direction
            relative_waypoint_pos[0] = new_direction
        if action == "L":
            new_direction = relative_waypoint_pos[0] - amount
            new_direction = new_direction + 360 if new_direction < 0 else new_direction
            current_pos[0] = new_direction
        relative_waypoint_pos = rotate_waypoint(relative_waypoint_pos, int(amount / 90), action)
    return abs(current_pos[1]) + abs(current_pos[2])


def rotate_waypoint(waypoint_pos, times, direction):
    '''Rotates a position left or right 90 degrees a specified number of times.'''
    if direction == "R":
        for _ in range(times):
            value_to_copy = waypoint_pos[1]
            waypoint_pos[1] = -waypoint_pos[2]
            waypoint_pos[2] = value_to_copy
    elif direction == "L":
        for _ in range(times):
            value_to_copy = -waypoint_pos[1]
            waypoint_pos[1] = waypoint_pos[2]
            waypoint_pos[2] = value_to_copy
    return waypoint_pos


if __name__ == "__main__":
    test_instructions = read_file("test_input.txt")
    assert rain_risk(test_instructions) == 25
    assert rain_risk2(test_instructions) == 286
    
    start_time = timeit.default_timer()
    instructions = read_file("input.txt")
    print("Challenge 1 Answer: ", rain_risk(instructions))
    print("Challenge 1 Answer: ", rain_risk2(instructions))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))