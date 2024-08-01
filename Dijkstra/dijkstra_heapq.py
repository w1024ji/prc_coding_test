import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미. 10억이다.

# 노드의 개수, 간선의 개수
n,m = map(int, input().split())
# 시작 노드 번호 
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 인접 리스트(adjacency list)를 사용해 그래프를 표현했다.
graph = [ [] for i in range(n+1) ]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 edge 정보
for _ in range(m):
  a,b,c = map(int, input().split()) # a노드에서 b노드로 가는 비용이 c
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0,start))
  distance[start]=0
  while q: # 큐가 비어있지 않으면
    dist, now = heapq.heappop(q) # 거리, 노드가 리턴된다(우선순의가 젤 높은)
    # 현재 큐에서 꺼낸 노드 now의 최단 거리(dist)가 
    # 이미 알고 있는 최단 거리(distance[now])보다 큰 경우, 해당 노드를 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost= dist+i[1] # i[1]은 비용을 뜻한다
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]: # i[0]은 노드. 즉 distance[i[0]]은 현재 시작 노드에서 i[0]노드까지의 최단 거리
        distance[i[0]] = cost # 갱신
        heapq.heappush(q, (cost, i[0])) # 갱신

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance)
