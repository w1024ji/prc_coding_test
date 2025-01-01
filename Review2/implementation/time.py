n = int(input())

count = 0 
# n=0일때 어떻게 해야 하지???
# 해결!! for문의 range() 특성을 까먹지 말자~

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      time = str(i) + str(j) + str(k)
      # print(time)
      if "3" in time:
        count += 1

print(count)

''' 책 해설 ''
-- 이런 유형은 완전 탐색 Brute Forcing 유형으로 분류되기도 한다.
    -- 완전 탐색은 알고리즘은 비효율적인 시간 복잡도를 가지고 있어서 
    -- 탐색해야 할 전체 데이터의 개수가 100만 개 이하일 때 사용하면 적절하다

h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)

'''
