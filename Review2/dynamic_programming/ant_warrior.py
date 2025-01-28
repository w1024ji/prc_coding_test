# [DP] 개미 전사

# 현재를 i라 두고 그 다음이 아니라 i-1이나 i-2를 생각하는게 좋다

n = int(input())

foods = list(map(int, input().split()))

# i-1번째를 얻는 경우, i-2와 ki를 얻는 경우

d = [0] * 100

# bottom-up
# a0과 a1은 초기항
d[0] = foods[0]
d[1] = max(foods[0], foods[1])
# i-1번째를 선택하는 경우, i번째는 선택하지 못하고,
# i-2번째를 선택하는 경우, i번째 선택 가능하다.
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + foods[i])

print(d[n-1])



