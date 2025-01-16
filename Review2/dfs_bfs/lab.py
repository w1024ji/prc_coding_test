# [DFS & BFS] [연구소]

# n행 m열
n, m = map(int, input().split())

# 새롭게 만들 수 있는 벽의 개수는 3

# 세 개의 메서드를 만들거야. 
# 바이러스를 퍼지게 만드는 함수, 0의 개수를 세는 함수, dfs를 이용해 벽을 설치하면서 모든 경우의 수를 고려하는 함수

original = [] # 원본
temp = [ [0] * m for _ in range(n) ] # 여기저기에 벽을 세우고 시뮬 돌려볼 임시 맵

for _ in range(n):
  original.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maximum = 0

# 바이러스 퍼져라!
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx, ny)

# 안전영역(0) 계산하라!
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# DFS를 이용해 벽을 설치하면서 각 경우의 수에 대한 0의 개수를 비교
def dfs(count):
  global maximum
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = original[i][j] # 원본을 temp로 복제
    # temp가 준비되었으면, 바이러스 전파 시작!
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    maximum = max(maximum, get_score())
    return # 나가기

  # 벽 3개를 아직 다 설치하기 전이라면, 벽 추가
  for i in range(n):
    for j in range(m):
      if original[i][j] == 0:
        original[i][j] = 1
        count += 1
        dfs(count)
        original[i][j] = 0
        count -= 1

dfs(0)
print(maximum)

