

def get_data(path):
    with open(path) as f:
        return [line.split(":")[1] for line in f.read().splitlines() if line]

def get_cards(data):
    return [[numbers.split() for numbers in line.split("|")] for line in data]

def get_common(x,y):
    return set(x).intersection(set(y))

def part1(data):
    cards = get_cards(data)
    wins = []
    for x,y in cards:
        common = get_common(x,y)
        if common:
            score = 2**(len(common)-1)
            wins.append(score)
    return sum(wins)

def part2(data):
    cards = get_cards(data)
    total = [1] * len(cards)
    for i,(x,y) in enumerate(cards):
        common = len(get_common(x,y))
        start = i+1
        end = start + common
        total[start:end] = [v+total[i] for v in total[start:end]]
    return sum(total)

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()