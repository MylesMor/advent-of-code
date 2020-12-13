import timeit

def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        earliest_time = int(lines[0].strip())
        bus_list = lines[1].strip().replace("x", "-1").split(",")
        bus_list = [int(bus) for bus in bus_list]
    return [earliest_time, bus_list]


def shuttle_search(earliest_time, bus_list):
    departure_differences = {}
    for bus in bus_list:
        if bus != -1:
            how_long_to_bus = bus - (earliest_time % bus)
            departure_differences[bus] = how_long_to_bus
    next_bus = min(departure_differences, key=departure_differences.get)
    return next_bus * departure_differences[next_bus] 


def shuttle_search2(bus_list):
    offset, period = 0, bus_list[0]
    for count in range(1, len(bus_list)):
        if bus_list[count] != -1:
            bus_id = bus_list[count]
            index = bus_list.index(bus_list[count])
            while (offset + index) % bus_id != 0:
                offset += period
            period *= bus_id
    return offset  
    


if __name__ == "__main__":
    test_data = read_file("test_input.txt")
    assert shuttle_search(test_data[0], test_data[1]) == 295
    assert shuttle_search2(test_data[1]) == 1068781

    start_time = timeit.default_timer()
    data = read_file("input.txt")
    print("Challenge 1 Answer:", shuttle_search(data[0], data[1]))
    print("Challenge 2 Answer:", shuttle_search2(data[1]))
    print("Time taken: %s" % (round(timeit.default_timer() - start_time, 8)))