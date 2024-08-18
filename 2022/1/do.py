def get_data(path):
    with open(path) as f:
        return [[int(word) for word in section.split()] for section in f.read().split('\n\n')]

def part_one(inventories):
    max_cals = 0
    for inventory in inventories:
        cals = sum(inventory)
        if cals > max_cals:
            max_cals = cals
    return max_cals

def part_two(inventories):
    max_cals = [0,0,0]
    for inventory in inventories:
        cals = sum(inventory)
        min_cal = min(max_cals)
        if cals > min_cal:
            min_index = max_cals.index(min_cal)
            max_cals[min_index] = cals
    return sum(max_cals)

def main():
    PATH = "data_1.txt"
    inventories = get_data(PATH)
    print("Part 1 result: ", part_one(inventories))
    print("Part 2 result: ", part_two(inventories))

if __name__ == "__main__":
    main()


