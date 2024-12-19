from collections import deque

# n X n 맵 만들기
n = int(input())
maps =[ [0] * n for _ in range(n) ]
apples = int(input())
loc_ap = []
# 사과 위치
for i in range(apples):
  loc_ap.append(list(map(int, input().split())))
# 맵에 사과 위치시키기
for i in range(apples):  
  x,y=loc_ap.pop()
  maps[x-1][y-1]=1    # 사과가 있는 장소는 1

# 벽 만들기(2라고 가정)
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1:
      maps[i][j]=2
    if j==0 or j==n-1:
      maps[i][j]=2
print('maps: ', maps)

# 변환 정보
mvs = int(input())
moves = []
for i in range(mvs):
  moves.append(list(map(str, input().split())))

print('moves: ', moves)

# 초기 위치
x,y,d=0,0,1


# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 몸 길이
body=1
# 뱀의 전체 위치 (큐로 구현?)
queue = deque()
queue.append((x,y)) # (0,0) 큐에 넣어주기

# 머리 방향 돌리기
def turn_left():
  global d
  d -=1
  if d==-1:
    d=3

def turn_right():
  global d
  d +=1
  if d==4:
    d=0

# 먼저 뱀은 몸길이를 늘려 머리를 다음 칸(nx,ny)에 위치시킨다
def stretch(x, y, rl):
  if rl == 'L':
    turn_left()
  elif rl == 'D':
    turn_right()
  nx = x+dx[d]
  ny = y+dy[d]
  return (nx, ny) # 머리가 어디로 움직였는가
  
# 몇 초에 끝나는가?
time=0
nx,ny=0,0
while True:
  time+=1
  for move in moves:
    if time == int(move[0]):
      nx,ny = stretch(x, y, move[1])
    else:
      nx, ny = x+1, y+1
        
  if maps[nx][ny] == 1: # 사과가 있다면
    maps[nx][ny]=0
    body+=1             # 사과 먹고 몸 길어지기
    queue.append((nx,ny))
    x,y=nx,ny
  elif maps[nx][ny] == 0: # 빈 공간이라면
    queue.append((nx,ny))
    queue.popleft()
    x,y=nx,ny
  elif (nx,ny) in queue: # 자기자신이라면
    break
  else:                  # 벽이라면
    break
    
    
print("time: ", time)


