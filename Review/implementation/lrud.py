n = int(input())
# 2차원 리스트를 만들어야 하나?
# map = [[0]*n for _ in range(n)]
# 맵을 다 만들지 마!!!
plan = map(str, input().split())

# NxN 맵에서 오른쪽으로 움직이면 (x,y) 중에 y가 증가
#           아랫쪽으로 움직이면 (x,y) 중에 x가 증가
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
move_types=['D','U','R','L']

x,y= 1,1 # 출발점

for p in plan:
  nx,ny=0,0
  for i in range(len(move_types)): # 한 단어당 4번씩 돌려준다
    if p == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  x,y=nx,ny

print(x,y)


