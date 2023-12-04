import re

def cal_worth_points(string: str) -> int:
    count = 0
    win, our = string.split(':')[1].split('|')[0].strip(), string.split(':')[1].split('|')[1].strip()
    win_arr = re.sub(' +', ' ', win).split(' ')
    our_arr = re.sub(' +', ' ', our).split(' ')
    win_arr = set(win_arr)
    for elem in our_arr:
        if elem in win_arr:
            count += 1
    return count

def main():
    file = open('input.txt', 'r')
    return_sum = 0
    scores = []
    for line in file.readlines():
        scores.append(cal_worth_points(line.strip()))
    occur_count = [1]*len(scores)
    for it, score in enumerate(scores):
        count = score
        itt = it + 1
        while count > 0 and itt < len(scores):
            occur_count[itt] += occur_count[it]
            count -= 1
            itt += 1
    final_score = 0
    for it in range(len(scores)):
        # final_score += scores[it] * occur_count[it]
        final_score += occur_count[it]
    print(final_score)
    return

if __name__ == "__main__":
    main()
