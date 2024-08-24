'''
# n열, m행
n,m=map(int, input().split())
# (x,y)에서 d를 바라보고 있는 캐릭터
x,y,d=map(int, input().split())
graph=[]
for i in range(m):
  graph.append(list(map(int, input().split())))
  
print('graph: ', graph)

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

# 메뉴얼 함수를 만들자. 어떤 인자들이 필요할까?
def manual(graph, x, y, d):
  # 왼쪽 방향으로 돌리기
  if d == 0:
    d+=3
  else:
    d-=1
  # 가보지 않은 칸이 없다면 1단계로
  nx,ny=0,0
  for i in range(4): 
    nx = x + dx[i]
    ny = y + dy[i]
  if graph[nx][ny]==1: 
    pass


아직 더 연습이 필요한 듯 하다... 아래에 정답
'''

n,m=map(int, input().split())
visited=[ [0] * m for _ in range(n) ]
x,y,d = map(int, input().split())
visited[x][y]=1 # 현재 위치를 방문 처리

graph=[]
for i in range(n):
  graph.append(list(map(int, input().split())))

# 북 동 남 서.
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn_left():
  global d
  d -=1
  if d==-1:
    d=3

# 시뮬레이션 시작
count=1 # 현재 위치를 이미 칠했으니 1로 시작. 방문한 칸의 수를 의미
turn_time=0
while True:
  turn_left()
  # 북동남서 순으로 돌게 된다.
  nx = x+dx[d]
  ny = y+dy[d]
  if visited[nx][ny]==0 and graph[nx][ny]==0: # 아직 안 가봤는가? 육지인가?
    visited[nx][ny]=1     # 가봄
    x,y=nx,ny             # 위치 옮기고
    count+=1
    turn_time=0           # 초기화
    continue
  else: # 회전했는데 갈 수 있는 칸이 없거나 바다라면
    turn_time+=1

  if turn_time==4: # 다 돌았는데 갈 수 없다면
    nx = x-dx[d]
    ny = y-dy[d]
    # 뒤로 갈 수 있다면 이동
    if graph[nx][ny]==0:
      x,y=nx,ny
    else:
      break # 루프 탈출
    turn_time=0

print(count)
    