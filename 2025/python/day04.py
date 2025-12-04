from collections.abc import Iterator

with open("day04.txt") as f:
    data = {(x, y) for y, line in enumerate(f) for x, c in enumerate(line) if c == "@"}


def adjacent(point: tuple[int, int]) -> Iterator[tuple[int, int]]:
    x, y = point

    for dx, dy in (
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ):
        yield x + dx, y + dy


def removable(rolls: set[tuple[int, int]]) -> set[tuple[int, int]]:
    out = set()

    for roll in rolls:
        if sum(ap in rolls for ap in adjacent(roll)) < 4:
            out.add(roll)

    return out


print(len(removable(data)))

remaining = data.copy()
removed = 0

while remaining and (to_remove := removable(remaining)):
    remaining -= to_remove
    removed += len(to_remove)

print(removed)
