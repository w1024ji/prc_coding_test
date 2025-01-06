n = int(input()) # nXn의 보드
k = int(input()) # 사과의 개수

board = [ [0] * (n+1) for _ in range(n+1) ] # 보드 만들기
ld = [] # 방향 회전 정보

# 보드에서 사과가 있는 곳은 1로 표시!
for _ in range(k):
  a, b = map(int, input().split())
  board[a][b] = 1

# 방향 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  ld.append((int(x), c))

# 처음에는 오른쪽을 보고 시작하므로 (동 남 서 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direc, c):
  if c == 'L':
    direc = (direc -1) % 4
  else:
    direc = (direc +1) % 4
  return direc

def simulate():
  x, y = 1, 1 # 뱀의 머리 위치
  board[x][y] = 2 # 뱀이 있는 위치는 2로 표시
  direction = 0   # 어디를 보고 있는가? (동0 남1 서2 북3)
  time = 0
  index = 0 # 다음에 회전할 정보
  q = [(int(x), int(y))] # 뱀이 어디어디 위에 있는가에 대한 정보.
  while True:
    # 여기로 가~
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 보드 안에 있고 자기자신과 만나지 않으면
    if 1<=nx and nx <=n and 1<=ny and ny<=n and board[nx][ny] != 2:
      # 사과가 없다면
      if board[nx][ny] == 0:
        board[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0) # 꼬리 움직이기. q 리스트의 제일 앞 부분을 pop한다.
        board[px][py] = 0 # 꼬리 치우고 다시 0 상태로
      # 사과가 있다면
      if board[nx][ny] == 1:
        board[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 자기 몸에 부딪혔다면
    else:
      time += 1
      break

    x, y = nx, ny # 현재 위치 갱신
    time += 1
    if index < l and time == ld[index][0]: # 회전해야 할 시간이면
      direction = turn(direction, ld[index][1])
      index += 1
      
  return time
    
print(simulate())

