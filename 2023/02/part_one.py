def check_game_possibility(string: str) -> (bool, int):
    if string == "": return 0
    colon_divides = string.split(":")
    left, right = colon_divides[0], colon_divides[1]
    game_number = int(left[5:])

    for draw in right.strip().split(";"):
        draw_count = [0, 0, 0]
        for color_elem in draw.strip().split(","):
            elements = color_elem.strip().split(" ")
            count = int(elements[0].strip())
            color = elements[1].strip()
            if color[0] == "r": 
                draw_count[0] += count
            elif color[0] == "g":
                draw_count[1] += count
            elif color[0] == "b":
                draw_count[2] += count

        if draw_count[0] > 12:
            return False, 0
        if draw_count[1] > 13:
            return False, 0
        if draw_count[2] > 14:
            return False, 0
    return True, game_number

def main(file_name: str) -> None:
    file = open(file_name, 'r')
    total_count = 0
    for line in file.readlines():
        is_possible, value = check_game_possibility(line)
        if is_possible: total_count += value
    
    print(total_count)
    return

if __name__ == "__main__":
    main("input.txt")