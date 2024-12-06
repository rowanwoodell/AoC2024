input = open("input", "r")

class Found(Exception): pass

rules = []
updates = []
current_line = 0

while True:
    l = input.readline()
    current_line += 1

    if current_line <= 1176:
        n1 = int(l[0:2])
        n2 = int(l[3:5])
        rules.append([n1, n2])

    elif current_line == 1177:
        continue

    elif current_line <= 1366:
        u = [int(x) for x in l.split(",")]
        updates.append(u)

    else: break

correct_updates = []

for u in updates:
    try:
        for i, x in enumerate(u):
            for y in u[i + 1:]:
                if [x, y] not in rules:
                    raise Found
        correct_updates.append(u)
    except Found:
        pass

sum = 0

for u in correct_updates:
    middle_index = int((len(u) - 1) / 2)
    sum += u[middle_index]

print(sum)
