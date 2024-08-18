def get_data(path):
    with open(path) as f:
        return [[int(word) if i == 1 else word for i,word in enumerate(line.split())] for line in f.read().splitlines() if line]
        
def determine_type(card):
    char_count = {i: card.count(i) for i in set(card)}
    counts = list(char_count.values())
    
    # 5 of a kind
    if 5 in counts:
        return "a"
    # 4 of a kind
    elif 4 in counts:
        return "b"
    # Full house
    elif 3 in counts and 2 in counts:
        return "c"
    # 3 of a kind
    elif 3 in counts:
        return "d"
    # 2 pairs
    elif counts.count(2) == 2:
        return "e"
    # 1 pair
    elif counts.count(2) == 1:
        return "f"
    #High card
    else:
        return "g"

def sort_by_type_and_label(data, label_sort_order, determine_type_fn):
    return sorted(
        data, key=lambda card: ( 
            determine_type_fn(card[0]),
            [label_sort_order.index(c) for c in card[0]], #returns a list of the indices of each of the word's chars in label_sort_order which python can sort normally
            )
        )

def part1(data):
    ranking = sort_by_type_and_label(data, "AKQJT98765432", determine_type)
    return sum([v[1]*(i+1) for i,v in enumerate(reversed(ranking))])

def determine_type_joker(card):
    char_count = {i: card.count(i) for i in set(card)}
    counts = list(char_count.values())

    # 5 of a kind
    if 5 in counts: #cannot be improved by J
        return "a"
    
    # 4 of a kind
    elif 4 in counts: 
        if "J" in char_count.keys():
            # becomes 5 of a kind
            return "a"
        else:
            return "b"
    
    # Full house
    elif 3 in counts and 2 in counts: 
        if "J" in char_count.keys():
            # becomes 5 of a kind
            return "a"
        else:
            return "c"
    
    # 3 of a kind
    elif 3 in counts: 
        if "J" in char_count.keys():
            # becomes 4 of a kind
            return "b"
        else:
            return "d"
    
    # 2 pairs
    elif counts.count(2) == 2: 
        if "J" in char_count.keys():
            if char_count["J"] == 2:
                #becomes 4 of a kind
                return "b"
            else:
                #becomes full house
                return "c"
        else:
            return "e"
    
    # 1 pair
    elif counts.count(2) == 1: 
        if "J" in char_count.keys(): 
            #becomes 3 of a kind
            return "d" 
        else:
            return "f"
    
    # High card
    else:
        if "J" in char_count.keys():
            #becomes 1 pair
            return "f"
        else:
            return "g"

def part2(data):
    ranking = sort_by_type_and_label(data, "AKQT98765432J", determine_type_joker)
    return sum([v[1]*(i+1) for i,v in enumerate(reversed(ranking))])

def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()