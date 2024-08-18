import math

def get_data(path):
    with open(path) as f:
        return [word for word in f.read().splitlines() if word]

def is_part_number(candidate, all_symbols):
    number,i = candidate
    n = len(number)
    valid = False
    for si in all_symbols:
        if si >= i-1 and si <= i+n:
            valid = True
    return valid

def handle_line(line):
    numbers = []
    symbols = []
    current_number = ""
    for i,c in enumerate(line+"."):  #adding extra "." in case a number is last on the line
        if c.isdigit():
            current_number += c
        else:
            if current_number:
                numbers.append((current_number, i-len(current_number)))
                current_number = ""
            if c != ".":
                symbols.append(i)
    return numbers, symbols

def part1(data):
    part_numbers = []
    prev_symbols = []
    numbers, symbols = handle_line(data[0])
    next_numbers, next_symbols = handle_line(data[1])
    for line in data[2:]:
        for candidate in numbers:
            if is_part_number(candidate, prev_symbols+symbols+next_symbols):
                part_numbers.append(int(candidate[0]))
        prev_symbols = symbols
        symbols = next_symbols
        numbers = next_numbers
        next_numbers, next_symbols = handle_line(line)
    
    for candidate in numbers:
        if is_part_number(candidate, prev_symbols+symbols+next_symbols):
            part_numbers.append(int(candidate[0]))
    for candidate in next_numbers:
         if is_part_number(candidate, symbols+next_symbols):
            part_numbers.append(int(candidate[0]))
    return sum(part_numbers)


def handle_line2(line):
    numbers = []
    symbols = []
    current_number = ""
    for i,c in enumerate(line+"."):  #adding extra "." in case a number is last on the line
        if c.isdigit():
            current_number += c
        else:
            if current_number:
                numbers.append((current_number, i-len(current_number)))
                current_number = ""
            if c == "*":
                symbols.append(i)
    return numbers, symbols

def get_adjacent_numbers(candidate, all_numbers):
    adjacent_numbers = []
    # print(candidate, all_numbers)
    for number, ni in all_numbers:
        if candidate >= ni-1 and candidate <= ni+len(number):
            adjacent_numbers.append(int(number))
    return adjacent_numbers

def part2(data):
    gear_ratios = []
    prev_numbers = []
    numbers, symbols = handle_line2(data[0])
    next_numbers, next_symbols = handle_line2(data[1])
    for line in data[2:]:
        for candidate in symbols:
            adjacent_numbers = get_adjacent_numbers(candidate, prev_numbers+numbers+next_numbers)
            print(adjacent_numbers)
            if len(adjacent_numbers) == 2:
                gear_ratios.append(math.prod(adjacent_numbers))
        prev_numbers = numbers
        symbols = next_symbols
        numbers = next_numbers
        next_numbers, next_symbols = handle_line2(line)
    for candidate in symbols:
        adjacent_numbers = get_adjacent_numbers(candidate, prev_numbers+numbers+next_numbers)
        if len(adjacent_numbers) == 2:
            gear_ratios.append(math.prod(adjacent_numbers))
    for candidate in next_symbols:
        adjacent_numbers = get_adjacent_numbers(candidate, numbers+next_numbers)
        if len(adjacent_numbers) == 2:
            gear_ratios.append(math.prod(adjacent_numbers))
    return sum(gear_ratios)

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()

