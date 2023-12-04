import re

def cal_worth_points(string: str) -> int:
    points = 0
    win, our = string.split(':')[1].split('|')[0].strip(), string.split(':')[1].split('|')[1].strip()
    win_arr = re.sub(' +', ' ', win).split(' ')
    our_arr = re.sub(' +', ' ', our).split(' ')
    our_set = set(our_arr)
    win_arr = set(win_arr)
    for elem in win_arr:
        if elem in our_set:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

def main():
    file = open('input.txt', 'r')
    return_sum = 0
    for line in file.readlines():
        return_sum += cal_worth_points(line.strip())
    print(return_sum)
    return

if __name__ == "__main__":
    main()
