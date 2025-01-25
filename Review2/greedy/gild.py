# [Greedy] 모험가 길드

n = int(input())
fears = list((map(int, input().split())))

fears.sort()    # 오름차순으로 정렬

# 'i번째까지의 사람 수' >= 'i번째의 공포도' 이어야지만 길드에 포함시킬 수 있다
result = 0  # 길드 수
count = 0   # 지금 몇 명 들어있는가

for i in fears:
    count += 1      # 일단 포함시켜봐
    if count >= i:  # 조건에 맞는가
        result += 1
        count = 0   # 리셋

print("길드 수: ", result)        

