def cal_locations(seeds, layers):
    curr_arr = seeds
    next_arr = curr_arr.copy()
    for layer in layers:
        for it, num in enumerate(curr_arr):
            for m, l, n in layer:
                if l <= num <= l + n:
                    value = m + (num - l)
                    next_arr[it] = value
                    break
        curr_arr = next_arr
    return next_arr

def main() -> None:
    file = open('input.txt', 'r')
    lines = file.readlines()
    seeds = [int(num_str) for num_str in lines[0].strip().split(":")[1].strip().split(" ")]
    
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
    
    locations = cal_locations(seeds, layers)
    print(locations)
    print(min(locations))
    return

if __name__ == "__main__":
    main()