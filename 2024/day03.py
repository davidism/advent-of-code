import re

with open("day03.txt", encoding="utf8") as f:
    data = f.read()

part1 = 0
part2 = 0
enabled = True

for instruction in re.findall(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)", data):
    if instruction == "don't()":
        enabled = False
    elif instruction == "do()":
        enabled = True
    else:
        a, b = map(int, instruction[:-1].partition("(")[2].split(","))
        value = a * b
        part1 += value

        if enabled:
            part2 += value

print(part1)
print(part2)
