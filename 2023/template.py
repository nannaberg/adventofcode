def get_data(path):
    with open(path) as f:
        return [line for line in f.read().splitlines() if line]
    
def part1(data):
    return 0

def part2(data):
    return 0

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()