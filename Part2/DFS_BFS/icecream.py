n, m = map(int, input().split()) # N x M 

graph = [list(map(int, input())) for _ in range(m)]

def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상하좌우의 위치도 모두 재귀적으로 호출(방문 처리를 위한)
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j):
      result += 1

print(result)