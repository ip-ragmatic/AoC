from helper import matrix_dict, sub_pts, add_pts, timeit
from itertools import combinations


TEST = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............\
"""


def sol1(matrix: dict[tuple[int], str], part2=False):
    freqs = set(matrix.values()) - {"."}
    antinodes_pos = set()
    for freq in freqs:
        freq_locs = (k for k, v in matrix.items() if v == freq)
        for p1, p2 in combinations(freq_locs, 2):
            slope = sub_pts(p2, p1)
            if part2:
                for pt, func in (p1, sub_pts), (p2, add_pts):
                    while pt in matrix:
                        antinodes_pos.add(pt)
                        pt = func(pt, slope)
            else:
                for pt in sub_pts(p1, slope), add_pts(p2, slope):
                    if pt in matrix:
                        antinodes_pos.add(pt)
    return len(antinodes_pos)


def day8(matrix, part2=False):
    return sol1(matrix, part2)


if __name__ == "__main__":
    # print(TEST)
    with open("puzzle_input/8.txt") as f:
        data = matrix_dict(f.read())
    # data = matrix_dict(TEST)
    timeit(day8, data)
    timeit(day8, data, True)

# part 1 answers:
#   - 293  (CORRECT)

# part 2  answers:
#   - 934  (CORRECT)
