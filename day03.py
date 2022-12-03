# imports
import string
from collections import defaultdict

# letter_values
letters = {}
for i,j in zip(string.ascii_lowercase, range(1, 27)):
    letters[i] = j

for i,j in zip(string.ascii_uppercase, range(27,53)):
    letters[i] = j

# functions
def split_list(l):
    half = int(len(l)/2)
    return l[:half], l[half:]

def find_common_elements(l1, l2, l3=None):
    a = set(l1)
    b = set(l2)
    if l3 is None:
        return a.intersection(b).pop()
    else:
        c = set(l3)
        return a.intersection(b, c).pop()

def fetch_value(key, letters):
    return letters[key]

# part 1
data = {}
idx = 0
with open("./input/day03.txt") as f:
    for line in f:
        x = [i for i in line.strip()]
        data[idx] = split_list(x)
        idx += 1

common_elements = []
for i in data:
    common_elements.append(find_common_elements(data[i][0], data[i][1]))

print(f"Part 1: {sum([fetch_value(i, letters) for i in common_elements])}")

# part 2
data2 = defaultdict(list)
idx = 0
with open("./input/day03.txt") as f:
    group_idx = 1
    for line in f:
        x = [i for i in line.strip()]
        if group_idx < 4:
            data2[idx].append(x)
            group_idx += 1
        elif group_idx == 4:
            idx += 1
            data2[idx].append(x)
            group_idx = 2

common_badges = []
for i in data2:
    common_badges.append(find_common_elements(data2[i][0], data2[i][1], data2[i][2]))

print(f"Part 2: {sum([fetch_value(i, letters) for i in common_badges])}")
