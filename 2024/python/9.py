from itertools import batched
from helper import timeit

TEST = "2333133121414131402"


def print_map(data: list):
    print("".join(map(str, data)))


def day9(diskmap: str, p2=False):
    expanded = []
    for file_id, (file_size, gap_size) in enumerate(
        batched([int(n) for n in diskmap + "0"], 2)
    ):
        if p2:  # makes a list[list[str]]
            expanded.append([file_id] * file_size)
            if gap_size > 0:
                expanded.append(["."] * gap_size)
        else:  # makes a list[str]
            expanded.extend([file_id] * file_size + ["."] * gap_size)

    if p2:
        j = len(expanded) - 1
        while j > 0:
            at_j = expanded[j]
            if "." in at_j:
                j -= 1
                continue
            for i in range(j):
                at_i = expanded[i]
                if "." not in at_i:
                    continue
                empty_idx = at_i.index(".")
                if len(at_j) <= len(at_i) - empty_idx:
                    at_i[empty_idx : empty_idx + len(at_j)] = at_j
                    expanded[j] = ["."] * len(at_j)
                    break
            j -= 1
        expanded = sum(expanded, [])
    else:
        i, j = 0, len(expanded) - 1
        while True:
            while expanded[i] != ".":
                i += 1
            while expanded[j] == ".":
                j -= 1
            if i >= j:
                break
            expanded[i], expanded[j] = expanded[j], expanded[i]

    # print_map(expanded)
    return sum(i * int(n) for i, n in enumerate(expanded) if isinstance(n, int))


if __name__ == "__main__":
    with open("puzzle_input/9.txt") as f:
        data = f.read()
    timeit(day9, data)
    timeit(day9, data, True)

# part 1 answers:
#   - 6301895872542  (CORRECT)
#       attempt 1: ~0.015029s

# part 2 answers:
#   - 6323761685944  (CORRECT)
#       attempt 1: ~7.067040s
