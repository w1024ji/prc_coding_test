import heapq

n,m=map(int, input().split())
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

INF = int(1e9)
start=1
distance =[INF] * (n+1)

def dijkstra(start):
  distance[start]=0
  q=[]
  heapq.heappush(q, (0,start))
  while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
      continue
    for next in graph[node]:
      cost = distance[node] + next[1]
      if cost < distance[next[0]]:
        distance[next[0]] = cost
        heapq.heappush(q, (cost, next[0]))
  # 1번 헛간으로부터 가장 먼 헛간까지의 거리
  max_node=0
  max_dist=0
  max_node_lst=[]
  for i in range(1,n+1):
    if max_dist < distance[i]:
      max_node =i
      max_dist=distance[i]
      max_node_lst=[max_node]
    elif max_dist == distance[i]:
      max_node_lst.append(i)
  print(max_node, max_dist, len(max_node_lst))

dijkstra(start)

