def cal_location(seed, layers):
    curr_num = seed
    for layer in layers:
        for m, l, n in layer:
            if l <= curr_num <= l + n:
                value = m + (curr_num - l)
                curr_num = value
                break
    return curr_num

def all_seeds(seeds):
    for it in range(0, len(seeds), 2):
        for elem in range(seeds[it], seeds[it] + seeds[it+1]):
            yield elem

def main() -> None:
    file = open('input.txt', 'r')
    lines = file.readlines()
    seeds_arr = [int(num_str) for num_str in lines[0].strip().split(":")[1].strip().split(" ")]
    total_seeds = sum([seeds_arr[i] for i in range(0, len(seeds_arr), 2)])
    print(total_seeds)

    seeds = all_seeds(seeds_arr)

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
        # percentage = seeds_count * 100 / total_seeds
        # if percentage == int(percentage):
        #     print(percentage, " completed")

    print(min_location)
    return

if __name__ == "__main__":
    main()