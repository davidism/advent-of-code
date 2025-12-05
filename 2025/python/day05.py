with open("../day05.txt") as f:
    data_ranges: list[range] = []

    for line in f:
        if not (line := line.strip()):
            break

        start, _, stop = line.partition("-")
        data_ranges.append(range(int(start), int(stop) + 1))

    data_ids: list[int] = [int(line.strip()) for line in f]

data_ranges.sort(key=lambda r: (r.start, r.stop))
current_range = data_ranges[0]
distinct_ranges = []

for r in data_ranges[1:]:
    if r.start in current_range:
        if r.stop not in current_range:
            current_range = range(current_range.start, r.stop)

        continue

    distinct_ranges.append(current_range)
    current_range = r

distinct_ranges.append(current_range)

fresh = 0

for id in data_ids:
    if any(id in r for r in distinct_ranges):
        fresh += 1

print(fresh)
print(sum(map(len, distinct_ranges)))
