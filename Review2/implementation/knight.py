# a는 97이고 h는 104

cur = list(input(str()))
row = int(cur[1])
col = int(ord(cur[0])) - int(ord('a')) + 1

# print(row, col)

# dx = [-2, -2, -1, 1, 2, 2, 1, -1] # col
# dy = [-1, 1, 2, 2, 1, -1, -2, -2] # row

steps = [(-2,-1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]
  # 검사!
  if next_row >= 1 and next_col >=1 and next_row <=8 and next_col <=8:
    result += 1

print(result)
