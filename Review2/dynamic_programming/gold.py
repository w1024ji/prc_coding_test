# [DP] 금광

for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # dp 테이블 초기화!
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
    
    # print('dp 초기화 완료 ', dp)

    # DP 진행. 미리 채워둔 1열을 이용해 2열부터 시작해서 나머지 열들을 채워보자
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 온다면
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽에서 온다면
            left = dp[i][j-1]
            # 왼쪽 아래에서 온다면
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            # 이 중에서 제일 큰 경우를 가지고 dp테이블을 갱신한다
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
            
        
    result = 0

    for i in range(n):
        result = max(result, dp[i][m-1])    # 마지막 열에 있는 값 중에서 제일 큰 값이 답이다

    print(result)


