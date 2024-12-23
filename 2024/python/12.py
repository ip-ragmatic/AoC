from helper import to_str_matrix, timeit, steps


def dfs_grouping(
    plot: list[list[str]],
    dimensions: tuple[int, int],
    cur_pt: tuple[int, int],
    plant: str,
    visited: set,
):
    rows, cols = dimensions
    cur_r, cur_c = cur_pt
    cur_region = set()
    if (
        cur_r < 0
        or cur_r >= rows
        or cur_c < 0
        or cur_c >= cols
        or plot[cur_r][cur_c] != plant
        or cur_pt in visited
    ):
        return cur_region
    visited.add(cur_pt)
    cur_region.add(cur_pt)
    for dr, dc in steps:
        next_pt = cur_r + dr, cur_c + dc
        cur_region |= dfs_grouping(plot, dimensions, next_pt, plant, visited)
    return cur_region


def get_boundary(
    region: set[tuple[int, int]],
) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    perimeter = set()
    for row, col in region:
        for dr, dc in steps:
            next_pt = row + dr, col + dc
            if next_pt not in region:
                perimeter.add(
                    ((row, col), next_pt)
                )  # coord on perimeter, external point. creates
                # a direction vector of the coord
    return perimeter


def get_sides(boundary: set[tuple[tuple[int, int], tuple[int, int]]]):
    orthog_surface_vecs = set()
    for pt1, pt2 in boundary:
        keep = True
        for dr, dc in [(1, 0), (0, 1)]:
            pt1_n = pt1[0] + dr, pt1[1] + dc
            pt2_n = pt2[0] + dr, pt2[1] + dc
            if (pt1_n, pt2_n) in boundary:
                keep = False
        if keep:
            orthog_surface_vecs.add(((pt1, pt2), (pt1_n, pt2_n)))
    return orthog_surface_vecs


def day12(text: str, p2=False):
    data = to_str_matrix(text)
    dimensions = len(data), len(data[0])
    total_cost = 0

    visited = set()
    for r, line in enumerate(data):
        for c, plant in enumerate(line):
            coord = (r, c)
            if coord not in visited:
                region = dfs_grouping(data, dimensions, coord, plant, visited)
                area = len(region)
                boundary = get_boundary(region)
                if p2:
                    sides = len(get_sides(boundary))
                    total_cost += area * sides
                    continue
                perimeter = len(boundary)
                total_cost += area * perimeter
    return total_cost


if __name__ == "__main__":
    with open("../puzzle_input/12.txt") as f:
        text = f.read()
    timeit(day12, text)
    timeit(day12, text, True)


# part 1 answers:
#   - 1485656  (CORRECT)
#       attempt 1 ~0.042113s
#       attempt 2 ~0.040747s  (cleanup of attempt 1)
#       attempt 3 ~0.039707s  (cleanup of attempt 2)

# part 2 answers:
#   - 899196   (CORRECT)
#       attempt 1 ~0.045123s
