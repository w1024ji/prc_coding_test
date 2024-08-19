import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split())

# 바이러스 정보 저장
graph=[]
# 바이러스의 추가 정보 저장
data=[]

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하면
    if graph[i][j] != 0:
      # 바이러스 종류, 확산 시간, 행열의 위치
      data.append((graph[i][j], 0, i, j))

# 바이러스를 번호가 낮은 순서대로 정렬
data.sort()
# 바이러스 추가 정보를 큐로 변환
q = deque(data)

s,x,y=map(int, sys.stdin.readline().split())

# 상하좌우
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
  virus, time, i, j = q.popleft()
  if time==s:
    break
  for l in range(4):
    nx=i+dx[l]
    ny=j+dy[l]
    if (0<= nx and nx < n and 0 <= ny and ny < n and graph[nx][ny] == 0):
      # 그래프에 바이러스 확산 표시
      graph[nx][ny] = virus
      # 큐에 삽입
      q.append((virus, time+1, nx, ny))

print(graph[x-1][y-1])