with open("data/day1.txt", "r") as f:
    data = f.read().split('\n')

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

FORWARDS = 0
BACKWARDS = 1

def find_digit(line : str, direction : int) -> int:
    ret = 0
    cur_word = ""
    need_to_break = False
    if direction == BACKWARDS: line = line[::-1]
    for c in line:
        if need_to_break: break
        if c.isnumeric():
            ret = int(c)
            break
        else:
            if direction == FORWARDS: cur_word += c
            else: cur_word = c + cur_word
            for d in DIGITS.keys():
                if d in cur_word:
                    ret = DIGITS[d]
                    need_to_break = True
                    break
    return ret

total = 0
for l in data:
    first_dig = find_digit(l, FORWARDS)
    last_dig = find_digit(l, BACKWARDS)
    # print(f"First: {first_dig}, Last: {last_dig}")
    total += (first_dig * 10) + last_dig

print(total)    # Should be 54265