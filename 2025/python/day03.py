from operator import itemgetter

with open("../day03.txt") as f:
    data = tuple(tuple(int(c) for c in line.strip()) for line in f)

get1 = itemgetter(1)


def max_joltage(bank: tuple[int, ...], size: int) -> int:
    enumerated_bank = tuple(enumerate(bank))
    len_bank = len(bank)
    offset = 0
    window = len_bank - size + 1
    chosen = []

    while size:
        i, battery = max(enumerated_bank[offset : offset + window], key=get1)
        chosen.append(battery)
        offset = i + 1
        size -= 1
        window = len_bank - offset - size + 1

    return int("".join(map(str, chosen)))


print(sum(max_joltage(b, 2) for b in data))
print(sum(max_joltage(b, 12) for b in data))
