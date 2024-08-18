import math
import time

def get_data(path):
    with open(path) as f:
        return [[line for line in segment.splitlines()] for segment in f.read().split("\n\n")]

def get_seed_maps(data):
    seed_maps = []
    seed_maps.append([int(number) for number in data[0][0][7:].split()])
    for d in data[1:]:
        m = [[int(number) for number in line.split()] for line in d[1:]]
        seed_maps.append(m) 
    return seed_maps

def get_new_number(number, map_numbers):
    for dst,src,n in map_numbers:
        if number >= src and number < src+n:
            diff = dst - src
            # print("diff: ", diff)
            return number + (diff)
    return number  

def get_locations(numbers, seed_maps):
    new_numbers = []
    for number in numbers:
        new_numbers.append(get_new_number(number, seed_maps[0]))
    if len(seed_maps) > 1:
        return get_locations(new_numbers, seed_maps[1:])
    else:
        return new_numbers

def part1(data):
    seed_maps = get_seed_maps(data)
    locations = get_locations(seed_maps[0], seed_maps[1:])
    return min(locations)

# def get_seeds(seed_pairs):
#     all_seeds = []
#     iter_seed_pairs = iter(seed_pairs)
#     for x in iter_seed_pairs:
#         all_seeds.extend(list(range(x, x+next(iter_seed_pairs))))
#     return all_seeds

def get_location(number, seed_maps):
    if len(seed_maps) > 1:
        new_number = get_new_number(number, seed_maps[0])
        return get_location(new_number, seed_maps[1:])
    else:
        return number

# src: 56, dst: 60, n: 37
# src: 93, dst: 

# def fix(seed, n):
#     if seed = n:
    
def non_recursive_get_location(seed, seed_maps):
    current_number = seed
    for m in seed_maps:
        new_number = get_new_number(current_number, m)
        current_number = new_number
    return new_number

def update_interval1(interval, map_next, new_intervals):
    # print("src map: ", interval)
    interval = [50,90,5]
    print("new_intervals: ", new_intervals)
    dst, src, n = interval
    # dst = 16 
    # src = 90
    # n = 5
    for i, (dst_next, src_next, n_next) in enumerate(map_next):
        # print("current: ", [dst, ])
        new_map_next = map_next
        print("next dst: {}, src: {}, n: {}".format(dst_next, src_next, n_next))
        #eg dst: [50,51], src_next: [15,51]
        if dst > src_next and dst+n == src_next+n_next:
            print("end of next")
            new1 = [dst_next+n_next-n, src, n]
            new2 = [dst_next, src_next, n_next-n]
            new_intervals.extend([new1, new2])
            return new_intervals
        #eg dst: [15,17], src_next: [15,51]
        elif dst == src_next and dst+n < src_next+n_next: 
            print("start of next")
            new1 = [dst_next, src, n]
            new2 = [dst_next+n, src_next+n, n_next-n]
            new_intervals.extend([new1, new2])
            return new_intervals
        #eg dst: [15,17], src_next: [15,17]
        elif dst == src_next and n == n_next:
            print("same as next")
            new = [src, dst_next, n]
            new_intervals.append(new)
            return new_intervals
        #eg dst: [16,20], src_next: [15,51]
        elif dst > src_next and dst+n < src_next+n_next-1: 
            print("contained inside next")
            n1 = dst-src_next
            new1 = [dst_next, src_next, n1]
            new2 = [dst_next+n1, src, n]
            n2 = n_next - n1 - n
            new3 = [dst_next+n1+n, src_next+n1+n, n2]
            new_intervals.extend([new1, new2, new3])
            return new_intervals
        #eg dst: [50,54], src_next: [15, 51]
        #eg [50,90,5] and [0,15,37] => [35,90,2], [0,15,35]
        #then recursively check leftover mapping [52, 92, 3] if it should be mapped further
        elif dst > src_next and dst+n > src_next+n_next:
            print("spilling over end of next")
            n1 = src_next+n_next-dst  #5-(54-51) = 2
            print("n1: ", n1)
            new1 = [dst_next+n_next-n1, src, n1]
            n2 = n_next - n1 #37-2 = 35
            new2 = [dst_next, src_next, n2]
            new_intervals.extend([new1, new2])
            n3 = n-n1   #5-2=3
            print("n3: ", n3)
            new3 = [dst+n1, src+n1, n3]
            print(new1)
            print(new2)
            print(new3)
            del(new_map_next, i)
            new_map_next.append(new2)
            return update_interval1(new3, new_map_next, new_intervals)
        #missing edge cases: eg [15,54], [15,51]
                           # eg other way around
    #when interval not part of or partially part of any intervals in map_next
        
    new_intervals.append(interval)
    return new_intervals


def update_interval(map, maps_next):
    dst, src, n = map
    for dst_next, src_next, n_next in maps_next:
        if dst > src_next and dst+n > src_next+n_next:
            n1 = src_next + n_next - dst
            new1 = [dst_next+n_next-n1, src, n1]
            n2 = n_next - n1
            new2 = [dst_next, src_next, n2]
            n3 = n-n1
            new3 = [dst+n1, src+n1, n3]

def test1():
    map = [50,90,5]
    map_next = [[0,15,37]]
    actual = update_map(map, map_next)
    expected = [[35,90,2], [52,92,3], [0,15,35]]
# def create_new_mapping(map1, map2):
#     new_mapping = []
#     for dst1, src1, n1 in map1:
#         for dst2, src2, n2 in map2:
            #not in any of the previous intervals
            

def part2(data):
    min_location = math.inf
    seed_maps = get_seed_maps(data)
    seeds = seed_maps[0]
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    to_soil = seed_maps[1]
    to_fer = seed_maps[2]

    new_intervals = update_interval(to_soil[0], [to_fer[0]], [])
    print(new_intervals)
    # create_new_mapping(to_soil, to_fer)
    # temp = 40000000
    # start, n = seed_pairs[0]
    # # print("start_seed: ", start)
    # # print("rounds: {}".format(n/step))
    # step = 1
    # current_location = non_recursive_get_location(start, seed_maps[1:])
    # for seed in range(start, start+n, step):
    #     # if seed % 100000 == 0:
    #     #     print("seed: {}, min_location: {}".format(seed, min_location))
    #         # print(min_location)
    #     # print("\n")
    #     # print("seed: ", seed)
    #     # min_location = seed
    #     # location = get_location(seed, seed_maps[1:])
    #     start = time.time()
    #     location = non_recursive_get_location(seed, seed_maps[1:])
    #     end = time.time()
    #     total = end-start
    #     print("total: {}, overall: {}".format(total, total*n))
    #     # abs_diff = abs(location - current_location)
    #     # print("abs diff: ", abs_diff)
    #     # if abs_diff != step:
    #     #     print("skipped important step")
    #     print("seed: {}, location: {}".format(seed, location))
    #     if location < min_location:
    #         min_location = location
    #         print("min location:", min_location)
        # current_location = location

   
    # for start, n in seed_pairs:
    #     print(start, n)
    #     count = 0
    #     for seed in range(seed_pairs[0][0], start+n):
    #         # if seed in numbers_seen:
    #         #     print(seed)
    #         #     break
    #         # else: 
    #         # numbers_seen.append(seed)
    #         location = get_location(seed, seed_maps[1:])
    #         print(location)
    #         if location < min_location:
    #             min_location = location
    #             count += 1
    #             print(min_location, count)
    #     print("\n")


    return min_location

def main():
    PATH = "example_data.txt"
    # PATH = "data.txt"
    data = get_data(PATH)
    # print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()