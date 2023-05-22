import re
from functools import *
from itertools import *
from math import *
from pprint import pprint


def f2():
    def F(a, b, c, d):
        return not (b <= a) and (c <= d) or a and b and c and not d

    def solve(letters, patterns, func):
        for letters_option in permutations(letters):
            matched = set()
            matched_values = set()
            m = dict(zip(patterns, [set() for i in range(len(patterns))]))

            for values_option in product([0, 1], repeat=len(letters)):
                letter_value_dict = dict(zip(letters_option, values_option))
                f = func(**letter_value_dict)
                s = "".join(map(str, values_option)) + str(int(f))

                for pattern in patterns:
                    if re.fullmatch(pattern, s):
                        matched.add(pattern)
                        matched_values.add(s)
                        m[pattern].add(s)

            if len(matched) == len(patterns) and len(matched_values) == len(patterns):
                print(letters_option)
                pprint(m)

    solve("abcd", ["[01]0001", "[01]{3}01", "[01]{2}001", "[01]0[01]{2}1"], F)
    # bdca


def f5():
    for i in range(1, 1000):
        n = i
        s = ""

        while n != 0:
            s = f"{n % 10:04b}" + s
            n //= 10

        s = s.replace('0', '2').replace('1', '0').replace('2', '1')

        if int(s, 2) == 151:
            print(i)


def f6():
    print(lcm(360, 50) // 50)


def f7():
    print(68 * 3 // 2 // 6)


def f8():
    print("0123456789ABCDE"[::-1])
    print("123456789ABCDEF"[::-1])


def f9():
    with open("data9.txt") as fin:
        data = fin.read().split('\n')

    counter = 0

    for line in data:
        numbers = sorted(list(map(int, line.split(' '))))

        if numbers[-1] - numbers[0] >= 50 and numbers[1] * numbers[2] <= 1000:
            counter += 1

    print(counter)


def f10():
    print(2)


def f11():
    N = 12312
    k = N // 50
    i = ceil(log2(2000))

    I = ceil(k * 50 * i / 8) + ceil(N % 50 * i / 8)
    print(ceil(I / 1024))


def f12():
    for one, two, tree in product([i for i in range(1, 100)], repeat=3):
        s = '0' + '1' * one + '2' * two + '3' * tree + '0'

        while '00' not in s:
            s = s.replace('01', '210', 1).replace('02', '320', 1).replace('03', '3012', 1)

        if s.count('1') == 13 and s.count('2') == 27 and s.count('3') == 24:
            print(2 + (one + two + tree) * 2)


def f14():
    for x in range(10):
        n = 3 * 7 ** (x + 1) + 13 * 7 ** (x + 2) + 31 * 7 ** (3 * x) + 1 * 7 ** (2 * x)

        s = ''
        while n != 0:
            s = str(n % 7) + s
            n //= 7

        if sum(map(int, s)) == 18:
            print(x)
            break


def f15():
    def check(A):
        return all(
            (((x > 8) <= (x ** 2 + 3 * x >= A)) and ((y ** 2 + 5 * y > A) <= (y >= 4)) for x, y in
             product([i for i in range(0, 1000)], repeat=2))
        )

    counter = 0

    for a in range(-2000, 2000):
        if check(a):
            counter += 1

    print(counter)


def f16():
    def f(n):
        if n < 3:
            return n + 1

        if n % 2 == 0:
            return f(n - 2) + n - 2

        return f(n + 2) + n + 2

    counter = 0

    for i in range(0, 2000, 2):
        try:
            n = f(i)

            if len(str(n)) == 5:
                counter += 1

        except RecursionError:
            pass

    print(counter)


def f17():
    with open("data17.txt") as fin:
        data = list(map(int, fin.read().split('\n')))

    middle_digits = dict()

    for elem in data:
        n = abs(elem)
        s = str(n)

        if len(s) != 3:
            continue

        n = int(s[1])

        if n not in middle_digits.keys():
            middle_digits[n] = 0
        else:
            middle_digits[n] += 1

    most_common_digit = max(middle_digits.items(), key=lambda x: x[1])[0]

    pairs = []

    for n1, n2 in zip(data, data[1:]):
        if abs(n1) % 10 == most_common_digit or abs(n2) % 10 == most_common_digit:
            pairs.append(n1 + n2)

    print(len(pairs), max(pairs))


def f18():
    with open("data18.txt") as fin:
        data = fin.read().split('\n')

    for i in range(len(data)):
        data[i] = list(map(int, data[i].split(' ')))

    max_x = len(data) - 1
    max_y = len(data[0]) - 1

    @cache
    def f(x, y):
        def calculate_food(new_y, new_x):
            try:
                if new_x != x:
                    if data[y][x - 1] % 2 == data[y][x + 1] % 2:
                        return 10
                else:
                    if data[y - 1][x] % 2 == data[y + 1][x] % 2:
                        return 10
            except BaseException:
                pass

            return 0

        if x == max_x and y == max_y:
            return data[y][x]

        if x == max_x:
            return data[y][x] + f(y + 1, x) + calculate_food(y + 1, x)

        if y == max_y:
            return data[y][x] + f(y, x + 1) + calculate_food(y, x + 1)

        return data[y][x] + min(
            calculate_food(y + 1, x) + f(y + 1, x),
            calculate_food(y, x + 1) + f(y, x + 1)
        )

    print(f(0, 0))


def f19():
    def f(s, moves, moves_to_win, force_any=False):
        if s >= 166:
            return moves % 2 == moves_to_win % 2

        if moves == moves_to_win:
            return False

        nm = moves + 1
        opt = [f(s + 2, nm, moves_to_win), f(s + 10, nm, moves_to_win)]

        for i in range(2, 80):
            if s * i - i > 80:
                break

            opt.append(f(s * i, nm, moves_to_win))

        if nm % 2 == moves_to_win % 2 or nm == 2:
            return any(opt)

        return all(opt)

    print(min(s for s in range(1, 166) if not f(s, 0, 1) and f(s, 0, 3)))


def f20():
    def f(s, moves, moves_to_win, force_any=False):
        if s >= 166:
            return moves % 2 == moves_to_win % 2

        if moves == moves_to_win:
            return False

        nm = moves + 1
        opt = [f(s + 2, nm, moves_to_win), f(s + 10, nm, moves_to_win)]

        for i in range(2, 80):
            if s * i - s > 80:
                break

            opt.append(f(s * i, nm, moves_to_win))

        if nm % 2 == moves_to_win % 2:
            return any(opt)

        return all(opt)

    data = [s for s in range(1, 166) if not f(s, 0, 1) and f(s, 0, 3)]
    print(min(data), max(data))

    print(min(s for s in range(1, 166) if not f(s, 0, 2) and f(s, 0, 4)))


def f23(s, counter) -> set:
    if counter == 9:
        return 