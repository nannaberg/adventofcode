def get_data(path):
    with open(path) as f:
        return [[int(word) for word in line.split()] for line in f.read().splitlines() if line]
    
def get_diffs(sequence):
    return [j-i for i,j in zip(sequence[:-1], sequence[1:])]

def get_next_value(sequence, index):
    if all(v == 0 for v in sequence):
        return 0
    else:
        diffs = get_diffs(sequence)
        if index < 0:
            return sequence[index] + get_next_value(diffs, index)
        else:
            return sequence[index] - get_next_value(diffs, index)

def part1(data):
    return sum([get_next_value(sequence, -1) for sequence in data])

def part2(data):
    return sum([get_next_value(sequence, 0) for sequence in data])

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()