# 행의 개수 n, 열의 개수 m
n,m = map(int, input().split())
array = [ [0]*m for _ in range(n) ] # n행 m열 만들기

# 넣기
for i in range(n):
  array[i] = list(map(int, input().split()))

min_array=[0]*m # 각 행에서 최소 값들만 모을거임

for i in range(n):
  array[i].sort()
  min_array[i] = array[i][0]

print(max(min_array))

