# 고정점 찾기. 원소의 값이 인덱스와 동일할 때

n = int(input())
array = list(map(int, input().split()))

def find_fixed(array, start, end):
  if start>end:
    return None
  mid = (start+end)//2
  
  if array[mid] == mid: # 찾았다면
    return mid
  elif array[mid] > mid:
    return find_fixed(array, start, mid-1)
  else:
    return find_fixed(array, mid+1, end)
  
result = find_fixed(array, 0, n-1)
if result == None:
  print(-1)
else:
  print(result) 