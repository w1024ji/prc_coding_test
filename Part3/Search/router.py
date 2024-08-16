# 1' 2' 3 4' 5 6 7 8' 9'
# 
n,c = map(int, input().split())
array =[]
for i in range(n):
  array.append(int(input()))

array.sort() # 1 2 4 8 9
# 최대한 중앙값에 가까운 숫자를 그 다음 공유기 장소로 잡아야 한다
# 그러면 그 숫자를 반환하는 함수가 필요.
mid_arr = []
def medium(array, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  medium = (array[start]+array[end]) // 2 # 5
  if array[mid] == medium: # 찾았다면
    return mid
  elif array[mid]>:
    return medium(array, start, mid-1) 
  else:
    return medium(array, mid+1, end) 

# 공유기가 두개인 경우와 세개 이상인 경우로 나누자
if c == 2:
  print(n-2)
elif c == n:
  print(0)
else:
  c -=2
  while c!=0:
    mid_arr.append(medium(array, 0, n-1))