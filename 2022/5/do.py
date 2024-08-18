def get_data(path):
    with open(path) as f:
        return [word for word in f.read().splitlines() if word]

def get_crate_data(data):
    n = 4
    # creating list of lists with crate letters as elements, each list represents one layer of all the stacks
    tmp = [["".join(c for c in section[i:i+n] if c.isalpha()) for i in range(0, len(section), n)] for section in data]
    # transposing list of lists, so each list represents one stack of crates, then filtering out whitespace elements 
    return [list(filter(None, list(i)))[::-1] for i in zip(*tmp)]   

def get_move_data(data):
    return [[int(i) for i in section.split() if i.isdigit()] for section in data]
    
def move_crates_part_1(crate_data, move):
    amount = move[0]
    #from and to should be 0-indexed
    fr, to = [i-1 for i in move[1:]]
    #the crates we want are at the end of the list, reverse to get right order of crates
    crates = crate_data[fr][::-1][:amount]
    for crate in crates:
        crate_data[fr].pop()
        crate_data[to].append(crate)
    return crate_data
    

def get_split_index(data):
    for i,d in enumerate(data):
        if d[:2] == " 1":
            return i+1

def get_result(crate_data):
    return "".join(d[-1] for d in crate_data)

def part_one(data):
    split_index = get_split_index(data)
    crate_data = get_crate_data(data[:split_index])
    move_data = get_move_data(data[split_index:])
    for move in move_data:
        crate_data = move_crates_part_1(crate_data, move)
    
    return get_result(crate_data)

def move_crates_part_2(crate_data, move):
    amount = move[0]
    #from and to should be 0-indexed
    fr, to = [i-1 for i in move[1:]]
    #the crates we want are at the end of the list
    crates = crate_data[fr][-amount:]
    for _ in range(len(crates)):
        crate_data[fr].pop()
    crate_data[to].extend(crates)
    return crate_data

def part_two(data):
    split_index = get_split_index(data)
    crate_data = get_crate_data(data[:split_index])
    move_data = get_move_data(data[split_index:])
    for move in move_data:
        crate_data = move_crates_part_2(crate_data, move)
    
    return get_result(crate_data)

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part_one(data))
    print("Part 2 result: ", part_two(data))

if __name__ == "__main__":
    main()