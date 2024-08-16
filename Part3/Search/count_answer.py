# 함수 두 개를 만든다. 
# x 중 맨 앞 x의 인덱스를 구하는 함수와
# 맨 뒤 x의 인덱스를 구하는 함수

def first(array, target, start, end):
  if start>end:
    return None
  mid = (start+end) // 2
  # 인덱스가 0이거나 앞에 있는 원소가 다르다면 && x라면
  if (mid==0 or target>array[mid-1]) and array[mid]==target: 
    return mid
  # 앞으로 최대한 당겨야 하니까 =등호도 넣어준
  elif array[mid]>=target:
    return first(array, target, start, mid-1) 
  else:
    return first(array, target, mid+1, end)

def last(array, target, start, end):
  if start>end:
    return None
  mid = (start+end) // 2
  if (mid==n-1 or target<array[mid+1]) and array[mid]==target:
    return mid
  elif array[mid]>target:
    return last(array, target, start, mid-1) 
  else:
    return last(array, target, mid+1, end)

def count_by_value(array, x):
  n = len(array) 
  a = first(array, x, 0, n-1)
  if a == None: # 수열에 x가 없으면
    return 0
  b = last(array, x, 0, n-1)
  return (b-a+1)

# n개의 원소와 타겟 x
n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)