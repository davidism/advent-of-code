from collections import defaultdict
from collections import deque
from pathlib import Path

initial_obstructions = set[tuple[int, int]]()
width = height = 0
start_x = start_y = 0
dir_order = ((0, -1), (-1, 0), (0, 1), (1, 0))

for y, line in enumerate(Path("day06.txt").read_text("utf8").splitlines()):
    width = len(line)
    height += 1

    for x, c in enumerate(line):
        if c == "^":
            start_x = x
            start_y = y
        elif c == "#":
            initial_obstructions.add((x, y))


def patrol(obstructions: set[tuple[int, int]]) -> tuple[set[tuple[int, int]], bool]:
    guard_x = start_x
    guard_y = start_y
    # The current direction is dirs[0], and dirs.rotate() chooses the next direction.
    dirs = deque(dir_order)
    seen = defaultdict[tuple[int, int], set[tuple[int, int]]](set)

    while True:
        if not ((0 <= guard_x < width) and (0 <= guard_y < height)):
            # moved out of the area
            return set(seen.keys()), False

        if dirs[0] in seen[guard_x, guard_y]:
            # loop, already moved to this point in this direction
            return set(seen.keys()), True

        # Record the guard's direction at the guard's position.
        seen[guard_x, guard_y].add(dirs[0])
        dx, dy = dirs[0]
        next_x = guard_x + dx
        next_y = guard_y + dy

        # Rotate if obstructed, otherwise move.
        if (next_x, next_y) in obstructions:
            dirs.rotate()
        else:
            guard_x = next_x
            guard_y = next_y


# Record the points from the initial patrol. These are the only points we need
# to place new obstructions on.
points, _ = patrol(initial_obstructions)
print(len(points))
loops = 0

for point in points:
    # Add one point from the initial patrol to the obstructions.
    _, loop = patrol({point, *initial_obstructions})
    loops += loop

print(loops)
