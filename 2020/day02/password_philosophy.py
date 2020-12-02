def read_file(filename):
    '''Returns a list of lines from a file.'''
    with open(filename, "r") as file:
        password_dict = {}
        x = 0
        for line in file:
            password_dict[x] = {}
            split_at_spaces = line.rstrip().split(" ")
            password_dict[x]['number'] = split_at_spaces[0]
            password_dict[x]['character'] = split_at_spaces[1][:-1]
            password_dict[x]['password'] = split_at_spaces[2]
            x += 1
    return password_dict
    

def password_philosophy1(password_dict):
    '''Checks whether a character's count is between the minimum/maximum.'''
    count_valid_passwords = 0
    for key in password_dict.keys():
        numbers = password_dict[key]['number'].split("-")
        min_num, max_num = int(numbers[0]), int(numbers[1])
        number_of_occurrences = password_dict[key]['password'].count(password_dict[key]['character'])
        if number_of_occurrences >= min_num and number_of_occurrences <= max_num:
            count_valid_passwords += 1
    return count_valid_passwords


def password_philosophy2(password_dict):
    '''Checks whether a character is at only one of the required positions.'''
    count_valid_passwords = 0
    for key in password_dict.keys():
        numbers = password_dict[key]['number'].split("-")
        # Minus 1 from the positions as the indexing starts at 1 (rather than 0) in this exercise
        position_1, position_2 = int(numbers[0])-1, int(numbers[1])-1
        password = password_dict[key]['password']
        character = password_dict[key]['character']
        if password[position_1] == character and password[position_2] != character:
            count_valid_passwords += 1
            continue
        if password[position_2] == character and password[position_1] != character:
            count_valid_passwords += 1
    return count_valid_passwords



if __name__ == "__main__":
    password_dict = read_file("input.txt")
    print(password_philosophy1(password_dict))
    print(password_philosophy2(password_dict))

    