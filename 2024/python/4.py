import re

TEST = r"""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".split()
XMAS = re.compile(r"(?=(XMAS|SAMX))")
MAS = re.compile(r"(?=(MAS|SAM))")


def parse_text(path):
    with open(path) as file:
        return file.read().split("\n")


def get_count(text: str, pattern: re.Pattern):
    return len(pattern.findall(text))


def x_mas_check(mtrx, i, j):
    right = "".join(mtrx[i - 1][j - 1] + mtrx[i][j] + mtrx[i + 1][j + 1])
    left = "".join(mtrx[i - 1][j + 1] + mtrx[i][j] + mtrx[i + 1][j - 1])
    return bool(MAS.findall(right) and MAS.findall(left))


def xmas_count_p1(mtrx: list[str]):
    rows, cols = len(mtrx), len(mtrx[0])
    count = 0

    # horizontal
    for row in mtrx:
        count += get_count(row, XMAS)

    # vertical
    for col in range(cols):
        flat_col = "".join([mtrx[row][col] for row in range(rows)])
        count += get_count(flat_col, XMAS)

    # down right
    for d in range(-(rows - 1), cols):
        right_diag = "".join([
            mtrx[i][j] for i in range(rows) for j in range(cols) if j - i == d
        ])
        count += get_count(right_diag, XMAS)

    # down left
    for s in range(rows + cols - 1):
        left_diag = "".join([
            mtrx[i][j] for i in range(rows) for j in range(cols) if i + j == s
        ])
        count += get_count(left_diag, XMAS)

    return count


def xmas_count_p2(mtrx: list[str]):
    rows, cols = len(mtrx), len(mtrx[0])
    count = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            count += x_mas_check(mtrx, i, j)
    return count


def main():
    word_search = parse_text("puzzle_input/4.txt")
    count = xmas_count_p1(word_search)
    count = xmas_count_p2(word_search)
    print(count)


if __name__ == "__main__":
    main()


# part 1 answers:
#    - 82615  too high
#    - 2196   too low
#    - 2646   (CORRECT)

# part 2 answers:
#    - 2000   (CORRECT)
