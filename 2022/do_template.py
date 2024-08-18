def get_data(path):
    with open(path) as f:
        return [word for word in f.read().splitlines() if word]
    
def part_one(data):
    return 0

def part_two(data):
    return 0

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part_one(data))
    print("Part 2 result: ", part_two(data))

if __name__ == "__main__":
    main()