# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # 갱신
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m = map(int, input().split())
parent = [0]*(n+1) # 부모 테이블 초기화
for i in range(1, n+1):
  parent[i] =i

# union 연산을 각각 수행
for i in range(m):
  x,a,b = map(int, input().split())
  if x == 0:
    union_parent(parent, a, b)
  elif x == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')
