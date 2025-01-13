# [DFS & BFS] [음료수 얼려 먹기] p.149

# 행, 열
n, m = map(int, input().split())

ice = []
for i in range(n):
  ice.append(list(map(int, input())))

def dfs(x, y):
  # 범위 벗어나면 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if ice[x][y] == 0: # 아직 방문하지 않았다면
    ice[x][y] = 1
    # 상하좌우의 위치도 재귀적으로 호출!!
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
    
  return False

# 모든 위치에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j):
      result += 1

print(result)

