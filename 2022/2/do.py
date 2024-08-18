#part 1
#A, X: rock
#B, Y: paper
#C, Z: scissors
shape_score_dict_part_1 = {"X": 1, "Y": 2, "Z": 3}
outcome_score_dict_part_1 = {"A": {"Y": 6, "X": 3, "Z": 0}, "B": {"Z": 6, "Y": 3, "X": 0}, "C": {"X": 6, "Z": 3, "Y": 0}}

#part 2
#A: rock
#B: paper
#C: scissors
#X: lose
#Y: draw
#Z: win
choose_move_dict = {"A": {"Y": "A", "X": "C", "Z": "B"}, "B": {"Y": "B", "X": "A", "Z": "C"}, "C": {"Y": "C", "X": "B", "Z": "A"}}
shape_score_dict_part_2 = {"A": 1, "B": 2, "C": 3}
outcome_score_dict_part_2 = {"Y": 3, "X": 0, "Z": 6}


def get_data(path):
    with open(path) as f:
        return [tuple(section.split()) for section in f.read().splitlines()]
    
def get_score_part_1(moves):
    (opponent, me) = moves
    shape_score = shape_score_dict_part_1[me]
    outcome_score = outcome_score_dict_part_1[opponent][me]
    return shape_score + outcome_score

def part_one(rounds):
    total_score = 0
    for moves in rounds:
        total_score += get_score_part_1(moves)
    return total_score


def get_score_part_2(moves):
    (opponent, end) = moves
    my_move = choose_move_dict[opponent][end]
    shape_score = shape_score_dict_part_2[my_move]
    outcome_score = outcome_score_dict_part_2[end]
    return shape_score + outcome_score

def part_two(rounds):
    total_score = 0
    for moves in rounds:
        total_score += get_score_part_2(moves)
    return total_score


def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    rounds = get_data(PATH)

    print("Part 1 result: ", part_one(rounds))
    print("Part 2 result: ", part_two(rounds))

if __name__ == "__main__":
    main()


