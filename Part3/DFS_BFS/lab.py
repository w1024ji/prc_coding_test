# 세로 n, 가로 m
n,m=map(int, input().split())

data = [] # 초기 맵 리스트
temp = [ [0] * m for _ in range(n) ] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트 - 상하좌우 -
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result=0

# dfs 이용
def virus(x,y):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    # 상 하 좌 우 중에서 바이러스가 퍼질 수 있는 경우
    if nx >=0 and nx<n and ny >=0 and ny<m:
      if temp[nx][ny] ==0:
        # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
        temp[nx][ny]=2
        virus(nx,ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
  score=0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# dfs를 이용해 울타리를 설치하면서, 매번 안전영역의 크기 계산. 그리고 최대경우를 선택
def dfs(count):
  global result
  # 울타리가 3개 설치되었다면
  if count ==3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j] # temp가지고 시뮬 돌려보기
    # 각 바이러스 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j]==2:
          virus(i,j)
    # 안전 영역의 최댓값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치. 울타리를 설치할 수 있는 모든 경우의 수를 고려. 
  for i in range(n):
    for j in range(m):
      if data[i][j] ==0:
        data[i][j]=1
        count+=1
        dfs(count)
        data[i][j]=0  # 이건 뭘까? 원상태로 돌리기?
        count-=1

dfs(0)
print(result)

    

# 전체 그래프에서 0의 개수를 세서 출력