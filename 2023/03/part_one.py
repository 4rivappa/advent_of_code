def cal_start_index(string: str, s_index: int) -> (int, int):
    it = s_index
    while it > 0:
        if 48 <= ord(string[it-1]) <= 57:
            it -= 1
        else:
            break
    end_it = it + 1
    while end_it < len(string) and 48 <= ord(string[end_it]) <= 57:
        end_it += 1
    return it, int(string[it:end_it])


def calculate_parts_sum(arr: list[str]):
    numbers_set = set()
    return_sum = 0

    for it in range(len(arr)):
        string = arr[it]
        print(string)
        for s_it in range(len(string)):
            if string[s_it] != "." and not (48 <= ord(string[s_it]) <= 57):
                for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]:
                    new_i = it + i
                    new_j = s_it + j
                    if new_i < 0 or new_i > len(arr)-1 or new_j < 0 or new_j > len(string)-1:
                        continue
                    if 48 <= ord(arr[new_i][new_j]) <= 57:
                        start_index, number = cal_start_index(arr[new_i], new_j)
                        if (new_i, start_index) not in numbers_set:
                            return_sum += number
                            print(new_j)
                            print(start_index, number)
                            numbers_set.add((new_i, start_index))
                        # return_sum += number
                        # print(number)
    
    return return_sum

def main(file_name: str) -> None:
    file = open(file_name, 'r')
    input_arr = []
    for line in file.readlines():
        input_arr.append(line.strip())
    
    answer = calculate_parts_sum(input_arr)
    print(answer)
    return

if __name__ == "__main__":
    main("input.txt")