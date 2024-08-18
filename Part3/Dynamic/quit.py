# 다이나믹 문제.. 이전 문제는 오직 숫자의 합의 최댓값이었다면
# 이번엔 시간까지 추가. 어떻게 풀어야 할까

n = int(input())
schedule=[]
for i in range(n):
  schedule.append(list(map(int,input().split())))

print('sche: ', schedule)



