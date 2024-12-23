from helper import timeit
from math import copysign


def parse_report(path):
    with open(path) as file:
        return [list(map(int, line.split())) for line in file]


def safe_p1(report: list):
    if len(report) < 2:
        return True
    ops = len(report) - 1
    incr_decr = 0
    for i in range(1, len(report)):
        step_diff = report[i] - report[i - 1]
        if not 1 <= abs(step_diff) <= 3:
            return False
        incr_decr += copysign(1, step_diff)
    return incr_decr == ops or incr_decr == -ops


def safe_p2(report: list[int]):
    if safe_p1(report):
        return True
    for i in range(len(report)):
        if safe_p1([report[j] for j in range(len(report)) if j != i]):
            return True
    return False


def day2(text_data):
    log = parse_report(text_data)
    return sum(safe_p2(report) for report in log)


def tests():
    def test_safe_p1():
        print(safe_p1([7, 6, 4, 2, 1]))
        print(safe_p1([1, 2, 7, 8, 9]))
        print(safe_p1([9, 7, 6, 2, 1]))
        print(safe_p1([1, 3, 2, 4, 5]))
        print(safe_p1([8, 6, 4, 4, 1]))
        print(safe_p1([1, 3, 6, 7, 9]))
        print(safe_p1([1, 1, 2, 3, 4]))
        print(safe_p1([2, 5, 4, 3, 2]))

    def test_safe_p2():
        print(safe_p2([7, 6, 4, 2, 1]))  # True
        print(safe_p2([1, 2, 7, 8, 9]))  # False
        print(safe_p2([9, 7, 6, 2, 1]))  # False
        print(safe_p2([1, 3, 2, 4, 5]))  # True
        print(safe_p2([8, 6, 4, 4, 1]))  # True
        print(safe_p2([1, 3, 6, 7, 9]))  # True
        print(safe_p2([1, 1, 2, 3, 4]))  # True
        print(safe_p2([2, 5, 4, 3, 2]))  # True

    test_safe_p1()
    print()
    test_safe_p2()


if __name__ == "__main__":
    timeit(day2, "../puzzle_input/2.txt")
