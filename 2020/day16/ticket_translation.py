from collections import defaultdict, Counter
import timeit

def read_file(filename):
    '''Returns the data parsed from the file.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        rules = {}
        nearby_tickets = []
        for count, line in enumerate(lines):
            if line.strip() == "":
                break
            number_range = line.strip().split(": ")[1].split(" or ")
            range_0 = number_range[0].split("-")
            range_1 = number_range[1].split("-")
            one_rule = [x for x in range(int(range_0[0]), int(range_0[1])+1)]
            one_rule.extend([x for x in range(int(range_1[0]), int(range_1[1])+1)])
            rules[line.strip().split(":")[0]] = one_rule
        your_ticket = [int(x) for x in lines[count+2].strip().split(",")]
        for line in lines[count+5:]:
            nearby_tickets.append([int(x) for x in line.strip().split(",")])
    return [rules, your_ticket, nearby_tickets]


def check_nearby_tickets(rules, nearby_tickets):
    '''Returns the sum of invalid fields and all the remaining valid tickets.'''
    invalid_count = 0
    valid_tickets = []
    for ticket in nearby_tickets:
        for field in ticket:
            for rule in rules.values():
                found = False
                if field in rule:
                    found = True
                    break
            if not found:
                invalid_count += field
                break
        if found:
            valid_tickets.append(ticket)
    return [invalid_count, valid_tickets]


def identify_fields(rules, valid_tickets, your_ticket):
    possible_fields = defaultdict(lambda: [])
    # Finds all possible positions for each field
    for k, v in rules.items():
        count = 0
        while count < len(valid_tickets[0]):
            valid = True
            for ticket in valid_tickets:
                if count <= len(valid_tickets[0])-1:
                    if ticket[count] not in v:
                        valid = False
                        break
            if valid:
                possible_fields[k].append(count)
            count += 1
    # Determines the final position for each field
    final_positions = determine_positions(possible_fields, len(valid_tickets[0]))
    # Multiplies all values in your_ticket which are in the position which
    # corresponds to keys with "departure" in their name
    total = 1
    for k, v in final_positions.items():
        if "departure" in k:
            total *= your_ticket[v]
    return total
            

def determine_positions(possible_fields, ticket_length):
    '''Returns a dict of final positions for each key.
    
    This is done by finding the key with only one possible position
    and working backwards, essentially removing this key from each
    position list and the finding the next one with only one possible
    position.
    '''
    final_positions = {}
    while len(final_positions) != ticket_length:
        for k, v in possible_fields.items():
            if len(v) == (1 + len(final_positions)):
                for item in v:
                    if item not in final_positions.values():
                        final_positions[k] = item
                        break
                continue
    return final_positions


if __name__ == '__main__':
    test_data = read_file("test_input.txt")
    test_nearby_tickets = check_nearby_tickets(test_data[0], test_data[2])
    assert test_nearby_tickets[0] == 71

    data = read_file("input.txt")
    start_time = timeit.default_timer()
    nearby_tickets = check_nearby_tickets(data[0], data[2])
    print("Challenge 1 Answer:", nearby_tickets[0])
    print("Challenge 2 Answer:", identify_fields(data[0], nearby_tickets[1], data[1]))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))
