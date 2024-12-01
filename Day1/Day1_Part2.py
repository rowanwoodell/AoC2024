left = []
right = []

input = open("input", "r")

for line in input:
    left_ID = int(line[0:5])
    right_ID = int(line[8:13])

    left.append(left_ID)
    right.append(right_ID)

total_similarity = 0

for left_ID in left:
    mult = right.count(left_ID)
    similarity = left_ID * mult
    total_similarity += similarity

print(total_similarity)