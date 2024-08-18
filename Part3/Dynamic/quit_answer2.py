# 출처: https://wooono.tistory.com/574
# 1일차에 상담을 진행하는 경우의 최대 이익은, '1일 차의 상담 금액 + 4일부터의 최대 상담 금액'이다.
# 이러한 원리를 이용하여 뒤쪽 날짜부터 거꾸로 계산하자.
# 뒤쪽부터 매 상담에 대하여 '현재 상담 일자의 이윤p[i] + 현재 상담을 마친 일자부터의 최대 이윤dp[t[i] + i]' 를 계산하면 된다
# 이후에 계산된 각각의 값 중에서 최댓값을 출력하면 된다
# dp[i]가 i번째 날부터 마지막 날까지 낼 수 있는 최대 이익이라고 한다면, 점화식은 아래와 같다.
# max_value는 뒤에서부터 계산할 때, 현재까지늬 최대 상담 금액에 해당하는 변수
# dp[i] = max(p[i] + dp[ t[i]+i ], max_value)

import sys

n = int(sys.stdin.readline())

t=[] # 각 상담을 완료하는데 걸리는 기간
p=[] # 각 상담을 완료했을 때 받을 수 있는 금액

dp = [0] * (n+1) # i번째 날부터 마지막 날까지 낼 수 있는 최대 이익

max_value=0

for _ in range(n):
  x,y=map(int, sys.stdin.readline().split())
  t.append(x)
  p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):

  # i번째 날짜에 상담이 가능한 경우
  if (i + t[i] <= n):
    # (현재 상담 날짜의 금액 + 다음 상담 날짜의 누적 금액)과
    # 현재 상담 날짜부터 마지막 날까지 쌓을 수 있는 최대 누적 금액을 비교
    dp[i]=max(p[i] + dp[t[i]+i], max_value)
    print('dp[i]: ', dp[i])
    print('max_value: ', max_value)
    max_value = dp[i]
  # i번째 날짜에 상담이 불가능한 경우
  else:
    print('max_value: ', max_value)
    dp[i] = max_value

print(max_value)

