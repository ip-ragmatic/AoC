import re


pattern_p1 = r"mul\(\d{1,3},\d{1,3}\)"
pattern_p2 = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"


def mul(L, R):
    return L * R


def decorrupt_file(path, pattern):
    with open(path) as file:
        return re.findall(pattern, file.read())


def get_sum_1(instructions):
    return sum(eval(cmd) for cmd in instructions)


def get_sum_2(instructions):
    state = True
    total = 0
    for cmd in instructions:
        if cmd == "do()":
            state = True
        elif cmd == "don't()":
            state = False
        if state and cmd.startswith("mul"):
            total += eval(cmd)
    return total


def main():
    commands = decorrupt_file("puzzle_input/3.txt", pattern_p2)
    total = get_sum_2(commands)
    print(total)


if __name__ == "__main__":
    main()


# Answer for part 1:
#   - 185797128 (CORRECT)

# Answers for part 2:
#   - 24575205  too low
#   - 89798695  (CORRECT)
