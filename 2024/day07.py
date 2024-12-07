from itertools import product
from operator import add
from operator import mul
from pathlib import Path

equations = tuple(
    (int(a), tuple(map(int, b.split())))
    for a, _, b in (
        line.partition(": ")
        for line in Path("day07.txt").read_text("utf8").splitlines()
    )
)


def concat(a, b):
    return int(f"{a}{b}")


def validate(goal, numbers, sequences):
    start, *rest = numbers

    for operators in sequences[len(rest)]:
        total = start

        for operator, number in zip(operators, rest, strict=True):
            total = operator(total, number)

        if total == goal:
            return True

    return False


def calibrate(ops):
    sequences = tuple(
        tuple(product(ops, repeat=n)) for n in range(max(len(e[1]) for e in equations))
    )
    total = 0

    for equation in equations:
        if validate(*equation, sequences):
            total += equation[0]

    return total


print(calibrate((add, mul)))
print(calibrate((add, mul, concat)))
