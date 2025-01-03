# 점수 n을 나누어 왼쪽 부분의 합과 오른쪽의 합이 같으면 상태인가?

n = input() # string으로 받자

first_half = n[: len(n)//2]
second_half = n[len(n)//2 :]

first_sum = 0
second_sum = 0

for i in first_half:
  first_sum += int(i)
for j in second_half:
  second_sum += int(j)

if first_sum == second_sum:
  print('LUCKY')
else:
  print('READY')
  

''' 책 해설 ''

n = input()
length = len(n)
summary = 0     # summary 변수 하나로 합이 동일한지 아닌지 확인한다.
                # 만약 값을 더하고 뺐는데 결과가 0이면 동일하다.
for i in range(length // 2):
  summary += int(n[i])   # n의 인덱스를 사용하자!

for j in range(length // 2):
  summary -= int(n[j])

if summary == 0:
  print("LUCKY")
else:
  print("READY")

'''
