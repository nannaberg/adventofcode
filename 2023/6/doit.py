from math import sqrt, ceil, floor


def get_data(path):
    with open(path) as f:
        return [line for line in f.read().splitlines() if line]
        return list(zip(*[[int(x) for x in word.split()[1:]] for word in f.read().splitlines() if word]))

def format_data_part1(data):
    return list(zip(*[[int(x) for x in line.split()[1:]] for line in data]))

def get_records(time, dist):
    records = 0
    for hold in range(time):
        travel_time = time-hold
        travel_dist = travel_time * hold
        if travel_dist > dist:
            records += 1
    return records

def part1(data):
    races = format_data_part1(data)
    all_records = 1
    for time,dist in races:
        records = get_records(time,dist)
        all_records *= records
    return all_records

def format_data_part2(data):
    return [int("".join(line.split()[1:])) for line in data]

#solution by finding roots of polynomial
def get_number_of_records(time, dist):
    # solve for x, (time-x) * x = dist + 1 <=> -x^2 + time*x - (dist + 1) = 0 
    # use quadratic formula, then round up x1, round down x2 (since we want ints, and the next travel_dist after dist is not just dist+1)
    x1 = ((-time) + sqrt(time**2 - 4*(-1)*(-(dist+1)))) / (2 * (-1))
    x2 = ((-time) - sqrt(time**2 - 4*(-1)*(-(dist+1)))) / (2 * (-1))
    return (floor(x2) - ceil(x1)) + 1

#iteration solution ok, but still slower than polynomial solution
# def get_first_record(time, dist):
#     for hold in range(time):
#         travel_time = time-hold
#         travel_dist = travel_time * hold
#         if travel_dist > dist:
#             return hold

# def get_last_record(time,dist):
#     for hold in reversed(range(time)):
#         travel_time = time-hold
#         travel_dist = travel_time * hold
#         if travel_dist > dist:
#             return hold

def part2(data):
    race = format_data_part2(data)
    time, dist = race
    number_of_records = get_number_of_records(time, dist)
    return number_of_records
    #iteration solutions (slower):
    # # records = get_records(time,dist)
    # first_record = get_first_record(time,dist)
    # last_record = get_last_record(time,dist)
    # return last_record - first_record + 1
    

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()