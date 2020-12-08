import timeit

def read_file(filename):
    '''Returns a list of instructions in the file.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        instruction_list = [line.strip() for line in lines]            
    return instruction_list


def handheld_halting(instructions):
    '''Returns whether the program terminated and the accumalator after a set of instructions.

    Returns:
        tuple: (False, accumalator) before instruction is revisited if instructions cause an infinite loop, 
        otherwise (True, accumalator) if program successfuly terminates.
    '''
    visited = []
    accumalator = 0
    index = 0
    while True:
        if index in visited:
            return (False, accumalator)
        if len(instructions)-1 in visited:
            return (True, accumalator)
        operation, counter = instructions[index].split(" ")[0], int(instructions[index].split(" ")[1])
        visited.append(index)
        if operation == "nop":
            index += 1
            continue
        if operation == "jmp":
            index += counter
            continue
        if operation == "acc":
            index += 1
            accumalator += counter


def stop_loop(instructions):
    '''Swaps a jmp/nop instruction one-by-one until program terminates.'''
    for count, instruction in enumerate(instructions):
        new_instructions = instructions.copy()
        operation, counter = instruction.split(" ")[0], int(instruction.split(" ")[1])
        if operation == "jmp":
            new_instructions[count] = "nop " + str(counter)
            result = handheld_halting(new_instructions)
        elif operation == "nop":
            new_instructions[count] = "jmp " + str(counter)
            result = handheld_halting(new_instructions)
        else:
            continue
        if result[0]:
                return result[1]
                

if __name__ == "__main__":
    # Test cases
    test_instructions = read_file("test_input.txt")
    assert handheld_halting(test_instructions)[1] == 5
    assert stop_loop(test_instructions) == 8

    # Real input
    start_time = timeit.default_timer()
    instructions = read_file("input.txt")
    print("Challenge 1 Answer:", handheld_halting(instructions)[1])
    print("Challenge 2 Answer:", stop_loop(instructions))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))