from helper import endswith, digits, timeit

TEST = r"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def parse(text: str):
    return [list(map(int, line.replace(":", "").split())) for line in text.split("\n")]


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


# recursive brute force
def sol1(target: int, terms: list[int], p2=False):
    if len(terms) == 1:
        return terms[0] == target
    head, *tail = terms
    if sol1(target, [head + tail[0]] + tail[1:], p2):
        return True
    if sol1(target, [head * tail[0]] + tail[1:], p2):
        return True
    if p2 and sol1(target, [concat(head, tail[0])] + tail[1:], p2):
        return True
    return False


# non-recursive brute force
def sol2(target: int, terms: list[int], ops):
    head, *tail = terms
    combo = [head]
    for term in tail:
        combo = [op(n, term) for n in combo for op in ops]
    return target in combo


# recursive with attempt at pruning. think about what will prune a branch of tree quickest. if brute
# forcing left-to-right with add, mul (and concat) operations. this will move right-to-left with
# div, concat, sub operations, while altering target with each op: div -> concat -> sub.
def sol3(target, terms, p2=False):
    if len(terms) == 1:
        return terms[0] == target
    *head, tail = terms

    # if no remainder, then tail is a factor of target and what would result from division is
    # quotient
    quotient, rem = divmod(target, tail)
    
    # check division first as that reduces target search by largest amount
    if rem == 0 and sol3(quotient, head, p2):
        return True
    
    # if target ends with tail, then this mean concatenation in the left-to-right could occur,
    # continue this branch. if it doesn't, prune this branch and move on.
    if p2 and endswith(target, tail) and sol3(target // (10 ** digits(tail)), head, p2):
        return True
    
    # fallback subtraction case
    if sol3(target - tail, head, p2):
        return True
    
    # no branch results in target value
    return False
    

def day7(eqns, p2=False):
    total = 0
    for eqn in eqns:
        target, *terms = eqn
        if sol3(target, terms, p2):
            total += target
    return total


if __name__ == "__main__":
    with open("../puzzle_input/7.txt") as f:
        data = parse(f.read())
    # data = parse(TEST)
    timeit(day7, data)
    timeit(day7, data, True)


# part 1 answers:
#    - 1153997401072   (CORRECT)
#        attempt 1: ~0.187075s
#        attempt 2: ~0.037662s
#        attempt 3: ~0.003757s

# part 2 answers:
#    - 97902809384118  (CORRECT)
#        attempt 1: ~7.650215s
#        attempt 2: ~3.410470s
#        attempt 3: ~0.006052s
