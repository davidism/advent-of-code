from itertools import pairwise

reports = []

with open("day02.txt", encoding="utf8") as f:
    for line in f:
        reports.append(tuple(map(int, line.split())))


def is_safe(r):
    diffs = [a - b for a, b in pairwise(r)]
    return (all(d < 0 for d in diffs) or all(d > 0 for d in diffs)) and all(
        1 <= abs(d) <= 3 for d in diffs
    )


print(sum(is_safe(r) for r in reports))


def is_tolerated(r):
    if is_safe(r):
        return True

    for i in range(len(r)):
        if is_safe([*r[:i], *r[i + 1 :]]):
            return True

    return False


print(sum(is_tolerated(r) for r in reports))
