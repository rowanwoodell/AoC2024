input = open("input", "r")

def is_safe(levels):
    inc = None

    for i in range(len(levels) - 1):
        diff = levels[i] - levels[i + 1]

        if diff == 0 or diff > 3  or diff < -3:
            break

        elif diff > 0 and diff < 4:
            if i == 0:
                inc = True
            elif inc == False:
                break

        elif diff < 0 and diff > -4:
            if i == 0:
                inc = False
            elif inc == True:
                break
    else:
        return 1
    
    return 0

sum = 0

for line in input:
    levels = [int(x) for x in line.split()]
    sum += is_safe(levels)
    
print(sum)
    

    

            
