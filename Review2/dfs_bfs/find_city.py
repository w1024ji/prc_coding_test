# [DFS & BFS] [특정 거리의 도시 찾기]
from collections import deque

# n개의 도시, m개의 도로, 최단거리 k, 출발도시 x
n, m, k, x = map(int, input().split())

# n개의 도시 각각을 인덱스라고 생각하도록 (인덱스 0은 만들어지지만 안 쓴다. 그래서 n+1)
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b) # 출발a -> 도착b [[], [2, 3], [3, 4], [], []]


# 모든 도시에 대한 최단 거리 초기화. 출발 도시까지의 거리는 0이다
distance = [-1] * (n+1)
distance[x] = 0 

# BFS
q = deque([x])
while q:
  now = q.popleft()
  # now 도시랑 연결된 인접도시들을 꺼내 (이렇게 써먹으려고 위에서 세팅을 저렇게 함)
  for next_node in graph[now]:
    # 만약 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      distance[next_node] = distance[now] +1 # 최단거리 갱신
      q.append(next_node)

# 최단 거리가 k인 도시 번호 출력
check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if not check:
  print(-1)

