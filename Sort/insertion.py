array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i,0,-1): # 인덱스 i부터 1까지 -1씩 더해서 반복하
    if array[j] < array[j-1]: # 내가 더 작으면
      array[j], array[j-1] = array[j-1], array[j] # 자리 바꿔
    else: # 나보다 작네
      break

print(array)