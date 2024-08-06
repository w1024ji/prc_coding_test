loc = input()
row = loc[0] # 행 x
col = loc[1] # 열 y
# 열을 숫자로 변환
array=['0', 'a','b','c','d','e','f','g','h']
for arr in array:
  if row == arr:
    row = array.index(arr)

print(row, col)
row,col = int(row), int(col)

dx=[1,-1,-1,1,2,-2,2,-2]
dy=[2,-2,2,-2,1,-1,-1,1]
nx,ny=0,0
count=0
for i in range(8):
  nx = row + dx[i]
  ny = col + dy[i]
  if nx>=1 and ny>=1 and nx<=8 and ny<=8:
    count+=1

print(count) # 이것도 잘 작동하긴 함..

