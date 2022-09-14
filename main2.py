import re
from itertools import *


def arrow(a, b):
    return (not a) or b


def solve(variables: str, patterns: list, function):

    for names in permutations(variables):
        possible_states = []

        for state in product([0, 1], repeat=4):
            values = {
                names[0]: state[0],
                names[1]: state[1],
                names[2]: state[2],
                names[3]: state[3]
            }

            if function(values):
                possible_states.append("".join(list(map(str, state))))

        matched_patterns = set()

        for pattern in patterns:
            for state in possible_states:
                if re.match(pattern, state) is not None:
                    matched_patterns.add(patterns.index(pattern))

        if len(matched_patterns) == len(patterns):
            print(names)


def n_224():
    def func(values):
        x, y, z, w = values['x'], values['y'], values['z'], values['w']
        return not (not arrow(x, z) or (y == w))

    patterns = ["00[0-1][0-1]", "0[0-1][0-1][0-1]", "11[0-1]0"]
    solve("xyzw", patterns, func)


def n_225():
    def func(values):
        x, y, z, w = values['x'], values['y'], values['z'], values['w']
        return not ((y or x) == (arrow(y, w) or (not z)))

    patterns = ["1000", "0100", "1010"]
    solve("xyzw", patterns, func)


def n_227():
    def func(values):
        a, b, c, d = values['a'], values['b'], values['c'], values['d']
        return not (arrow(a, b) and arrow(c, d) or (not c))

    patterns = ["1010", "0011", "0111", "1011"]
    solve("abcd", patterns, func)


def n_228():
    def func(values):
        x, y, z, w = values['x'], values['y'], values['z'], values['w']
        return not (not arrow(w, z) or arrow(x, y) or (not x))

    patterns = ["1[0-1][0-1][0-1]", "010[0-1]", "[0-1]0[0-1][0-1]"]
    solve("xyzw", patterns, func)


def n_229():
    def func(values):
        x, y, z, w = values['x'], values['y'], values['z'], values['w']
        return not (arrow(arrow(x, z), y) or (not w))

    patterns = ["10[0-1][0-1]", "[0-1]10[0-1]", "0[0-1][0-1][0-1]"]
    solve("xyzw", patterns, func)


n_229()
