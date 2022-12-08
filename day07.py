from collections import defaultdict
import re

data = []
with open("./input/day07.txt") as f:
    for line in f:
        data.append(line.strip())

def get_nested_dict(dct, keys):    
    for key in keys:
        dct = dct[key]
    return dct

def find_struct(data):
    folder = defaultdict(dict)

    cur_dir = ""
    path = []
    for line in data:
        if "$ cd" in line and ".." not in line:
            cur_dir_name = re.search(r"[a-zA-Z\/]+$", line).group()
            path.append(cur_dir_name)
            if cur_dir == "":
                cur_dir = folder[cur_dir_name]
            else:
                if cur_dir_name in cur_dir.keys():
                    cur_dir = cur_dir[cur_dir_name]
                else:
                    cur_dir[cur_dir_name] = {}
                    cur_dir = cur_dir[cur_dir_name]

        elif "ls" in line:
            continue
        elif ".." in line:
            path.pop()
            cur_dir_name = path[-1]
            cur_dir = get_nested_dict(folder, path)
        elif "dir" in line:
            dir_name = re.search(r"[a-zA-Z\/]+$", line).group()
            cur_dir[dir_name] = {}
        else:
            size = int(re.search(r"^[0-9]+", line).group())
            file = re.search(r"[a-zA-Z\/\.]+$", line).group()
            if "files" in cur_dir.keys() and isinstance(cur_dir["files"], list):
                cur_dir["files"].append((file, size))
            else:
                cur_dir["files"] = [(file, size)]
                # calc sizes here
                # take path into account
    
    return folder

def calc_sizes_per_dict(struct):
    if isinstance(struct, dict):
        if "files" in struct.keys():
            struct["total_size_files"] = sum([i[1] for i in struct["files"]])
            struct["total_folder_size"] = 0

        keys = struct.keys()
        for key in keys:
            struct[key] = calc_sizes_per_dict(struct[key])
    
    return struct

def calc_total_folder_size(struct, path=[]):
    if isinstance(struct, dict):
        keys = struct.keys()
        for key in keys:
            path.append
            struct[key] = calc_total_folder_size(struct[key])
        

folder = find_struct(data)
folder = calc_sizes_per_dict(folder)
print(folder)
