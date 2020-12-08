import timeit
from collections import defaultdict


def read_file(filename):
    '''Returns a dictionary of bags and their inside bags.'''
    with open(filename, "r") as file:
        lines = file.readlines()
        bags_dict = defaultdict(lambda: [])
        for line in lines:
            bag = line.split(" bags contain ")
            if "no other" not in bag[1]:
                contained_bags = bag[1].replace(",", "").replace("bags", "bag").split("bag")
                stripped_bags = [bag.strip() for bag in contained_bags]
                bags_dict[bag[0]] = stripped_bags[:-1]
    return bags_dict


def handy_haversacks(bags, type_of_bag):
    final_bags = []
    for bag_to_find in type_of_bag:
        final_bags.extend([bag for bag in bags if bag_to_find in (inside_bag.split(" ", 1)[1] for inside_bag in bags[bag])])
    if len(final_bags) == 0:
        return final_bags
    return final_bags + (handy_haversacks(bags, final_bags))


def handy_haversacks2(bags, bag_dict):
    final_bags = defaultdict(lambda: 0)
    number_of_bags = 0
    for bag_to_find in bag_dict:
        for bag in bags:
            if bag_to_find in bag:
                for inside_bag in bags[bag]:
                    number_of_inside_bags = inside_bag.split(" ", 1)[0]
                    final_bags[inside_bag[2:]] += int(bag_dict[bag_to_find]) * int(number_of_inside_bags)
                    number_of_bags += int(bag_dict[bag_to_find]) * int(number_of_inside_bags)
    if len(final_bags) == 0:
        return number_of_bags
    return number_of_bags + handy_haversacks2(bags, final_bags)
    

if __name__ == "__main__":
    start_time = timeit.default_timer()
    bags = read_file("input.txt")
    print("Challenge 1 Answer:", len(set(handy_haversacks(bags, ["shiny gold"]))))
    print("Challenge 2 Answer:", handy_haversacks2(bags, {"shiny gold":1}))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))