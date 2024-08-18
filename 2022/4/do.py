def get_data(path):
    with open(path) as f:
        return [[translate_id(id) for id in section.split(",")] for section in f.read().splitlines()]

def translate_id(id):
    id_numbers = [int(i) for i in id.split("-") if i.isdigit()]
    return id_numbers

def is_contained(start_1, end_1, start_2, end_2):
    return start_1 <= start_2 and end_1 >= end_2

def is_contained_any(id_pair):
    f_start, f_end = id_pair[0][0], id_pair[0][1]
    s_start, s_end = id_pair[1][0], id_pair[1][1]
    return is_contained(f_start, f_end, s_start, s_end) or is_contained(s_start, s_end, f_start, f_end)

def part_one(data):
    total = 0
    for id_pair in data:
        if is_contained_any(id_pair):
            total += 1
    return total

def is_overlapping(id_pair):
    f_start, f_end = id_pair[0][0], id_pair[0][1]
    s_start, s_end = id_pair[1][0], id_pair[1][1]
    f_set = set(range(f_start, f_end+1))
    s_set = set(range(s_start, s_end+1))
    return  f_set.intersection(s_set)

def part_two(data):
    total = 0
    for id_pair in data:
        if is_overlapping(id_pair):
            total += 1
    return total

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part_one(data))
    print("Part 2 result: ", part_two(data))

if __name__ == "__main__":
    main()