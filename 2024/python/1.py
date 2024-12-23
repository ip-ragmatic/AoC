from helper import timeit


def sum_distances(left: list, right: list):
    left.sort()
    right.sort()
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    return sum


def make_lists(path):
    left, right = [], []
    with open(path, "r") as f:
        line_list = f.readlines()
        for line in line_list:
            L, R = line.split("  ")
            left.append(int(L))
            right.append(int(R))
    return left, right


def similarity_score(left: list, right: list):
    score = 0
    for i in left:
        occurs = right.count(i)
        score += i * occurs
    return score


def day1(text_data):
    left, right = make_lists(text_data)
    return similarity_score(left, right)


if __name__ == "__main__":
    timeit(day1, "../puzzle_input/1.txt")
