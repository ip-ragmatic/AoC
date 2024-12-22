from helper import dirs, timeit, to_dict_matrix

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


def parse(text_data):
    _map, steps = text_data.strip().split("\n\n")
    return to_dict_matrix(_map), "".join(steps.strip().split())


def find_bot(_map):
    for k, v in _map.items():
        if v == "@":
            return k


def moveable(_map, r, c, dr, dc, objects):
    objects.append((r, c))
    pt_n = r + dr, c + dc
    if (
        pt_n not in _map or _map[pt_n] == "#"
    ):
        return False
    if _map[pt_n] == ".":
        objects.append(pt_n)
        return True
    return moveable(_map, pt_n[0], pt_n[1], dr, dc, objects)


def move_bot(_map, involved):
    for i in range(len(involved) - 1, 0, -1):
        _map[involved[i]], _map[involved[i - 1]] = _map[involved[i - 1]], _map[involved[i]]


def part1(text_data):
    val = 0
    _map, bot_dirs = parse(text_data)
    bot = find_bot(_map)
    for step in bot_dirs:
        r, c = bot
        dr, dc = dirs[step]
        involved = []
        move = moveable(_map, r, c, dr, dc, involved)
        if move:
            move_bot(_map, involved)
            bot = involved[1]
    for k, v in _map.items():
        if v == "O":
            r, c = k
            val += 100 * r + c
    return val


if __name__ == "__main__":
    with open("puzzle_input/15.txt") as f:
        text_data = f.read()
    timeit(part1, text_data)

