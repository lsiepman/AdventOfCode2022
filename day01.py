from collections import defaultdict
import operator

# read data
data = []
with open("./input/day01.txt") as f:
    for line in f:
        data.append(line.strip())

# separate calories per elf
elves = defaultdict(list)
num_elf = 0
for cal in data:
    if cal == "":
        num_elf += 1
    else:
        elves[num_elf].append(cal)

# sum calories per elf
max_cals = {}
for k,v in elves.items():
    max_cals[k] = sum([int(j) for j in v])

# key, value pair for max calories in the dict
max_kv = max(max_cals.items(), key=operator.itemgetter(1))

# answer to part 1
print(f"Elf {max_kv[0]} is carrying the largest amount of calories: {max_kv[1]}")

# find top 3 calorie counts
top3 = sorted(max_cals.values(), reverse=True)[0:3]

# answer to part 2
print(f"The total calories carried by the top 3 elves sums to {sum(top3)} calories")

