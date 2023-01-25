def f7(x, target) -> int:
    if target > x:
        return 0

    if x == target:
        return 1

    return f7(x - 2, target) + f7(x // 2, target)


print(f7(28, 10) * f7(10, 1))


def f8(x, target) -> int:
    if target > x:
        return 0

    if x == target:
        return 1

    return f8(x - 1, target) + f8(x // 2, target)


print(f8(30, 12) * f8(12, 1))


def f9(x, target) -> int:
    if x > target:
        return 0

    if x == target:
        return 1

    result = f9(x + 1, target) + f9(x * 5, target)

    if (x * 10 + 1) % 3 == 0:
        result += f9(x * 10 + 1, target)

    return result


print(f9(1, 410))
