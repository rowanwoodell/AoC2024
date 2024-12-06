input = open("input", "r")

class Found(Exception): pass

rules = []
updates = []
current_line = 0

def quicksort(list, rules):
    if len(list) == 0:
        return []

    if len(list) == 1:
        return list

    pivot = list[0]

    left = []
    right = []

    for x in list[1:]:
        if [x, pivot] in rules:
            left.append(x)
        else:
            right.append(x)

    return quicksort(left, rules) + \
           [pivot] + \
           quicksort(right, rules)


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

incorrect_updates = []

for u in updates:
    try:
        for i, x in enumerate(u):
            for y in u[i + 1:]:
                if [x, y] not in rules:
                    raise Found
    except Found:
        incorrect_updates.append(u)

sum = 0

for u in incorrect_updates:
    correct = quicksort(u, rules)
    
    middle_index = int((len(correct) - 1) / 2)
    sum += correct[middle_index]

print(sum)
