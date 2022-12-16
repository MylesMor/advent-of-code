import timeit

map = {
    "A": "1",
    "B": "2",
    "C": "3",
    "X": "1",
    "Y": "2",
    "Z": "3",
}

def read_file(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            translation_table = line.maketrans(map)
            lines.append([int(i) for i in line.translate(translation_table).split(" ")])
    return lines


def rock_paper_scissors(lines):
    score = 0
    score += sum([line[1] + determine_result(line[0], line[1]) for line in lines])
    return score


def determine_result(opponent, player):
    # DRAW
    if opponent == player:
        return 3
    # WIN
    elif player == opponent+1 or player == (opponent + 1) % 3:
        return 6
    # LOSE
    else:
        return 0


def rock_paper_scissors_2(lines):
    score = 0
    for line in lines:
        opponent = line[0]
        result = line[1]
        # LOSE
        if (result == 1):
            player = opponent - 1 if opponent > 1 else 3
            score += player + determine_result(opponent, player)
        # DRAW
        elif (result == 2):
            score += opponent + determine_result(opponent, opponent)
        # WIN
        else: 
            player = opponent + 1 if opponent < 3 else 1
            score += player + determine_result(opponent, player)
    return score


if __name__ == "__main__":
    
    test_lines = read_file("test_input.txt")
    assert rock_paper_scissors(test_lines) == 15
    assert rock_paper_scissors_2(test_lines) == 12

    start_time = timeit.default_timer()
    lines = read_file("input.txt")
    print(f'Challenge 1 Answer: {rock_paper_scissors(lines)}')
    print(f'Challenge 2 Answer: {rock_paper_scissors_2(lines)}')
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
