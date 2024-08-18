import numpy as np

def get_data(path):
    with open(path) as f:
        return [[0 if word=="." else 1 for word in line] for line in f.read().splitlines() if line]

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def get_expanded_map(map):
    galaxy_indices = np.where(map==1)
    n = galaxy_indices[0].shape[0]
    map[galaxy_indices] = list(range(1,n+1))
    rows_with_all_zeros = np.where(~map.any(axis=1))[0]
    cols_with_all_zeros = np.where(~map.any(axis=0))[0]
    map = np.insert(map,rows_with_all_zeros,0, axis=0)
    map = np.insert(map,cols_with_all_zeros,0, axis=1)
    return map

def get_galaxy_indices(map):
    galaxy_indices = np.where(map!=0)
    return list(zip(galaxy_indices[0], galaxy_indices[1]))

def get_sum_shortest_paths(idxs):
    sum_shortest_paths = 0
    for i,a in enumerate(idxs[:-1]):
        for b in idxs[i+1:]:
            sum_shortest_paths += manhattan(a,b)
    return sum_shortest_paths

def part1(data):
    map = get_expanded_map(np.array(data))
    galaxy_indices = get_galaxy_indices(map)
    return get_sum_shortest_paths(galaxy_indices)
    

def get_map(map):
    galaxy_idxs = np.where(map==1)
    n = galaxy_idxs[0].shape[0]
    map[galaxy_idxs] = list(range(1,n+1))
    return map


def get_zeros_between_count(a_coord, b_coord, zeros):
    lo = min(a_coord, b_coord)
    hi = max(a_coord, b_coord)
    zeros_between = np.where((zeros > lo) & (zeros < hi))[0]
    return len(zeros_between)

def manhattan_expanded(a, b, zero_rows, zero_cols, factor):
    ay, ax = a
    by, bx = b
    zero_rows_between = get_zeros_between_count(ay, by, zero_rows)
    zero_cols_between = get_zeros_between_count(ax, bx, zero_cols)
    return sum(abs(val1-val2)+(zeros*(factor-1)) for val1, val2, zeros in zip(a,b,(zero_rows_between, zero_cols_between)))

def get_sum_shortest_paths_2(idxs, zero_rows, zero_cols, factor):
    sum_shortest_paths = 0
    for i,a in enumerate(idxs[:-1]):
        for b in idxs[i+1:]:
            sum_shortest_paths += manhattan_expanded(a,b, zero_rows, zero_cols, factor)
    return sum_shortest_paths

def part2(data):
    map = get_map(np.array(data))
    galaxy_indices = get_galaxy_indices(map)
    zero_rows = np.where(~map.any(axis=1))[0]
    zero_cols = np.where(~map.any(axis=0))[0]
    return get_sum_shortest_paths_2(galaxy_indices, zero_rows, zero_cols, 1000000)

def main():
    # PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()