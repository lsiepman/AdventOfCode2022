# read data
with open("./input/day06.txt") as file:
    data = file.read().replace("\n", "")
    data = [i for i in data]

def find_marker(slice):
    temp_set = set(slice)
    if len(slice) == len(temp_set):
        return True
    else:
        return False

def part1(data, len_slice):
    for i in range(len(data)):
        if i < len_slice - 1:
            continue
        
        slice_start = i - (len_slice - 1) 
        slice_end = i + 1 # slicing excludes last value, therefore adding one
        if (find_marker(data[slice_start:slice_end])):
            return i + 1

print("Part 1:", part1(data, 4))
print("Part 2:", part1(data, 14))