from collections import defaultdict
from pathlib import Path

data = Path("day05.txt").read_text("utf8")
rule_data, _, update_data = data.partition("\n\n")
updates = [tuple(map(int, line.split(","))) for line in update_data.splitlines()]
dependencies = defaultdict[int, set[int]](set)

for line in rule_data.splitlines():
    sa, _, sb = line.partition("|")
    dependencies[int(sb)].add(int(sa))


def is_valid(update: tuple[int, ...]) -> bool:
    set_update = set(update)
    seen = set()

    for page in update:
        deps = dependencies[page] & set_update

        if deps - seen:
            return False

        seen.add(page)

    return True


def fix(update: tuple[int, ...]) -> list[int]:
    set_update = set(update)
    remaining = {p: dependencies[p] & set_update for p in update}
    result = []

    while remaining:
        for page in remaining:
            if remaining[page]:
                continue

            result.append(page)
            del remaining[page]

            for deps in remaining.values():
                deps.remove(page)

            break

    return result


valid = []
invalid = []
fixed = []

for update in updates:
    if is_valid(update):
        valid.append(update)
    else:
        fixed.append(fix(update))

print(sum(u[len(u) // 2] for u in valid))
print(sum(u[len(u) // 2] for u in fixed))
