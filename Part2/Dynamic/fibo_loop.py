# for문으로 피보나치 만들기 - 보텀업 다이나믹 프로그래밍 -

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*100

# 첫 번째와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 11

for i in range(3, n+1):  # d[3]부터 하나씩 채워나가는 건가
  d[i] = d[i-1] + d[i-2] 

print(d[n])