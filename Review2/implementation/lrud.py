from collections import deque
n = int(input()) 
q = deque(map(str, input().split()))

print(q)

# initial (x,y)
x,y=1,1

while( q ) : # q가 비어있지 않다면
  where = q.popleft()
  if where == 'l' and y > 1:
    y = y-1
  elif where == 'r' and y < n:
    y = y+1
  elif where == 'u' and x > 1:
    x = x-1
  elif where == 'd' and x < n:
    x = x+1
  else: 
    continue

print(x, y)
    
''' 책 해설 ''

n = int(input())
x,y = 1, 1
plans = input().split()

# LRUD에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n: # 채택할 것인지 버릴것인지 결정
    continue
  # 이동 수행
  x, y = nx, ny # 채택한다

print(x, y)

'''
