n, m = map(int, input().split())

# d는 방문한 위치를 저장하기 위한 맵이다. 0으로 초기화
d = [[0] * m for _ in range(n)] # n행 x m열인 맵을 만든다

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 위치 방문 처리

# 전체 맵 정보
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 
# dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -2:
    direction = 3

# 시뮬레이션 시작
count = 1     # 몇 칸을 움직였는가 (현재 위치 아까 칠함)
turn_time = 0
while True:
  # 자 이제 회전하고 움직여보자
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 만약 아직 가보지 않은 칸이라면 (즉, 육지이면서 아직 방문하지 않았다면)
  if d[nx][ny] == 0 and array[nx][ny] == 0: 
    d[nx][ny] = 1
    x = nx
    y = ny
    count+=1
    turn_time = 0
    continue
  else:
    turn_time += 1

  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있어?
    if array[nx][ny] == 0:
      x = nx
      y = ny
    else: # 아니
      break
    turn_time = 0

print(count)


  
