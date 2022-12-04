from collections import defaultdict

# read data
data = {}
idx = 0
with open("./input/day04.txt") as f:
    for line in f:
        a, b = line.strip().split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        data[idx] = {"a": {}, "b":{}}
        data[idx]["a"]["min"] = int(a1)
        data[idx]["a"]["max"] = int(a2)
        data[idx]["b"]["min"] = int(b1)
        data[idx]["b"]["max"] = int(b2)
        idx += 1

# functions
def check_containing(left, right):
    if left["min"] <= right["min"] and left["max"] >= right["max"]:
        return True
    else:
        return False

def check_overlap(left, right):
    if left["min"] <= right["min"] and left["max"] >= right["min"]:
        return True
    elif right["min"] <= left["min"] and right["max"] >= left["min"]:
        return True
    elif left["min"] <= right["min"] and left["max"] >= right["max"]:
        return True
    elif right["min"] <= left["min"] and right["max"] >= left["max"]:
        return True
    else:
        return False

# part 1
containing = []
for idx in data:
    containing.append(check_containing(data[idx]["a"], data[idx]["b"]))
    if data[idx]["a"] != data[idx]["b"]:
        containing.append(check_containing(data[idx]["b"], data[idx]["a"]))

print(f"Part 1: There are {sum(containing)} ranges that fully contain the other")

# part 2
overlap = []
for idx in data:
    overlap.append(check_overlap(data[idx]["a"], data[idx]["b"]))
   
print(f"Part 2: There are {sum(overlap)} ranges that overlap with the other")
