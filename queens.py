from sat_utils import solve_all, some_of, one_of, basic_fact, all_of, one_or_less, zero_or_more
from sys import intern
from itertools import chain
import time

display_resulting_states = False

n = 12

board = ''.join([f"{x},{y}\n" if x == n-1 else f"{x},{y}" + ' ' for y in range(n) for x in range(n)])[:-1]

grid = [row.split(" ") for row in board.splitlines()]

diagonals = []

for i, row in enumerate(chain(range(n), range(n-2,-1,-1))):
    diagonal = []
    x = row if i == row else n - 1
    y = 0 if i == row else n - 1 - row
    for col in range(row + 1):
        diagonal += [grid[y][x]]
        x -= 1
        y += 1
    diagonals += [diagonal]

for i, row in enumerate(chain(range(n), range(n-2,-1,-1))):
    diagonal = []
    x = n - 1 - row if i == row else 0
    y = 0 if i == row else n - 1 - row
    for col in range(row + 1):
        diagonal += [grid[y][x]]
        x += 1
        y += 1
    diagonals += [diagonal]


# groups excludes diagonals
groups = grid[:] + list(zip(*grid))
points = board.split()

def comb(point, value):
    'Format a fact (a value assigned to a given point)'
    return intern(f'{point} {value}')

def str_to_facts(s):
    'Convert str in row major form to a list of facts'
    return [comb(point, value) for point, value in zip(points, s) if value != ' ']

def facts_to_str(facts):
    'Convert a list of facts to a string in row major order with blanks for unknowns'
    point_to_value = dict(map(str.split, facts))
    return ''.join(point_to_value.get(point, ' ') for point in points)

def show(flatline):
    for i in range(n):
        offset = i * n
        print(flatline[offset:offset + n])


values = list("Q" + "e")

cnf = []

for point in points:
    cnf += one_of(comb(point, value) for value in values)

for group in groups:
    cnf += one_of(comb(point, "Q") for point in group)
    cnf += some_of(comb(point, "e") for point in group)

for diag in diagonals:
    cnf += one_or_less(comb(point, "Q") for point in diag)
    cnf += zero_or_more(comb(point, "e") for point in diag)

if not display_resulting_states:
    count = 0
    start = time.time()
    count = len(solve_all(cnf))
    print(count)
    print(f"Time elapsed: {time.time()-start}")
else:
    results = [facts_to_str(solution) for solution in solve_all(cnf)]

    for i, result in enumerate(results):
        print(i + 1)
        show(result)
        print()
