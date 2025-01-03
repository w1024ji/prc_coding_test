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
