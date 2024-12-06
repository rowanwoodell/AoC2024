input = open("input", "r")

ws = []

for l in input:
    ws.append("".join(l.split()))

def find_x_mas(i, j, ws):
    try:
        if ws[i + 1][j + 1] == "A":
            corners = [
                ws[i    ][j    ],
                ws[i    ][j + 2],
                ws[i + 2][j + 2],
                ws[i + 2][j    ]
            ]
            corners = "".join(corners)
            match corners:
                case "MMSS" | "MSSM" | "SSMM" | "SMMS":
                    return 1
                case _: return 0
        else: return 0
    except: return 0

sum = 0

for i, l in enumerate(ws):
    for j in range(len(l)):
        sum += find_x_mas(i, j, ws)

print(sum)