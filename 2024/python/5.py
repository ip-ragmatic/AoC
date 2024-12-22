from collections import deque, defaultdict

TEST = r"""
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def parse_text(text):
    ls1, ls2 = text.split("\n\n")
    order_rules = [tuple(line.split("|")) for line in ls1.split()]
    produce = [list(line.split(",")) for line in ls2.split()]
    return order_rules, produce

def find_involved(update, rules):
    return [rule for rule in rules if all(num in update for num in rule)]

def correct_order(update: list[str], rules: list[tuple[str]]):
    indices = {n: i for i, n in enumerate(update)}
    for rule in rules:
        if indices[rule[0]] >= indices[rule[1]]:  # rule[0] must come before rule[1]
            return False
    return True        


def topological_sort(update: list[str], rules: list[tuple[str]]):  # RIGHT RULE DEPENDS ON LEFT RULE
    """
    Topological Sort Steps (Kahn):
        - this assumes the data passed in is definitely a DAG and unsorted
  
    1. create graph and in_degree structures
    2. populate graph with nodes from DAG data and update corresponding in_degrees of each node
    3. create the queue (like a call-stack); left-most (or bottom) value contains nodes w/ in_degree = 0
    4. create the list that'll contain sorted DAG data
    5. implement sort logic:
        a. remove first value from queue (current node) and append it to sorted structure placeholder
        b. loop through dependencies of current node (values of key in graph structure) and apply each:
            - subtract in_degree by 1
            - check if in_degree now equals 0; if it does, append it to the queue (wait in line bud)
    6. sorted structure placeholder now sorted the DAG data, meaning the order of it corresponds to the
       order of dependencies (left-most has no dependencies, right-most depends on everything before it)
  
    """
    # create graph and in_degree structure
    graph = defaultdict(list)  # key = left-rule values, value = associated right-rule values
    in_degree = {num: 0 for num in update}
  
    # populate graph and update in_degree information
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            graph[rule[0]].append(rule[1])  # left-val is a node, right is its dependency
            in_degree[rule[1]] += 1  # the dependency now has 1 additional in_degree
  
    # create queue
    queue = deque(num for num in update if in_degree[num] == 0)  # queue starts w/ nodes w/ no incoming edges (in_degree = 0)
    sorted_update = []  # sorted elements will gradually be added here
  
    # sort logic
    while queue:  # while there's elements in the queue
        cur_node = queue.popleft()
        sorted_update.append(cur_node)
      
        for dependency in graph[cur_node]:  # iterate thru the current node's values in the graph structure
            in_degree[dependency] -= 1  # removal of cur_node from queue decreases in_degree of nodes depending on cur_node
            if in_degree[dependency] == 0:  # if node has no edges to it, it can be added to the queue
                queue.append(dependency)

    return sorted_update


def middle_val_p1(update, rules):
    sum_middles = 0
    for numbers in update:
        involved = find_involved(numbers, rules)
        if correct_order(numbers, involved):
            mid = len(numbers) // 2
            sum_middles += int(numbers[mid])
    return sum_middles


def middle_val_p2(update, rules):
    sum_middles = 0
    for numbers in update:
        involved = find_involved(numbers, rules)
        if not correct_order(numbers, involved):
            sorted_list = topological_sort(numbers, involved)
            mid = len(sorted_list) // 2
            sum_middles += int(sorted_list[mid])
    return sum_middles


def main():
    # order_rules, num_mtrx = parse_text(TEST)
    # val = middle_val_p2(num_mtrx, order_rules)
    # print(val)

    with open("puzzle_input/5.txt") as f:
        order_rules, num_mtrx = parse_text(f.read())
    val = middle_val_p2(num_mtrx, order_rules)
    print(val)


if __name__ == "__main__":
    main()


# part 1 answers:
#    - 4872  (CORRECT)

# part 2 answers:
#    - 4770  too low
#    - 5151  too low
#    - 5564  (CORRECT)
