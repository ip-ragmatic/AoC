from helper import get_nums, timeit
from collections import defaultdict
from math import prod


ex1 = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def create_grid(w, h):
    grid = defaultdict(set)
    midx, midy = w // 2, h // 2
    for x in range(w):
        for y in range(h):
            pt = (x, y)
            if x < midx and y < midy:  # QI
                grid[1].add(pt)
            elif x > midx and y < midy:  # QII
                grid[2].add(pt)
            elif x < midx and y > midy:  # QIII
                grid[3].add(pt)
            elif x > midx and y > midy:  # QIV
                grid[4].add(pt)
    return grid


def move_bot(bot, w, h, t):
    xi, yi, vx, vy = bot
    dx, dy = vx * t, vy * t
    xf = (xi + dx) % w
    yf = (yi + dy) % h
    return xf, yf


def find_tree_time(text_data, w, h):
    bot_list = [get_nums(line) for line in text_data.strip().split("\n")]
    n_bots = len(bot_list)
    i = 1
    while True:
        unique = set()
        for bot in bot_list:
            pf = move_bot(bot, w, h, i)
            if pf not in unique:
                unique.add(pf)
        if len(unique) == n_bots:
            return i
        i += 1


def get_safety_factor(text_data, w, h, t):  # part 1 only
    bot_list = [get_nums(line) for line in text_data.strip().split("\n")]

    quads = create_grid(w, h)
    tracker = defaultdict(int)

    for i, bot in enumerate(bot_list):
        pf = move_bot(bot, w, h, t)
        bot_list[i] = (*pf, bot[2], bot[3])
        for Q, pts in quads.items():
            if pf in pts:
                tracker[Q] += 1
                break
    
    return prod(tracker.values())


def display_bots(text_data, w, h, t):
    bot_list = [get_nums(line) for line in text_data.strip().split("\n")]
    graph = [[" " for _ in range(w)] for _ in range(h)]
    for bot in bot_list:
        x, y = move_bot(bot, w, h, t)
        graph[y][x] = "$"
    print(*("".join(line) for line in graph), sep="\n")


if __name__ == "__main__":
    with open("../puzzle_input/14.txt") as f:
        text = f.read()
        w, h = 101, 103
    safety_factor = timeit(get_safety_factor, text, w, h, 100)
    tree_time = timeit(find_tree_time, text, w, h)
    display_bots(text, w, h, tree_time)


# part 1 answers:
#   - 549
#   - 232589280  (CORRECT)
#       attempt 1: ~0.003040s

# part 2 answers:
#   - 7569   (CORRECT)
#       attempt 1: ~0.819388s
