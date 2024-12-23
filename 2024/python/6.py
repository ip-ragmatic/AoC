from helper import dirs, timeit


def to_matrix(text):
    return [list(line) for line in text.split()]


def print_map(patrol_map):
    print(*("".join(line) for line in patrol_map), sep="\n")


def turn_right(carat):
    order = list(dirs.keys())
    return order[(order.index(carat) + 1) % len(order)]


def find_carat(patrol_map):
    for i, row in enumerate(patrol_map):
        for j, obj in enumerate(row):
            if obj in dirs:
                return obj, (i, j)
    raise ValueError("Carat not found on patrol map.")


def move_carat(patrol_map, carat_state):
    if carat_state:
        carat, pos = carat_state
        next_pos = pos[0] + dirs[carat][0], pos[1] + dirs[carat][1]

        # if next position falls off map
        if not (0 <= next_pos[0] < len(patrol_map) and 0 <= next_pos[1] < len(patrol_map[0])):
            return None  # will conclude path simulation

        # if next position is obstacle
        if patrol_map[next_pos[0]][next_pos[1]] == "#":
            carat = turn_right(carat)
            return carat, pos

        # otherwise carat continues moving straight
        return carat, next_pos

    # if carat_state is None, it's already off the map
    return None


def detect_loop(patrol_map, carat_state):
    unique_pos = set()
    while carat_state:
        if carat_state in unique_pos:  # loop detected
            return True
        unique_pos.add(carat_state)
        carat_state = move_carat(patrol_map, carat_state)
    return False  # no loop detected


def init_loop_positions(patrol_map, carat_state):
    tested_pos = set()  # tracks positions that've been tested
    obstacles_pos = set()  # tracks positions where added obstacles init loops
    while carat_state:
        carat, pos = carat_state
        next_pos = pos[0] + dirs[carat][0], pos[1] + dirs[carat][1] 
        if (
            next_pos not in tested_pos  # ensures positions don't get counted multiple times
            and 0 <= next_pos[0] < len(patrol_map)
            and 0 <= next_pos[1] < len(patrol_map[0])
            and patrol_map[next_pos[0]][next_pos[1]] == "."
        ):
            tested_pos.add(next_pos)
            patrol_map[next_pos[0]][next_pos[1]] = "#"
            if detect_loop(patrol_map, carat_state):
                obstacles_pos.add(next_pos)
            patrol_map[next_pos[0]][next_pos[1]] = "."
        carat_state = move_carat(patrol_map, carat_state)
    return obstacles_pos


def part1(patrol_map):
    unique_pos = set()
    carat_state = find_carat(patrol_map)
    while carat_state:
        unique_pos.add(carat_state[1])
        carat_state = move_carat(patrol_map, carat_state)
    return len(unique_pos)


def part2(patrol_map):
    carat_state = find_carat(patrol_map)
    obstacle_pos = init_loop_positions(patrol_map, carat_state)
    return len(obstacle_pos)


if __name__ == "__main__":
    with open("../puzzle_input/6.txt") as f:
        patrol_map = to_matrix(f.read())
    timeit(part1, patrol_map)
    timeit(part2, patrol_map)

# part 1 answers:
#    - 5129  (CORRECT)

# part 2 answers:
#    - 1888  (CORRECT)
#         ~ sol 1: approx 9.4s
#         ~ sol 2: approx 4.9s (nice)
