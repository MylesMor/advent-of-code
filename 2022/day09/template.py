import timeit

def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        lines = [line.strip().split(" ") for line in file]
    return lines

def rope_bridge(lines, tail_size=1, track_tail=1):
    rope = [[0, 0] for _ in range(0, tail_size+1)]
    tail_positions = [rope[0][:]]
    
    for line in lines:
        direction, amount = line[0], int(line[1])

        # Move head
        for _ in range(1, amount+1):
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1

            # Move tail
            for i in range(1, tail_size+1):

                # Distance between rope parts
                distance = [abs(rope[i][0] - rope[i-1][0]), abs(rope[i][1] - rope[i-1][1])]

                # If tail part requires moving
                if max(distance) > 1:

                    # Move vertically
                    if (rope[i-1][0] == rope[i][0]):
                        rope[i][1] += 1 if rope[i-1][1] > rope[i][1] else -1
                    # Move horizontally
                    elif (rope[i-1][1] == rope[i][1]):
                        rope[i][0] += 1 if rope[i-1][0] > rope[i][0] else -1
                    # Move diagonally
                    else:
                        rope[i][0] += 1 if rope[i-1][0] > rope[i][0] else -1
                        rope[i][1] += 1 if rope[i-1][1] > rope[i][1] else -1

                    # If the tail part being tracked hasn't visited this position
                    # before, append it to the list
                    if rope[i] not in tail_positions and i == track_tail:
                        tail_positions.append(rope[i][:])

    return len(tail_positions)
        

if __name__ == "__main__":

    test_lines = read_file("test_input.txt")
    assert rope_bridge(test_lines) == 13
    assert rope_bridge(test_lines, 9, 9) == 1

    test_lines_2 = read_file("test_input_2.txt")
    assert rope_bridge(test_lines_2, 9, 9) == 36

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {rope_bridge(lines)}')
    print(f'Challenge 2 Answer: {rope_bridge(lines, 9, 9)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
