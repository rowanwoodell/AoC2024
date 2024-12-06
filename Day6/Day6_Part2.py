input = open("input", "r")

def move(map, checking_loops):
    new_map = map

    if not checking_loops:
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
                    
    else:
        for i, row in enumerate(map):
            for j, x in enumerate(row):
                match x:
                    case "^":
                        if i == 0:
                            new_map[i][j] = "u"
                        elif map[i - 1][j] == "#":
                            new_map[i][j] = ">"
                        elif map[i - 1][j] in ".Xurdl":
                            if map[i - 1][j] == "u":
                                return "LOOPING"
                            new_map[i - 1][j] = "^"
                            new_map[i][j] = "u"
                        return new_map

                    case ">":
                        if j == len(row) - 1:
                            new_map[i][j] = "r"
                        elif map[i][j + 1] == "#":
                            new_map[i][j] = "v"
                        elif map[i][j + 1] in ".Xurdl":
                            if map[i][j + 1] == "r":
                                return "LOOPING"
                            new_map[i][j + 1] = ">"
                            new_map[i][j] = "r"
                        return new_map

                    case "v":
                        if i == len(map) - 1:
                            new_map[i][j] = "d"
                        elif map[i + 1][j] == "#":
                            new_map[i][j] = "<"
                        elif map[i + 1][j] in ".Xurdl":
                            if map[i + 1][j] == "d":
                                return "LOOPING"
                            new_map[i + 1][j] = "v"
                            new_map[i][j] = "d"
                        return new_map

                    case "<":
                        if j == 0:
                            new_map[i][j] = "l"
                        elif map[i][j - 1] == "#":
                            new_map[i][j] = "^"
                        elif map[i][j - 1] in ".Xurdl":
                            if map[i][j - 1] == "l":
                                return "LOOPING"
                            new_map[i][j - 1] = "<"
                            new_map[i][j] = "l"
                        return new_map
    
    return "GUARD GONE"

def check_loops(map):
    while True:
        new_map = move(map, True)
        if new_map == "GUARD_GONE":
            print("gg")
            return 0
        if new_map == "LOOPING":
            return 1
        else:
            map = new_map

map = []

for l in input:
    map.append(list("".join(l.split())))

original_map = map

# we still run the original movement prediction, since any 
# potential loop-enabling obstable must lie on the original 
# path (since we can only add one). so the Xs on the final
# map indicate all our potential obstacle locations.

while True:
    new_map = move(map, False)
    if new_map == "GUARD GONE":
        break
    else:
        map = new_map

potential_obstacles_map = map

# for l in potential_obstacles_map:
#     print("".join(l))

sum = 0

for i, row in enumerate(potential_obstacles_map):
    for j, x in enumerate(row):
        if x == "X":
            map = original_map
            map[i][j] = "#"
            sum += check_loops(map)
            print(sum)

print(sum)