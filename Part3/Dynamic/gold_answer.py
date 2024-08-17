# 테스트 케이스
for tc in range(int(input())):
  n,m=map(int, input().split())
  array=list(map(int,input().split()))
  # dp 테이블
  dp=[]
  index=0
  for i in range(n):
    dp.append(array[index:index+m])
    index+=m
    print('dp: ', dp)
  # 다이나믹 프로그래밍 진행
  for j in range(1,m): # 열m을 기준으로. 1번째 열부터 시작
    for i in range(n):
      # 왼쪽 위에서 온다면
      if i==0: # 경계 바깥이므로
        left_up=0
      else:
        left_up=dp[i-1][j-1]
      # 왼쪽 아래에서 온다면
      if i==n-1: # 경계 바깥이므로
        left_down=0
      else:
        left_down=dp[i+1][j-1]
      # 왼쪽에서 온다면
      left = dp[i][j-1]

      # 제일 중요한 부분!!! 점화식!
      dp[i][j] = dp[i][j] + max(left_up, left, left_down)
  
  result=0
  for i in range(n):
    result=max(result, dp[i][m-1])
  print(result)
        