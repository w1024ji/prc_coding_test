# 모험가의 수 n
n = int(input())
# 모험가들의 공포도
data = list(map(int, input().split()))
data.sort()

result=0  # 총 그룹 수
count=0   # 현재 그룹에 포함된 모험가의 수

for i in data:   # 공포도를 낮은 것부터 하나씩 확인
  count+=1       # 현재 그룹에 해당 모험가를 포함
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
    result += 1  # 현재 그룹에 포함된 모험가의 수 초기화
    count=0

print(result)
    