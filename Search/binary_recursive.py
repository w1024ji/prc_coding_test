# 재귀함수를 이용해 이진 탐색 구현
def binary_search(array, target, start, end):
  if start>end:
    return None
  mid = (start+end) // 2 # 나머지는 버린다
  if array[mid] == target: # 찾았다면
    return mid
  elif array[mid]>target:
    return binary_search(array, target, start, mid-1) # 끝점 변경
  else:
    return binary_search(array, target, mid+1, end) # 시작점 변경

# n(원소의 개수), target(찾고자 하는 문자열)
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다")
else:
  print(result) 

