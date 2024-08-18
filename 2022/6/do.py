def get_data(path):
    with open(path) as f:
        return f.read()

def solution(data, n):
    for i in range(len(data)):
        if len(set(data[i:i+n])) == n:
            return i+n

def main():
    PATH = "example_data1.txt"
    PATH = "example_data2.txt"
    PATH = "example_data3.txt"
    PATH = "example_data4.txt"
    PATH = "example_data5.txt"
    PATH = "data.txt"
    data = get_data(PATH)
    print("Part 1 result: ", solution(data, 4))
    print("Part 2 result: ", solution(data, 14))

if __name__ == "__main__":
    main()