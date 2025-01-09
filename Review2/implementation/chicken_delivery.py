# [구현] [치킨 배달] p.332

from itertools import combinations

n, m = map(int, input().split())

# 입력받는 동시에 어디가 집 or 치킨집인지 기록
chicken, house = [], []
for r in range(n):
  board = list(map(int, input().split()))
  for c in range(n):
    if board[c] == 1: # 집
      house.append((r,c))
    elif board[c] == 2: # 치킨집
      chicken.append((r,c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합을 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수 (조합 중에서 어떤 한 경우가 들어왔을 때)
def get_sum(candidate):
  result = 0
  # 모든 집에 대하여 (house는 전역변수다)
  for hx, hy in house:
    # 가장 가까운 치킨집을 찾자
    temp = 1e9
    for cx, cy in candidate: 
      temp = min(temp, abs(hx-cx) + abs(hy-cy))
    result += temp
  return result # 그 최단거리들의 합을 리턴

# 치킨 거리의 합의 최소를 찾자
result = 1e9
for candidate in candidates:
  result = min(result, get_sum(candidate))

print(result)



