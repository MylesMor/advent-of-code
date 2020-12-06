import timeit

def read_file(filename):
    '''Returns a list of questions answered "yes".'''
    with open(filename, "r") as file:
        lines = file.readlines()
        # Adds final newline character to retrieve last group
        lines.append("\n")
        group_list = []
        one_group = ""
        for line in lines:
            if line != "\n":
                # Add the different lines of the group together
                one_group += line.replace("\n", " ")
                continue
            group_list.append(one_group)
            one_group = ""
    return group_list


def custom_customs1(groups):
    '''Returns the total number of "yes" questions excluding duplicates.'''
    return sum(len(set(group.replace(" ", ""))) for group in groups)


def custom_customs2(groups):
    '''Returns the number of questions where the whole group answered "yes".'''
    total_yes = 0
    for group in groups:
        individuals = group.split(" ")[:-1]
        if len(individuals) == 1:
            total_yes += len(individuals[0])
            continue
        else:
            individuals_sets = [set(individual) for individual in individuals]
            total_yes += len(set.intersection(*individuals_sets))
    return total_yes


if __name__ == "__main__":
    start_time = timeit.default_timer()
    groups = read_file("input.txt")
    print("Challenge 1 Answer:", custom_customs1(groups))
    print("Challenge 2 Answer:", custom_customs2(groups))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))