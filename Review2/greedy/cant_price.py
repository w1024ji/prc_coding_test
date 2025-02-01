# [Greedy] 만들 수 없는 금액

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

# 만들 수 없는 금액 1부터 시작
target = 1

for coin in coins:
    if target < coin:
        break
    target += coin

print(target)
