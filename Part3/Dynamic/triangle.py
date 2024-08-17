# 이 문제도 다이나믹 프로그랭. 점화식을 사용해보도록 해보자.
# 금광 문제랑 비슷하게 또 최댓값 구하기 문제이다.
# 금광의 점화식: dp[i][j] += max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
# 음.. 그렇다면
# 자기자신 += max(위 대각 원소 두개)
# dp[i][j] += max(dp[i-1][j-1], dp[i-1[j]]) 이거 인가?

n = int(input()) # 삼각형의 높이
tri=[]
for i in range(n):
  tri.append(list(map(int,input().split())))

print(tri)

for i in range(1, n):
  for j in range(len(tri[i])): # [8, 1, 0] 이라면 0,1,2를 돌리겠지?
    if j==0: # 왼쪽 위가 없다면
      tri[i][j] += tri[i-1][j]
    elif j==len(tri[i])-1: # 오른쪽 위가 없다면
      tri[i][j] += tri[i-1][j-1]
    else: # 왼쪽, 오른쪽 위가 둘 다 있다면
      tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1])) # 성공!!!
    