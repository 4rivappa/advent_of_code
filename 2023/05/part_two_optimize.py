import sys

# class Node:
#     def __init__(self, value, side, index):
#         self.val = value
#         if side == "left":
#             self.is_left = True
#         else:
#             self.is_left = False
#         self.index = index

# def merge_ranges(seeds_arr):
#     all_nodes = []
#     for it in range(0, len(seeds_arr), 2):
#         all_nodes.append(Node(seeds_arr[it], "left", it))
#         all_nodes.append(Node(seeds_arr[it] + seeds_arr[it+1], "right", it+1))
#     all_nodes.sort(key = lambda x: (x.val, not(x.is_left)))
#     for node in all_nodes:
#         print(node.val, node.is_left, node.index)

# ## # after printing these values, got to know that there is no use of merging ranges for my test case .. xD

def cal_location(seed, layers):
    curr_num = seed
    for layer in layers:
        for m, l, n in layer:
            if l <= curr_num <= l + n:
                value = m + (curr_num - l)
                curr_num = value
                break
    return curr_num

def all_seeds(seeds, it):
    if it == 10:
        arg_two = int(sys.argv[2])
        start = seeds[it] + (arg_two - 1) * (100000000)
        final = seeds[it] + arg_two * (100000000)
        if seeds[it] + seeds[it+1] < final:
            final = seeds[it] + seeds[it+1]
        for elem in range(start, final):
            yield elem
        return
    for elem in range(seeds[it], seeds[it] + seeds[it+1]):
        yield elem

def main() -> None:
    file = open('input.txt', 'r')
    lines = file.readlines()
    file.close()
    seeds_arr = [int(num_str) for num_str in lines[0].strip().split(":")[1].strip().split(" ")]
    total_seeds = sum([seeds_arr[i] for i in range(1, len(seeds_arr), 2)])
    
    print(total_seeds)
    arg_index = int(sys.argv[1])

    print(seeds_arr[arg_index + 1])
    seeds = all_seeds(seeds_arr, arg_index)

    layers = []
    curr_layer = []
    for line in lines[1:]:
        if line.strip() == "":
            continue
        if line.strip().find('map') != -1:
            if curr_layer != []:
                layers.append(curr_layer)
                curr_layer = []
        else:
            curr_layer.append([int(num_str) for num_str in line.strip().split(" ")])

    if curr_layer != []:
        layers.append(curr_layer)
        curr_layer = []
    
    min_location = None
    seeds_count = 0
    for elem in seeds:
        location = cal_location(elem, layers)
        if min_location == None or location < min_location:
            min_location = location
        seeds_count += 1

        if seeds_count % 10000 == 0:
            print(seeds_count, end="\r")
    
    print("\n\n")
    print(min_location)
    return

if __name__ == "__main__":
    main()