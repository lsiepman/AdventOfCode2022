import itertools
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