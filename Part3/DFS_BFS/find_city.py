from collections import deque

# n 도시의 개수, m 도로의 개수, k 최단거리, x 출발 노드
n,m,k,x = map(int, input().split())

# 빈 그래프 먼저 만들고 그 다음에 채운다
graph = [ [] for _ in range(n+1) ]

# 정보 채우기
for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)

def bfs(graph, start, minlen):
  queue = deque([start])
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if minlen[i] == -1:
        minlen[i] = minlen[v] + 1
        queue.append(i)

minlen = [-1] * (n+1) # x 도시에서 다른 도시들까지 최단거리 정보
minlen[x]=0 # 출발 도시는 0

bfs(graph, x, minlen)

check = False
for i in range(1, n+1):
  if minlen[i] == k:
    print(i)
    check=True

if check == False:
  print(-1)



