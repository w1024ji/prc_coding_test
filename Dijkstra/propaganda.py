import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미. 10억이다.

# 노드, 간선, 시작노드
n, m, start = map(int, input().split())

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

# 도달할 수 있는 노드의 개수
count=0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance =0
print(distance)
for d in distance:
  # 도달할 수 있는 노드인 경우
  if d!= INF:
    count+=1
    max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1
print(count-1, max_distance)