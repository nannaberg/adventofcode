import matplotlib.path as mpltPath

def get_data(path):
    with open(path) as f:
        return [line for line in f.read().splitlines() if line]

def get_next_pipe(grid, prev_pipe, pipe):
    _, (prev_y, prev_x) = prev_pipe
    tile, (y,x) = pipe
    new_y = y
    new_x = x
    match tile:
        case "|":
            if prev_y < y:
                new_y += 1
            else:
                new_y -= 1
        case "-":
            if prev_x < x:
                new_x += 1 
            else:
                new_x -= 1 
        case "L":
            if prev_y < y:
                new_x += 1
            else:
                new_y -= 1
        case "J":
            if prev_y < y:
                new_x -= 1
            else:
                new_y -= 1
        case "7":
            if prev_x < x:
                new_y += 1
            else:
                new_x -= 1
        case "F":
            if prev_y > y:
                new_x += 1
            else:
                new_y += 1

    next_pipe = [grid[new_y][new_x], (new_y,new_x)]
    return next_pipe

def get_first_pipe_connected_to_s(grid, s_pos):
    y,x = s_pos
    if y > 0:
        new_y = y-1
        tile = grid[new_y][x]
        if tile in ["|", "7", "F"]:
            return [tile, (new_y, x)]
    #if there is a tile to the SOUTH:
    if y < len(grid)-1:
        new_y = y+1
        tile = grid[new_y][x]
        if tile in ["|", "L", "J"]:
            return [tile, (new_y, x)]
    #if there is a tile to the WEST:
    if x > 0:
        new_x = x-1
        tile = grid[y][new_x]
        if tile in ["-", "L", "F"]:
            return [tile, (y, new_x)]
    #if there is a tile to the EAST:
    if x < len(grid[0]) - 1:
        new_x = x+1
        tile = grid[y][new_x]
        if tile in ["-", "J", "7"]:
            return [tile, (y, new_x)]

def get_loop(grid, s_pos):
    loop = [s_pos]
    prev_pipe = ["S", s_pos]
    pipe = get_first_pipe_connected_to_s(grid, s_pos)
    while pipe[0] != "S":
        loop.append(pipe[1])
        next_pipe = get_next_pipe(grid, prev_pipe, pipe)
        prev_pipe = pipe
        pipe = next_pipe
    return loop

    
def part1(data):
    s_pos = next(((i, line.index("S")) 
                  for i, line in enumerate(data) 
                  if "S" in line))
    loop = get_loop(data, s_pos)
    max_dist = int(len(loop) / 2)
    return max_dist

def get_polygon_enclosed_area(loop, map_size):
    area = 0
    path = mpltPath.Path(loop)
    for i in range(map_size):
        for j in range(map_size):
            if (i,j) not in loop:
                if path.contains_point((i,j)):
                    area += 1
    return area

def part2(data):
    s_pos = next(((i, line.index("S")) 
                  for i, line in enumerate(data) 
                  if "S" in line))
    loop = get_loop(data, s_pos)
    return get_polygon_enclosed_area(loop, len(data))

def main():
    PATH = "example_data1.txt"
    # PATH = "example_data2.txt"
    PATH = "example_data3.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part1(data))
    print("Part 2 result: ", part2(data))

if __name__ == "__main__":
    main()