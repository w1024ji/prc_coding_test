from collections import deque

def bfs(graph, start, visited):
  queue = deque( [start] )
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 모두 큐에 넣기
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
# 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)