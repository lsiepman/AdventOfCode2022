# read data
with open("./input/day06.txt") as file:
    data = file.read().replace("\n", "")

def find_marker(slice):
    return len(slice) == len(set(slice))
        
def calc_answer(data, len_slice):
    for i in range(len(data)):
        if i < len_slice - 1:
            continue
        
        slice_start = i - (len_slice - 1) 
        slice_end = i + 1 # slicing excludes last value, therefore adding one
        if (find_marker(data[slice_start:slice_end])):
            return i + 1

print("Part 1:", calc_answer(data, 4))
print("Part 2:", calc_answer(data, 14))