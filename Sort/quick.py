array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  print(array)
  if start >= end:
    return
  pivot = start
  left = start+1
  right = end
  while left <= right:
    # left쪽에서 피벗보다 큰 수가 나올때까지 ㄱㄱ
    while left <= end and array[left] <= array[pivot]:
      left +=1
    # right쪽에서 피벗보다 작은 수가 나올때까지 반복!
    while right > start and array[right] >= array[pivot]:
      right -=1
    if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 left랑 right랑 교체!
      array[left], array[right] = array[right], array[left]

  # 분할 완료! -> 왼쪽, 오른쪽으로 나눠서 다시 시작(재귀)
  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)