# N(떡의 개수), N(요청한 떡의 길이)
n,m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이
array = list(map(int, input().split()))

start=0
end=max(array)

# 이진 탐색 수행(loop)
result=0
while(start<=end):
  total=0
  mid=(start+end)//2
  for x in array:
    if x>mid: # 잘랐을 때의 떡의 양 계산
      total += x-mid
  # 얻은 떡의 양이 기준보다 부족한 경우
  if total < m:
    end=mid-1
  else:
    result=mid # 세이브포인트!!
    start=mid+1

print(result)