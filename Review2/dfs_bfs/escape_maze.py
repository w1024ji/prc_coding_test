# [DFS & BFS] [미로 탈출] 
from collections import deque

n, m = map(int, input().split()) # n행, m열

board = []
for i in range(n):
  board.append(list(map(int, input())))

# 괴물이 있는 부분이 0, 없는 부분이 1
# 탈출하는데 움직이는 최소 칸의 개수는?

# (0,0)에서 특정 구간까지 가는데 필요한 (최소)칸의 개수를 board에 다 적자!

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 모든 방향 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or nx >=n or ny<0 or ny>=m:
        continue
      if board[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우(1인 경우)에만 최단 거리 기록!!
      if board[nx][ny] == 1:
        board[nx][ny] = board[x][y] + 1
        queue.append((nx, ny))

  return board[n -1][m -1] # 맨 오른쪽 아래 (탈출구 위치)의 숫자를 리턴

print(bfs(0, 0))
  