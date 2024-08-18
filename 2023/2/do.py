import math

def handle_subset(subset):
    i = subset.find(" ")
    return (subset[i+1:], int(subset[:i]))

def make_dict(cube_set):
    pairs = [handle_subset(subset.strip()) for subset in cube_set.split(",")]
    return dict((k,v) for k,v, in pairs)

def handle_line(line):
    game_dicts = [make_dict(cube_set) for cube_set in line[line.find(":")+2:].split(";")]
    return game_dicts

def get_data(path):
    with open(path) as f:
        return [handle_line(line) for line in f.read().split('\n')]

def is_possible(game):
    bag_contents = {"red": 12, "green": 13, "blue": 14}
    for cube_set in game:
        for k,v in cube_set.items():
            if v > bag_contents[k]:
                return False
    return True

def part1(games):
    id_sum = 0
    for i,game in enumerate(games):
        if is_possible(game):
            id_sum += i+1
    return id_sum


def get_minimal_power(game):
    min_cubes = {"red": 0, "blue": 0, "green": 0}
    for cube_set in game:
        for k,v in cube_set.items():
            if v > min_cubes[k]:
                min_cubes[k] = v
    return math.prod(min_cubes.values())

def part2(games):
    return sum([get_minimal_power(game) for game in games])

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))
    

if __name__ == "__main__":
    main()

