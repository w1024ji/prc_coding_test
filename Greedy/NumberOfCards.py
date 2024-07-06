# n은 행, m은 열
n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
  data[i].sort()  
  small = data[i][0]
  if i == 0 or small > result:
    result = small

print(result)