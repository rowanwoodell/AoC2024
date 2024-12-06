input = open("input", "r")

ws = []

word   = "XMAS"
word_r = "SAMX"

for l in input:
    ws.append("".join(l.split()))

# reflect the original wordsearch along the main diagonal, i.e.
# \...
# .\..
# ..\.
# ...\

ws_reflected = [""] * len(ws)

for i in range(len(ws[0])):
    for j in range(len(ws)):
        ws_reflected[j] += ws[i][j]

# rotate the original wordsearch 45 degrees cw and acw
diagonal_size = (len(ws) * 2 - 1)
ws_rotated_cw  = [""] * diagonal_size
ws_rotated_acw = [""] * diagonal_size

for i in range(diagonal_size):
    for j in range(i + 1):
        try:
            ws_rotated_cw[i]  += ws[i - j][j]
            ws_rotated_acw[i] += ws[j][-(i - j + 1)]
        except:
            continue

sum = 0

for l in ws:
    sum += l.count(word)
    sum += l.count(word_r)

for l in ws_reflected:
    sum += l.count(word)
    sum += l.count(word_r)

for l in ws_rotated_cw:
    sum += l.count(word)
    sum += l.count(word_r)

for l in ws_rotated_acw:
    sum += l.count(word)
    sum += l.count(word_r)

print(sum)