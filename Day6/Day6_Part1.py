input = open("input", "r")

def move(map):
    new_map = map.copy()
    for i, row in enumerate(map):
        for j, x in enumerate(row):
            match x:
                case "^":
                    if i == 0:
                        new_map[i][j] = "X"
                    elif map[i - 1][j] == "#":
                        new_map[i][j] = ">"
                    elif map[i - 1][j] in ".X":
                        new_map[i - 1][j] = "^"
                        new_map[i][j] = "X"
                    return new_map

                case ">":
                    if j == len(row) - 1:
                        new_map[i][j] = "X"
                    elif map[i][j + 1] == "#":
                        new_map[i][j] = "v"
                    elif map[i][j + 1] in ".X":
                        new_map[i][j + 1] = ">"
                        new_map[i][j] = "X"
                    return new_map

                case "v":
                    if i == len(map) - 1:
                        new_map[i][j] = "X"
                    elif map[i + 1][j] == "#":
                        new_map[i][j] = "<"
                    elif map[i + 1][j] in ".X":
                        new_map[i + 1][j] = "v"
                        new_map[i][j] = "X"
                    return new_map

                case "<":
                    if j == 0:
                        new_map[i][j] = "X"
                    elif map[i][j - 1] == "#":
                        new_map[i][j] = "^"
                    elif map[i][j - 1] in ".X":
                        new_map[i][j - 1] = "<"
                        new_map[i][j] = "X"
                    return new_map
    

    return "GUARD GONE"

map = []

for l in input:
    map.append(list("".join(l.split())))

while True:
    new_map = move(map)
    if new_map == "GUARD GONE":
        break
    else:
        map = new_map

sum = 0

for row in map:
    sum += row.count("X")

print(sum)