from helper import timeit, get_nums


def parse(text: str):
    data = [get_nums(machine) for machine in text.strip().split("\n\n")]
    return data


def min_cost(system, p2):
    ax, ay, bx, by, x, y = system
    if p2:
        x += 10000000000000
        y += 10000000000000
    D = (ax * by) - (ay * bx)
    Da = (x * by) - (bx * y)
    Db = (ax * y) - (x * ay)
    a, a_rem = divmod(Da, D)
    b, b_rem = divmod(Db, D)
    if a_rem != 0 or b_rem != 0:
        return 0
    resx = (ax * a) + (bx * b)
    resy = (ay * a) + (by * b)
    if resx == x and resy == y:
        return int((3 * a) + b)
    return 0


def day13(text: str, p2=False):
    total = 0
    data = parse(text)
    for machine in data:
        cost = min_cost(machine, p2)
        total += cost
    return total


if __name__ == "__main__":
    with open("../puzzle_input/13.txt") as f:
        text = f.read()
    timeit(day13, text)
    timeit(day13, text, True)

# part 1 answers:
#   - 4963
#   - 38835
#   - 36870  (CORRECT)
#       attempt 1: ~0.001702s
#       attempt 2: ~0.000937s

# part 2 answers:
#   - 3513513513793
#   - 78101482023732
#       attempt 1: ~0.001543s
#       attempt 2: ~0.000889s
