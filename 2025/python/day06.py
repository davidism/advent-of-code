import operator
from functools import reduce
from itertools import zip_longest

with open("../day06.txt") as f:
    data = f.read().splitlines()

print(
    sum(
        reduce(
            operator.mul if op == "*" else operator.add, map(int, values), int(start)
        )
        for start, *values, op in zip(
            *(line.strip().split() for line in data), strict=True
        )
    )
)

total = 0
op = operator.add
value = 0

for chars in zip_longest(*data, fillvalue=" "):
    line = "".join(chars).strip()

    if not line:
        total += value
        continue

    if not line.isdecimal():
        value = int(line[:-1])
        op = operator.mul if line[-1] == "*" else operator.add
    else:
        value = op(value, int(line))

total += value
print(total)
