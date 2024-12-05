input = open("input", "r")

input_str = ""

def check(i, str):
    m1 = 0
    m2 = 0
    if str[i + 1] == "u" and str[i + 2] == "l" and str[i + 3] == "(":
        j = 0
        while str[i + 4 + j].isdigit():
            j += 1
        else:
            if j == 0:
                return 0
            elif str[i + 4 + j] == ",":
                m1 = int(str[i + 4 : i + 4 + j])
            else:
                return 0
            
        k = 0
        while str[i + 4 + j + 1 + k].isdigit():
            k += 1
        else:
            if k == 0:
                return 0
            elif str[i + 4 + j + 1 + k] == ")":
                m2 = int(str[i + 4 + j + 1 : i + 4 + j + 1 + k])
                return m1 * m2
            else:
                return 0
    else:
        return 0

def en_dis(i, str, enabled):
    if str[i : i + 4] == "do()":
        return True
    elif str[i : i + 7] == "don't()":
        return False
    else:
        return enabled

for l in input:
    input_str += str(l)

sum = 0
enabled = True

for i, x in enumerate(input_str):
    if (enabled == True) and (x == "m"):
        sum += check(i, input_str)
    
    if x == "d":
        enabled = en_dis(i, input_str, enabled)

print(sum)