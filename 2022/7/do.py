def get_data(path):
    with open(path) as f:
        return [word for word in f.read().splitlines() if word]


def extract_dir(command):
    if command[:4] == "$ cd":
        return command[5:]
    else:
        return False


def extract_size(command):
    # print("extract size command: ", command)
    # file_size = int(''.join(c for c in command.split() if c.isdigit()))
    # print(file_size)
    # return file_size
    size_list = [int(c) for c in command.split() if c.isdigit()]
    if len(size_list) > 0:
        return size_list[0]
    else:
        return False


# def populate_dict(dir):


def get_dir_overview(data):
    all_dirs = []
    my_dict = {}
    current_dir = ""
    prev_dirs = []
    for i, d in enumerate(data):
        # print("command: ", d)
        # if i < 50:
        #     print(
        #         "{}: current_dir: {}, prev_dirs: {}".format(i + 1, current_dir, prev_dirs)
        #     )
        # print("prev_dirs", prev_dirs)
        dir = extract_dir(d)
        # print("extracted dir: ", dir)
        if dir == "..":
            prev_dir = prev_dirs.pop()
            # print("p_dir: ", prev_dir)
            # print("len p_dir: {}, len current_dir: {}".format(len(prev_dir), len(current_dir)))
            current_dir = current_dir[: len(current_dir) - (len(prev_dir) + 1)]
            # print("new current_dir after ..: ", current_dir)
        elif dir:
            if dir not in all_dirs:
                all_dirs.append(dir)
            current_dir += "-" + dir
            prev_dirs.append(dir)
            # print("new current dir after cd: ", current_dir)

        else:
            file_size = extract_size(d)
            if file_size:
                # print("file_size: ", file_size)
                if current_dir not in my_dict.keys():
                    my_dict[current_dir] = [file_size]
                    # print("curdir not in mydict: ", my_dict)
                else:
                    # print("alrady in dict")
                    new_file_sizes = my_dict[current_dir]
                    # print(new_file_sizes)
                    new_file_sizes.append(file_size)
                    my_dict[current_dir] = new_file_sizes
        # print(my_dict)

        # print("")
    return all_dirs, my_dict


def get_dirs_from_key(dict_key):
    dirs = [d for d in dict_key.split("-") if d]
    return dirs
    # print(dirs)


def get_total_dirs(all_dirs, dirs_overview):
    total_size = 0
    for dir in all_dirs:
        dir_size = 0
        for key in dirs_overview.keys():
            # print(key)
            # print(dir)
            # print(dir in key)
            # print("")
            dirs = get_dirs_from_key(key)
            print(dirs)
            if dir in dirs:
                dir_size += sum(dirs_overview[key])
        if dir_size <= 100000:
            total_size += dir_size
    return total_size


def part_one(data):
    all_dirs, dirs_overview = get_dir_overview(data)
    # print(all_dirs)
    # print(dirs_overview)
    # print("")
    for dir in all_dirs:
        print(dir)
    for k in dirs_overview.keys():
        print(k)
    # print(dirs_overview.keys())
    print("")
    total_size = get_total_dirs(all_dirs, dirs_overview)

    return total_size


def part_two(data):
    return 0


def main():
    PATH = "example_data.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", part_one(data))
    # print("Part 2 result: ", part_two(data))


if __name__ == "__main__":
    main()
