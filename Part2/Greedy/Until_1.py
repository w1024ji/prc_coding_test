# n은 숫자. k로 나눌 수 있는가?
n, k = map(int, input().split())
# 연산 횟수
count = 0

while True:
  if n % k == 0:
    while True:
      n /= k
      count += 1
      if n == 1:
        break
  n -= 1
  count += 1
  if n ==1:
    break

print(count)