# 숫자의 개수 n, 찾아야 하는 수 x
n, x = map(int, input().split())

# 계수 정렬을 사용해보자!
array=[0] * 10000001 # 1<=N<=1,000,000 이니까

for i in input().split():
  array[int(i)] += 1

print('array: ', array[0:5])

if array[x] != 0:
  print(array[x])
else:
  print(-1)