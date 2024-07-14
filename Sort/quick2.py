array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  print(array)
  if len(array) <= 1:
    return array

  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 파트
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 파트

  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))