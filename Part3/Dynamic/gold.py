# 오른쪽 위 / 오른쪽 / 오른쪽 아래 <- 이 방향들을 먼저 정의할까?
# steps = [(1,-1), (1,0), (1,1)]

import sys

t = int(sys.stdin.readline())
n,m=0,0
gold = []
for _ in range(t):
    # 금광 정보 입력
    n, m = map(int, sys.stdin.readline().split())
    gold_input = list(map(int, sys.stdin.readline().split()))

    for i in range(m): # 열을 기준으로 맵을 만들면 안되나?
        # for j in range(n): # 0 4 8 / 1 5 9 / 2 6 10 / 3 7 11
        gold.append((gold_input[i*0+n], gold_input[i*1+n], gold_input[i*2+n])) # i*0+n, i*1+n, i*2+n

print(gold)
# 채굴자가 얻을 수 있는 금의 최대 크기를 얻는 함수
# 첫 열의 시작을 포함해 m번을 이동할 수 있다
# 열을 한 칸씩 움직이면서 (필수), 최고 숫자를 가진 행을 선택하는 방식
def mining(gold):
  maxes=[]
  for i in range(m):
    maxes.append(max(gold[i]))
  return sum(maxes)