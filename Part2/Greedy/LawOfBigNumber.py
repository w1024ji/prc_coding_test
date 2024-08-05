import time

# 공백으로 구분해서 입력 받기
# n: 배열의 크기
# m: 숫자가 더해지는 횟수
# k: 최대 k번 연속으로 더할 수 있다
n, m, k = map(int, input().split())
# 입력받은 숫자들을 리스트로 만들기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 최종 값
result = 0

while True:
  for i in range(k):
    if m == 0:
      break
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)

end_time = time.time()
print("time : ", end_time - start_time)
