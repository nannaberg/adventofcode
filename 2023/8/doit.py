from math import lcm
import numpy as np


def get_data(path):
    with open(path) as f:
        return [line for line in f.read().splitlines() if line]


def get_node_map(nodes):
    node_map = {}
    for x, y in nodes:
        node_defs = [
            code.strip() for code in y.replace("(", "").replace(")", "").split(",")
        ]
        node_map[x] = {"L": node_defs[0], "R": node_defs[1]}
    return node_map


def reach_zzz(lrs, node_map):
    node = "AAA"
    count = 0
    lrs_len = len(lrs)
    while True:
        lrs_index = count % lrs_len
        side = lrs[lrs_index]
        node = node_map[node][side]
        count += 1
        if node == "ZZZ":
            break
    return count


def part1(data):
    lrs = data[0]
    nodes = [[x.strip() for x in line.split("=")] for line in data[1:]]
    node_map = get_node_map(nodes)
    counter = reach_zzz(lrs, node_map)
    print(node_map)
    return counter


def step(side, node_map, node):
    return node_map[node][side]


def is_last_z(node):
    return node[-1] == "Z"


def reach_all_z(lrs, start_nodes, node_map):
    lrs_len = len(lrs)
    count = 0
    new_nodes = start_nodes
    # if len(list(set(new_nodes))) != 6:
    #     print("not 6")
    seen = []
    while True:
        side = lrs[count % lrs_len]
        count += 1
        new_nodes = [step(side, node_map, x) for x in new_nodes]
        if len(list(set(new_nodes))) != 6:
            print(new_nodes)
        # else:
        #     print("hey")
        # if new_nodes not in seen:
        #     seen.append(new_nodes)
        # print(len(seen))
        if all(is_last_z(node) for node in new_nodes):
            break
    return count


def get_all_z_counts(lrs, node_map, start_node):
    zs = []
    z_counts = []
    count = 0
    lrs_len = len(lrs)
    node = start_node
    while True:
        side = lrs[count % lrs_len]
        node = node_map[node][side]
        count += 1
        if node[-1] == "Z":
            if node not in zs:
                z_counts.append(count)
                zs.append(node)
                count = 0
            else:
                break
    return z_counts


def get_start_nodes(node_map):
    start_nodes = []
    for k in node_map.keys():
        if k[-1] == "A":
            start_nodes.append(k)
    return start_nodes


def part2(data):
    lrs = data[0]
    nodes = [[x.strip() for x in line.split("=")] for line in data[1:]]
    node_map = get_node_map(nodes)
    start_nodes = get_start_nodes(node_map)
    z_counts = [get_all_z_counts(lrs, node_map, node) for node in start_nodes]
    count = np.lcm.reduce(np.array(z_counts))
    print(count)
    print(z_counts)


def main():
    PATH = "example_data1_1.txt"
    PATH = "example_data1_2.txt"
    PATH = "example_data2.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    # print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))


if __name__ == "__main__":
    main()
