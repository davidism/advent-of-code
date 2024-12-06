with open("day04.txt", encoding="utf8") as f:
    data = {(x, y): c for y, line in enumerate(f) for x, c in enumerate(line)}


def count_xmas(x, y):
    match data[(x, y)]:
        case "X":
            rest = "MAS"
        case "S":
            rest = "AMX"
        case _:
            return 0

    return sum(
        "".join(data.get((x + dx, y + dy), "") for dx, dy in offset) == rest
        for offset in (
            ((1, 0), (2, 0), (3, 0)),
            ((1, 1), (2, 2), (3, 3)),
            ((0, 1), (0, 2), (0, 3)),
            ((-1, 1), (-2, 2), (-3, 3)),
        )
    )


print(sum(count_xmas(x, y) for x, y in data))


def check_x_mas(x, y):
    if data[x, y] != "A":
        return False

    try:
        return "".join(
            (
                data[x - 1, y - 1],
                data[x + 1, y - 1],
                data[x - 1, y + 1],
                data[x + 1, y + 1],
            )
        ) in {"MMSS", "MSMS", "SMSM", "SSMM"}
    except KeyError:
        return False


print(sum(check_x_mas(x, y) for x, y in data))
