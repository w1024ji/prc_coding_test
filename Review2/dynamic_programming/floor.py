# [DP] 바닥 공사

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
# 점화식 an = an-1 + (an-2) * 2
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[n])

