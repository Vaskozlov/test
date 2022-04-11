from itertools import permutations

counter = 0

for i in range(1000000):
    s = i
    n = 1
    while s < 54:
        s = s + 7
        n = n * 3

    if n == 243:
        counter += 1

print(counter)

a = '1' * 20 + '32' * 15 + '3' * 40
max_sum = 0

# for variant in permutations(a):
s = '>' + a + '<'

while '><' not in s:
    s = s.replace('>1', '3>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)
    s = s.replace('3<', '<1', 1)
    s = s.replace('2<', '<3', 1)
    s = s.replace('1<', '<2', 1)

s = s.replace('>', '')
s = s.replace('<', '')

current_sum = sum(list(map(int, s)))
max_sum = max(current_sum, max_sum)

print(max_sum)

number = 7 ** 103 + 20 * 7 ** 204 - 3 * 7 ** 57 + 97
s = ''

while number != 0:
    s += str(number % 7)
    number //= 7

print(s.count('6'))

for i in range(10**3, 2 * 10**4):
    for j in range(7 ** 3, 7 ** 6):
        x, y = i, j
        a = b = 0

        while x * y > 0:
            if x > 0:
                a = a + 1
            if y > 0 and y % 7 > b:
                b = y % 7

            x = x // 10
            y = y // 7

        if a == 4 and b == 5:
            print(i * j)
            exit(0)
