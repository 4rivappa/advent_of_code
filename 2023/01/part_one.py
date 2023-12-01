# ------------------ Part One -----------------

def calculate_calibration_val(string: str) -> int:
    digits = []
    for char in string:
        if 48 <= ord(char) <= 57:
            digits.append(char)
    if len(digits) == 0:
        return 0
    return int(digits[0] + digits[-1])

# ------------------ Part Two -----------------
# rough work - not correct solution (refer part_two.py)

# def check_starts_with(string: str) -> (bool, str, str):
#     digits_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for it in range(len(string)):
#         for iter, word in enumerate(digits_list):
#             if word.startswith(string[it:]):
#                 return True, chr(ord('0') + iter) if word == string[it:] else '-', string[it:]
#     return False, '-', '-'
# def calculate_actual_calibration_val(string: str) -> int:
#     digits = []
#     curr_str = ""
#     for char in string:
#         if 48 <= ord(char) <= 57:
#             is_valid, valid_digit, x = check_starts_with(curr_str)
#             if is_valid and valid_digit != '-':
#                 digits.append(valid_digit)
#             curr_str = ""
#             digits.append(char)
#         else:
#             is_valid, valid_digit, x = check_starts_with(curr_str)
#             if is_valid:
#                 curr_str = char if valid_digit != "-" else x + char
#                 if valid_digit != "-": digits.append(valid_digit)
#             else:
#                 curr_str = char
#         # print(curr_str)
#     is_valid, valid_digit, x = check_starts_with(curr_str)
#     if is_valid and valid_digit != '-':
#         digits.append(valid_digit)
#     if len(digits) == 0:
#         return 0
#     print(digits)
#     return int(digits[0] + digits[-1])
# ---------------------------------------------

def main(file_name: str) -> None:
    file = open(file_name, 'r')
    total_calibration_val = 0
    for line in file.readlines():
        total_calibration_val += calculate_calibration_val(line)
        # value = calculate_actual_calibration_val(line)
    
    print(total_calibration_val)
    return

if __name__ == "__main__":
    main("input.txt")