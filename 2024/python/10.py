from helper import timeit


TEST = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split()

#           up,    down    left     right
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(
    topomap: list[str], cur_pt: tuple[int, int], visited: set[tuple[int, int]], p2=False
):
    rows, cols = len(topomap), len(topomap[0])
    cur_r, cur_c = cur_pt

    if p2:
        if cur_r < 0 or cur_r >= rows or cur_c < 0 or cur_c >= cols:
            return 0
    else:
        if (
            cur_r < 0
            or cur_r >= rows
            or cur_c < 0
            or cur_c >= cols
            or cur_pt in visited
        ):
            return 0
    visited.add(cur_pt)

    if topomap[cur_r][cur_c] == "9":
        return 1

    counter = 0
    for dr, dc in steps:
        next_r, next_c = cur_r + dr, cur_c + dc
        if (
            0 <= next_r < rows
            and 0 <= next_c < cols
            and int(topomap[next_r][next_c]) - int(topomap[cur_r][cur_c]) == 1
        ):
            next_pt = next_r, next_c
            counter += dfs(topomap, next_pt, visited, p2)
    return counter


def sol1(topomap, p2=False):
    result = 0
    for r, line in enumerate(topomap):
        for c, elev in enumerate(line):
            if elev == "0":
                trailhead = r, c
                visited_pts = set()
                result += dfs(topomap, trailhead, visited_pts, p2)
    return result


if __name__ == "__main__":
    with open("puzzle_input/10.txt") as f:
        data = f.read().split()
    timeit(sol1, data)  # part 1
    timeit(sol1, data, True)  # part 2

# part 1 answers:
#   - 760  (CORRECT)
#       attempt 1 w/ DFS: ~0.005734s
#       attempt 2 w/ DFS: ~0.005433s

# part 2 answers:
#   - 1764 (CORRECT)
#       attempt 1 w/ DFS: ~0.007338s
