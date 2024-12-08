from collections.abc import Iterator
from itertools import combinations
from pathlib import Path

type Point = tuple[int, int]
frequencies: dict[str, list[Point]] = {}
width = height = 0

for y, line in enumerate(Path("day08.txt").read_text("utf8").splitlines()):
    width = len(line)
    height += 1

    for x, c in enumerate(line):
        if c == ".":
            continue

        frequencies.setdefault(c, []).append((x, y))


def pair_antinodes(a: Point, b: Point, full=False) -> Iterator[Point]:
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = by - ay
    nx = ax - dx
    ny = ay - dy

    if full:
        yield a

    while 0 <= nx < width and 0 <= ny < height:
        yield nx, ny
        nx -= dx
        ny -= dy

        if not full:
            break

    nx = bx + dx
    ny = by + dy

    if full:
        yield b

    while 0 <= nx < width and 0 <= ny < height:
        yield nx, ny
        nx += dx
        ny += dy

        if not full:
            break


def count_antinodes(full=False):
    antinodes = set[Point]()

    for _, points in frequencies.items():
        for a, b in combinations(points, 2):
            antinodes.update(pair_antinodes(a, b, full=full))

    return len(antinodes)


print(count_antinodes())
print(count_antinodes(True))
