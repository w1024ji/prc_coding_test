# [DFS_BFS] [경쟁적 전염]
from collections import deque

n, k = map(int, input().split())
graph = []
data = [] # 바이러스에 대한 정보

for i in range(n):
  graph.append(list(map(int, input().split())))
  # 방금 입력된 i행에 있는 바이러스를 따로 적어두자
  for j in range(n):
    if graph[i][j] != 0:
      # 바이러스의 (종류, 시간, 위치x, 위치y)
      data.append((graph[i][j], 0, i, j))

# 작은 바이러스부터 증식하므로 
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
  virus, s, x, y = q.popleft()
  if s == target_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if graph[nx][ny] == 0: 
        graph[nx][ny] = virus # 바이러스 전파!
        q.append((virus, s+1, nx, ny)) # 큐에 새로운 바이러스에 대한 정보 넣기


# 바이러스 다 퍼진 뒤에 (target_x, target_y)의 바이러스는?
print(graph[target_x -1][target_y -1])

