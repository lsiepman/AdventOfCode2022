import itertools
from collections import defaultdict
from copy import deepcopy

# read data
moves = {}
stacks = []
with open("./input/day05.txt") as f:
    for idx, line in enumerate(f):
        if idx > 9:
            a, b, c, d, e, f = line.strip().split(" ")
            moves[idx] = {"number_to_move": b, 
                          "from": d,
                          "to": f}
        elif idx < 9: 
            x = line.replace("\n", " ")
            y = list(map(''.join, zip(*[iter(x)]*4)))
            stacks.append(y)

# transpose stacks
containers = list(map(list, itertools.zip_longest(*stacks[::-1], fillvalue=None)))
boxes = defaultdict(list)
for i in containers:
    idx = i.pop(0)
    j = [k.strip() for k in i if k.strip() != ""]
    boxes[idx.strip()] = j

boxes_part2 = deepcopy(boxes)

# follow instructions part 1
for i in moves:
    num_boxes = int(moves[i]["number_to_move"])
    fro = moves[i]["from"]
    to = moves[i]["to"]
    for n in range(num_boxes):
        boxes[to].append(boxes[fro].pop())

top = []
for key in boxes:
    top.append(boxes[key][-1])

print(f"part 1: {''.join(top).replace('[', '').replace(']', '')}")

# follow instructions part 2
for i in moves:
    num_boxes = int(moves[i]["number_to_move"])
    fro = moves[i]["from"]
    to = moves[i]["to"]
    temp = []
    for n in range(num_boxes):
        temp.append(boxes_part2[fro].pop())
    temp.reverse()
    boxes_part2[to] = boxes_part2[to] + temp
    
top = []
for key in boxes_part2:
    top.append(boxes_part2[key][-1])

print(f"part 2: {''.join(top).replace('[', '').replace(']', '')}")

