# adjacency matrix (인접 행렬) 방식 예제

# 연결이 되어 있지 않은 노드는 무한의 비용이라고 생각하자
INF = 99999999

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)
