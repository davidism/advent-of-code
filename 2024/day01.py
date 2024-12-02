from collections import Counter

left = []
right = []

with open("day01.txt", encoding="utf8") as f:
    for line in f:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()
diff = sum(abs(a - b) for a, b in zip(left, right, strict=True))
print(diff)

right_count = Counter(right)
similarity = sum(a * right_count[a] for a in left)
print(similarity)
