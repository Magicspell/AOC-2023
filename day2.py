data = \
"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open("data/day2.txt", "r") as f:
    data = f.read()

data = data.split('\n')

MAXIMUMS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# Returns whether it is possible to have those colors with the given maximums
def parse_color(string : str) -> bool:
    string_data = string.split(" ")
    number = int(string_data[0])
    color = string_data[1]

    return number <= MAXIMUMS[color]

# Returns the number and color string associated with the color.
def parse_color_pt2(string : str) -> (str, int):
    string_data = string.split(" ")
    number = int(string_data[0])
    color = string_data[1]

    return color, number

def part1() -> int:
    total = 0
    for l in data:
        line_data = l.split("Game ")[1].split(": ")
        id = int(line_data[0])
        rounds = line_data[1].split("; ")
        game_is_possible = True
        for r in rounds:
            colors = r.split(", ")
            for c in colors:
                if not parse_color(c): game_is_possible = False
        if game_is_possible: total += id
    return total

def part2() -> int:
    total = 0
    for l in data:
        line_data = l.split("Game ")[1].split(": ")
        id = int(line_data[0])
        rounds = line_data[1].split("; ")

        minimums = {
            "red": None,
            "green": None,
            "blue": None
        }

        for r in rounds:
            colors = r.split(", ")
            for c in colors:
                color_data = parse_color_pt2(c)
                color = color_data[0]
                number = color_data[1]
                if minimums[color] == None or number > minimums[color]:
                    minimums[color] = number
            
        total += minimums["red"] * minimums["green"] * minimums["blue"]
    return total

# Should be 2268 for part 1, 63542 for part 2.
print(part1())
print(part2())