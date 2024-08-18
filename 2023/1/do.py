def get_data(path):
    with open(path) as f:
        return [section for section in f.read().split('\n')]

def part1(data):
    filtered = [''.join([word for word in line if word.isdigit()]) for line in data]
    return sum([int(line[0]+line[-1]) for line in filtered if line])

def get_word_indices(line):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    word_list = []
    for i,k in enumerate(digits):
        index = 0
        while index < len(line):
            index = line.find(k, index)
            if index == -1:
                break
            word_list.append((index, str(i+1)))
            index += len(k)
    return word_list

def get_number_indices(line):
    return [(ind, char) for (ind,char) in enumerate(line) if char.isdigit()]

def get_calibration_value(line):
    indices = get_word_indices(line) + get_number_indices(line)
    indices.sort(key=lambda x: x[0])
    return int(indices[0][1] + indices[-1][1])

def part2(data):
    return sum([get_calibration_value(line) for line in data])

def main():
    # PATH = "example_data.txt"
    # PATH = "example_data_part2.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))
    

if __name__ == "__main__":
    main()
