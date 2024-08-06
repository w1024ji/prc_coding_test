n = int(input()) # N시 59분 59초까지 3이 하나라도 포함되는 모든 경우의 수는?
# n에 3이 포함되지 않은 경우
# n에 3이 포함된 경우: 3, 13, 23

# 다 틀림.

# ...
# 충격적이네 정답을 다시 보니까. 예전에 한 건데 왜 ... 음... 할많하않..

count=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k): # string의 속성을 쓴 풀이
        count+=1

print(count)