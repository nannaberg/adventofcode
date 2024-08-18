def get_data(path):
    with open(path) as f:
        return [section for section in f.read().splitlines()]

def get_priority(item):
    if item.islower():
        return ord(item)-96
    else:
        return ord(item)-38

def part_one(data):
    priority_sum = 0
    for rucksack in data:
        index = round(len(rucksack)/2)
        first = rucksack[:index]
        second = rucksack[index:]
        common = set(first).intersection(second)
        priority_sum += get_priority(next(iter(common)))
    return priority_sum
        
def part_two(data):
    step = 3
    priority_sum = 0
    for i in range(0,len(data), step):
        group = data[i:i+step]
        common = next(iter(set(group[0]).intersection(group[1]).intersection(group[2])))
        priority_sum += get_priority(common)
    return priority_sum

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part_one(data))
    print("Part 2 result: ", part_two(data))

if __name__ == "__main__":
    main()