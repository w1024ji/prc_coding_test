# set 자료형으로 풀기
n = int(input())
array = set(map(int, input().split())) # 부품 번호를 set 자료형에 기록

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
