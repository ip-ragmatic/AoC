from helper import to_str_matrix, timeit, dirs, print_list_matrix
from collections import deque

ex1 = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


ex2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""


ex3 = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""


def parse(text_data):
    _map, steps = text_data.strip().split("\n\n")
    return to_str_matrix(_map), "".join(steps.split("\n"))


def find_bot(_map):
    for r, row in enumerate(_map):
        for c, item in enumerate(row):
            if item == "@":
                return r, c


############################## PART 1 ##############################
def moveable_p1(_map, r, c, dr, dc):
    objects = [(r, c)]
    while True:
        r += dr
        c += dc
        if not (0 <= r < len(_map) and 0 <= c < len(_map[0])) or _map[r][c] == "#":
            return False, []
        objects.append((r, c))
        if _map[r][c] == ".":
            return True, objects


def shift_p1(_map, involved):
    for i in range(len(involved) - 1, 0, -1):
        r1, c1 = involved[i]
        r2, c2 = involved[i - 1]
        _map[r1][c1], _map[r2][c2] = _map[r2][c2], _map[r1][c1]


def part1(text_data):
    val = 0
    _map, bot_dirs = parse(text_data)
    bot = find_bot(_map)
    for step in bot_dirs:
        r, c = bot
        dr, dc = dirs[step]
        move, involved = moveable_p1(_map, r, c, dr, dc)
        if move:
            shift_p1(_map, involved)
            bot = involved[1]
    for r, line in enumerate(_map):
        for c, item in enumerate(line):
            if item == "O":
                val += 100 * r + c
    return val


####################################################################


############################## PART 2 ##############################
def double_width(_map):
    new_map = []
    for r, line in enumerate(_map):
        new_line = []
        for item in line:
            if item == "#":
                new_line.extend(item * 2)
            elif item == "O":
                new_line.extend(["[", "]"])
            elif item == ".":
                new_line.extend(item * 2)
            else:
                new_line.extend(["@", "."])
        new_map.append(new_line)
    return new_map


def moveable_p2(_map, r, c, dr, dc):
    objects = []
    visited = set()
    queue = deque([(r, c)])

    while queue:
        nr, nc = queue.popleft()

        if (
            (nr, nc) in visited
            or _map[nr][nc] == "#"
            or not (0 <= nr < len(_map) and 0 <= nc < len(_map[0]))
        ):
            # return False, []
            continue

        visited.add((nr, nc))
        r_idx = abs(nr - r)
        if r_idx >= len(objects):
            objects.append([])
        objects[r_idx].append((nr, nc))

        if _map[nr][nc] == ".":
            continue

        if _map[nr][nc] == "[":
            pair = (nr, nc), (nr, nc + 1)
        elif _map[nr][nc] == "]":
            pair = (nr, nc), (nr, nc - 1)
        elif _map[nr][nc] == "@":
            pair = [(nr, nc)]
        for b in pair:
            if (b[0] + dr, b[1] + dc) not in visited:
                queue.append((b[0] + dr, b[1] + dc))

    for row in objects:
        for r, c in row:
            if _map[r][c] == "#":
                return False, []
    return True, objects


def shift_p2(
    _map, involved, dr, dc
):  # dr and dc here are going to be steps in the direction
    # opposite to the one taken in the traversal
    for row in reversed(involved):
        for r, c in reversed(row):
            br, bc = r - dr, c - dc  # reads "behind r" and "behind c"
            _map[r][c], _map[br][bc] = _map[br][bc], _map[r][c]


def part2(text_data):
    val = 0
    old, bot_dirs = parse(text_data)
    _map = double_width(old)
    bot = find_bot(_map)
    for step in bot_dirs:
        print_list_matrix(_map)
        print(step)
        r, c = bot
        dr, dc = dirs[step]
        move, involved = moveable_p2(_map, r, c, dr, dc)
        print(*involved)
        if move:
            shift_p2(_map, involved, dr, dc)
            bot = r + dr, c + dc
        print()
    # print_list_matrix(_map)
    # print(step)
    return val


####################################################################

if __name__ == "__main__":
    with open("../puzzle_input/15.txt") as f:
        text_data = f.read()
    # timeit(part1, text_data)
    # timeit(part2, text_data)
    # timeit(part2, ex1)
    timeit(part2, ex3)

# part 1 answers:
#   - 1509074  (CORRECT)
#       attempt 1: ~0.582104s  (used dict matrix)
#       attempt 2: ~0.012920s  (reassigned bot position used index 1 of involved list)
#       attempt 3: ~0.009848s  (changed matrix representation to a 2D list instead of a dict)

# part 2 answers:
#   -
