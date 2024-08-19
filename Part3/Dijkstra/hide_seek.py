import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) 

# n개의 헛간과 m개의 양방향 통로
n,m=map(int, input().split())
start = 1
graph = [ [] for i in range(n+1) ]
distance = [INF] * (n+1)


# 모든 edge 정보
for _ in range(m):
  a,b = map(int, input().split()) 
  graph[a].append((b,1)) # 비용은 항상 1

def dijkstra(start):
  q=[]
  heapq.heappush(q, (0,start))
  distance[start]=0
  while q: 
    dist, now = heapq.heappop(q) 
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost= dist+i[1] # i[1]은 비용을 뜻한다
      if cost < distance[i[0]]: 
        distance[i[0]] = cost 
        heapq.heappush(q, (cost, i[0])) 

dijkstra(start)

# for i in range(1, n+1):
#   if distance[i] == INF:
#     print("INFINITY")
#   else:
#     print(distance)
len=0
cnt=0
house=20001
for i in range(1, n+1):
  if distance[i] != INF and distance[i] >= len:
    cnt+=1
    len = distance[i]
    if i < house:
      house = i+1
    
    
print(distance)
print(house, len, cnt)
    

