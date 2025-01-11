# adjacency list (인접 리스트) 방식 예제
# linked list를 이용해 구현한다. 
# 하지만 파이썬은 리스트 자료형이 append()와 메서드를 제공하므로 단순히 2차원 리스트를 이용하면 된다.

# row가 3개인 2차원 리스트로 인접 리스트 표현
graph = [ [] for _ in range(3) ]

# node 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append( (1, 7) )
graph[0].append( (2, 5) )
# node 1
graph[1].append( (0, 7) )
# node 2
graph[2].append( (0, 5) )

print(graph)
