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
        

def main():
    left, right = make_lists("puzzle_input/1.txt")
    sim_score = similarity_score(left, right)
    print(sim_score)


if __name__ == "__main__":
    main()
