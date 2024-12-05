input = open("input", "r")

input_str = ""

def match_mul(i, str):
    m1 = 0
    m2 = 0

    if str[i : i + 4] == "mul(":
        # pointer to character immediately following "("
        j = i + 4
        while str[j].isdigit():
            j += 1
        else:
            # next character not a digit
            if j == i + 4:
                return 0
            elif str[j] == ",":
                m1 = int(str[i + 4 : j])
            else:
                return 0
        
        # pointer to character immediately following ","
        k = j + 1
        while str[k].isdigit():
            k += 1
        else:
            # next character not a digit
            if k == j + 1:
                return 0
            elif str[k] == ")":
                m2 = int(str[j + 1 : k])
                return m1 * m2
            else:
                return 0
    else:
        return 0

for l in input:
    input_str += str(l)

sum = 0

for i, x in enumerate(input_str):
    sum += match_mul(i, input_str)

print(sum)