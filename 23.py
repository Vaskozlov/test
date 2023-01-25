import sys

sys.setrecursionlimit(1000000)


def f1(x, target) -> int:
    if x < target:
        return 0

    if x == target:
        return 1

    return f1(x - 3, target) + f1(x // 2, target)


print(f1(108, 42) * f1(42, 12))


def f2(x, target, commands: int) -> int:
    if x == target:
        return commands % 2

    if x > target:
        return 0

    if x == 1:
        return f2(x + 2, target, commands + 1) + f2(x * 2, target, commands + 1)

    return f2(x + 2, target, commands + 1) + f2(x * 2, target, commands + 1) + f2(x * x, target, commands + 1)


print(f2(1, 100, 0))
