from helper import digits, to_int_list, split_halves, timeit
from collections import defaultdict

TEST = "125 17"


def blink_transform1(data: list[int]):
    i = 0
    while i < len(data):
        num = data[i]
        if num == 0:
            data[i] = 1
        elif digits(num) % 2 == 0:
            left, right = split_halves(num)
            data[i] = left
            data.insert(i + 1, right)
            i += 2
            continue
        else:
            data[i] = num * 2024
        i += 1


def day11_brute(data: list[int], iterations: int):
    stones = data
    for i in range(iterations):
        blink_transform1(stones)
    return len(stones)


def blink_transform2(num: int) -> tuple[int] | tuple[int, int]:
    if num == 0:
        return 1,
    elif digits(num) % 2 == 0:
        return split_halves(num)
    return num * 2024,

def day11(data: list[int], iterations: int):
    stones = defaultdict(int)
    for n in data:
        stones[n] += 1
    for _ in range(iterations):
        new_stones = defaultdict(int)
        for key, count in stones.items():
            transform = blink_transform2(key)
            for stone in transform:
                new_stones[stone] += count
        stones = new_stones
    return sum(stones.values())

if __name__ == "__main__":
    with open("../puzzle_input/11.txt") as f:
        data = to_int_list(f.read())
    # data = to_int_list(TEST)
    # timeit(day11_brute, data, 25)
    timeit(day11, data, 25)
    timeit(day11, data, 75)

# part 1 answers:
#   - 220999  (CORRECT)
#       attempt 1: ~2.044172s
#       attempt 2: ~0.001410s

# part 2 answers:
#   - 
#       attempt 1: won't finish in human lifetime on this computer
#       attempt 2: ~0.059754s
