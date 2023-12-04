data = \
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("data/day3.txt", 'r') as f:
    data = f.read()

data = data.split("\n")

columns = len(data[0])
rows = len(data) - 1

print(f"{columns}, {rows}")

class Number:
    def __init__(self, x : int, y : int, length: int, value : int):
        self.x = x
        self.y = y
        self.length = length
        self.value = value
        self.is_adjacent = False
    
    def is_adjacent_to(self, x : int, y : int) -> bool:
        within_x = x <= (self.x + self.length + 1) and x >= (self.x - 1)
        within_y = y <= (self.y + 1) and y >= (self.y - 1)
        return within_y and within_x
    
    def __str__(self):
        return f"Value: {self.value}, Location: ({self.x, self.y}), Length: {self.length}, Is Adjacent: {self.is_adjacent}"


numbers = []

symbols = []    # (x, y)

n = Number(7, 5, 2, 58)

print(n.is_adjacent_to(5, 5))
# exit()

for y in range(columns):
    cur_num_str = ""
    cur_num_x = 0
    for x in range(rows):
        c = data[y][x]
        if c.isnumeric():
            cur_num_str += c
        else:
            if cur_num_str != "":
                # Add new number
                numbers.append(Number(cur_num_x, y, len(cur_num_str), int(cur_num_str)))
                cur_num_str = ""
            if c != '.':
                #  We have a symbol
                symbols.append((x, y))
            cur_num_x += 1

for s in symbols:
    for n in numbers:
        if n.is_adjacent_to(s[0], s[1]):
            n.is_adjacent = True

total = 0
for n in numbers:
    print(n)
    if n.is_adjacent:
        total += n.value

print(total)