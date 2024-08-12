# 스테이지 개수 n
n = int(input())

# 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
stages = list(map(int, input().split()))
print('stages: ', stages )
temp =[]

for i in range(1,n+1):
  participants=0
  for j in range(i, n+1):
    if stages[i] >= i:
      participants+=1
  fail = int(stages.count(i) / participants)
  print('participants: ', participants)
  print('fail: ', fail)
  temp.append((fail, i))

print(temp)
temp.sort(key=lambda x: x[0])

for t in temp:
  print(t[1], end=' ')




