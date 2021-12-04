import timeit
from anytree import Node, RenderTree


def read_file(filename):
    '''Returns the processed data from the file.'''
    with open(filename, "r") as file:
        rules_dict = {}
        lines = file.readlines()
        for count, line in enumerate(lines):
            if line !="\n":
                sections = line.strip().split(": ")
                if "|" in line:
                    rules_dict[int(sections[0])] = []
                    split_at_pipe = sections[1].split("|")
                    rules_dict[int(sections[0])].append([int(x.strip()) for x in split_at_pipe[0].strip().split(" ")])
                    rules_dict[int(sections[0])].append([int(x.strip()) for x in split_at_pipe[1].strip().split(" ")])
                elif "\"" in line:
                    rules_dict[int(sections[0])] = sections[1].replace("\"", "")
                else:
                    print(line)
                    rules_dict[int(sections[0])] = [int(x.strip()) for x in sections[1].split(" ")]
            else:
                message_list = [x.strip() for x in lines[count+1:]]
                break
        return rules_dict, message_list


def validate_messages(rules_dict, message_list):
    for message in message_list:
        print(check_rules(rules_dict, message, rules_dict[0]))
        break

def create_tree(rules):
    nodes = {}
    count = 0
    while True:
        value = rules[count]
        temp_count = count
        for item in value:
            if temp_count != 0:
                nodes[count] = Node(item, parent=temp_count)
            else:
                nodes[count] = Node(item)
            temp_count = item
    print(RenderTree(nodes[0]))


def evaluate_one(rules_dict, rule):
    rule = rules_dict[rule]
    for item in rule:

"""
def check_rules(rules_dict, message, rule_to_check):
    final_value = ""
    nodes = {}
    for rule in rule_to_check:
        if rules_dict[rule] == "a" or rules_dict[rule] == "b":
            final_value += rules_dict[rule]
        else:
            temp_value = ""
            for one_rule in rules_dict[rule]:
                print(one_rule)
                temp_value += check_rules(rules_dict, message, one_rule)[1]
                print("TEMP", temp_value)
            #final_list.append(final_value+temp_value)
            #print(final_list)
    print(final_value)
    return final_list, final_value
"""
        


if __name__ == "__main__":
    rules_dict, message_list = read_file("test_input.txt")
    print(rules_dict, message_list)
    create_tree(rules_dict)
    #validate_messages(rules_dict, message_list)