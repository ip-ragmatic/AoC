from math import log10
import time
import re


#          up      down    left     right
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def timeit(func, *args):
    start = time.time()
    res = func(*args)
    end = time.time()
    print(f"Result = {res}")
    print(f"Execution time: {end - start:.6f}s")
    return res


def to_dict_matrix(text: str) -> dict[tuple[int, int], str]:
    matrix = {}
    for i, line in enumerate(text.split()):
        for j, item in enumerate(line):
            matrix[i, j] = item
    return matrix


def to_int_matrix(data: str):
    return [list(map(int, line)) for line in data.split()]


def to_str_matrix(data: str):
    return [list(line) for line in data.split()]


def to_int_list(text: str) -> list[int]:
    return list(map(int, text.split()))


def to_str_list(text: str) -> list[str]:
    return text.split()


def print_dict_matrix(data):
    max_row = max(coord[0] for coord in data.keys())
    max_col = max(coord[1] for coord in data.keys())
    
    for row in range(max_row + 1):
        line = ""
        for col in range(max_col + 1):
            line += data.get((row, col), ' ')
        print(line)


def print_list_matrix(data):
    print(*("".join(line) for line in data), sep="\n")


def add_pts(p1: tuple[int], p2: tuple[int]) -> tuple[int, int]:
    return p1[0] + p2[0], p1[1] + p2[1]


def sub_pts(p1: tuple[int], p2: tuple[int]) -> tuple[int, int]:
    return p1[0] - p2[0], p1[1] - p2[1]


def get_nums(text: str):
    res = re.findall(r"-?\d+", text)
    return tuple(map(int, res))


def digits(n: int) -> int:
    return int(log10(n)) + 1


def endswith(n: int, m: int) -> int:
    return (n - m) % (10 ** digits(m))


def split_halves(n: int) -> tuple[int, int]:
    n_digits = digits(n)
    assert n_digits % 2 == 0
    return divmod(n, 10 ** (n_digits // 2))
