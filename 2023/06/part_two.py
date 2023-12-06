import re

def cal_possible_ways(t, d):
    count = 0
    for curr_t in range(t+1):
        if abs((curr_t)*(t - curr_t)) > d:
            count += 1
    return count

def gen_races(time, dist):
    for it in range(len(time)):
        yield time[it], dist[it]

def main() -> None:
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    time_str = lines[0].strip().split(":")[1].strip()
    time_str = re.sub(" ", "", time_str)
    time = [int(x) for x in time_str.split(" ")]
    dist_str = lines[1].strip().split(":")[1].strip()
    dist_str = re.sub(" ", "", dist_str)
    dist = [int(x) for x in dist_str.split(" ")]
    
    races = gen_races(time, dist)
    return_mul = 1
    for t, d in races:
        ways = cal_possible_ways(t, d)
        return_mul *= ways
    print(return_mul)
    return

if __name__ == "__main__":
    main()