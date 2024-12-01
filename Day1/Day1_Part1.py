left = []
right = []

input = open("input", "r")

for line in input:
    left_ID = int(line[0:5])
    right_ID = int(line[8:13])

    left.append(left_ID)
    right.append(right_ID)

left.sort()
right.sort()

total_distance = 0

for left_ID, right_ID in zip(left, right):
    distance = abs(left_ID - right_ID)
    total_distance += distance

print(total_distance)