import regex as re
import math

data ="""\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\
"""

with open("./data/day4.txt", 'r') as f:
    data = f.read()

data = data.split('\n')

re_start = re.compile(r".*:\s+")
re_pipe = re.compile(r"\s+\|\s+")
re_ws = re.compile(r"\s+")


def part2():
    mults = [0] * len(data)
    i = 0
    total = 0
    for l in data:
        l = re_start.sub("", l)
        l = re_pipe.split(l)
        win_nums = [int(n) for n in re_ws.split(l[0])]
        drawn_num = [int(n) for n in re_ws.split(l[1])]

        found_count = 0
        for n in drawn_num:
            if n in win_nums:
                found_count += 1
        
        mults[i] += 1
        for m in range(found_count):
            mults[i + m + 1] += mults[i]
        total += mults[i]
        i += 1
    
    print(mults)
    print(total)

def part1():
    total = 0
    for l in data:
        l = re_start.sub("", l)
        l = re_pipe.split(l)
        win_nums = [int(n) for n in re_ws.split(l[0])]
        drawn_num = [int(n) for n in re_ws.split(l[1])]

        found_count = 0
        for n in drawn_num:
            if n in win_nums:
                found_count += 1

        points = math.pow(2, found_count - 1) if found_count > 0 else 0
        total += int(points) 

    print(f"Part 1 Total: {total}")

part2()