# 모든 공유기들의 간격이 공평하게 설치되게.. 이분 탐색
'''
* 공유기를 설치할 수 있는 최소 간격과 최대 간격을 구한 뒤, 공유기를 가장 공평하게 설치할 수 있는 간격(mid)을 구합니다.
* 첫 번째 집에 공유기를 설치한 뒤, 첫 번째 집에서 나머지 집들 간의 간격을 확인하며, mid 이상으로 떨어져 있는 집을 탐색합니다.
* 첫 번째 집으로부터 mid 이상 떨어진 집을 찾은 경우, 해당 집에 공유기를 설치한 뒤, 해당 집 기준으로 다시 mid 만큼 떨어져있는 집을 탐색합니다.
* 모든 집을 탐색했다면, 공유기 설치 간격을 이분법을 사용해 갱신합니다.
* 현재까지 설치한 공유기의 개수가 아직 C개 이하라면, 기존 간격이 너무 크다는 의미이므로, 기존 간격보다 더 작은 간격으로 갱신합니다.
* 현재까지 설치한 공유기의 개수가 C개 이상이라면, 기존 간격이 너무 작다는 의미이므로, 기존 간격보다 더 큰 간격으로 갱신합니다.
* 가능한 모든 간격들을 탐색할 때까지 이분법 과정을 반복합니다.
* 탐색된 최대 간격을 반환합니다.
'''
n, c = list(map(int, input().split()))

array = []
for _ in range(n) :
  array.append(int(input()))
array.sort()
# start과 end는 거리이다
start = 1                  # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while start<=end:
  mid=(start+end)//2 # # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
  value=array[0]
  count=1
  for i in range(1,n):
    if array[i] >= value + mid: # mid값을 이용해 공유기를 설치
      value = array[i]
      count+=1
  if count>=c:
    start = mid+1
    reslut=mid
  else:
    end=mid-1

print(result)

