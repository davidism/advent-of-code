import math

with open("day01.txt") as f:
    data = [
        (1 if line[0] == "R" else -1) * int(line[1:]) for line in f.read().splitlines()
    ]

dial = 50
code1 = 0
code2 = 0

for amount in data:
    end = dial + amount
    zeroes = abs(math.trunc(end / 100))

    if dial != 0 and end <= 0:
        zeroes += 1

    dial = end % 100

    if dial == 0:
        code1 += 1

    code2 += zeroes

print(code1)
print(code2)
