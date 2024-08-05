# 배열의 크기 n, 숫자가 더해지는 횟수 k, 연속해서 k번까지만 더할 수 있음
n,m,k = map(int, input().split())

# 배열을 입력받아야지
array = list(map(int, input().split()))

# 첫 번째로 큰 수랑 두 번째로 큰 수만 쓰니까 그 두개만 필요함
array.sort(reverse=True)
first = array[0]
second = array[1]

sum=0 # 합
for i in range(m-m%k):
  sum += first
for i in range(m%k):
  sum += second

print(sum)
  


