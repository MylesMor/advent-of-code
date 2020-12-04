import re
import timeit

def read_file(filename):
    '''Returns a list of passport dictionaries.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        # Adds final newline character to retrieve last passport
        lines.append("\n")
        passport_list = []
        one_passport = ""
        for line in lines:
            if line != "\n":
                # Add the different lines of the passport together
                one_passport += line.replace("\n", " ")
                continue
            # Create dictionary of fields for each passport
            data_fields = one_passport[:-1].split(" ")
            passport_dict = {}
            for data in data_fields:
                data_split = data.split(":")
                passport_dict[data_split[0]] = data_split[1]
            passport_list.append(passport_dict)
            one_passport = ""
    return passport_list
    

def passport_processing(passports, validate_data):
    valid_passports = 0
    for passport in passports:
        if check_data(passport, validate_data):
            valid_passports += 1
    return valid_passports


def check_data(passport, validate_data):
    '''Validates a passport.

    Validates a invidivual passport - ensures the required fields are present and 
    optionally validates the data.

    Args:
        passport (dict): The passport to validate.
        validate_data (bool): True to validate the data, otherwise False.

    Returns:
        bool: True if valid passport, otherwise False.
    
    '''
    if len(passport) < 7:
        return False
    if len(passport) < 8 and "cid" in passport:
        return False
    if validate_data:
        if not re.match("^(19[2-9][0-9]|200[0-2])$", passport['byr']):
            return False
        if not re.match("^(201[0-9]|2020)$", passport['iyr']):
            return False
        if not re.match("^(202[0-9]|2030)$", passport['eyr']):
            return False
        if not re.match("^((1[5-8][0-9]|19[0-3])cm|(6[0-9]|59|7[0-6])in)$", passport['hgt']):
            return False
        if not re.match("^#[0-9a-f]{6}$", passport['hcl']):
            return False
        if not re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']):
            return False
        if not re.match("^[0-9]{9}$", passport['pid']):
            return False 
    return True


if __name__ == "__main__":
    start_time = timeit.default_timer()
    passports = read_file("input.txt")
    print("Challenge 1 Answer: " + str(passport_processing(passports, False)))
    print("Challenge 2 Answer: " + str(passport_processing(passports, True)))
    print("Time taken: %s" % (timeit.default_timer() - start_time))
