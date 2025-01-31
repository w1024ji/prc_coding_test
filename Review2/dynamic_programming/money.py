# [DP] 효율적인 화폐 구성

n, m = map(int, input().split())

numbers = []
for i in range(n):
    numbers.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

# dp 테이블을 채울 시간~
for i in range(n):
    for j in range(numbers[i], m + 1):
        # 만약 (i-k)원을 만드는 방법이 존재한다면
        if d[j - numbers[i]] != 10001:
            d[j] = min(d[j], d[j - numbers[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


