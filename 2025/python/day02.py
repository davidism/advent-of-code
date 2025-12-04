from more_itertools import all_equal
from more_itertools import sliced

with open("../day02.txt") as f:
    data = [
        range(int(a), int(b) + 1)
        for a, b in (r.split("-", 1) for r in f.read().strip().split(","))
    ]

answer1 = 0
answer2 = 0

for item_range in data:
    for item in item_range:
        str_item = str(item)
        len_item = len(str_item)
        half_len = len_item // 2
        is_even = len_item % 2 == 0

        for sub_len in range(half_len, 0, -1):
            if len_item % sub_len != 0:
                continue

            if not all_equal(sliced(str_item, sub_len)):
                continue

            answer2 += item

            if is_even and sub_len == half_len:
                answer1 += item

            break

print(answer1)
print(answer2)
