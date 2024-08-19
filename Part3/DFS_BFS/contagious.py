# nXn 크기의 시험관. 1번부터 k번까지의 바이러스 종류
n,k=map(int, input().split())
data=[]
for _ in range(n):
  data.append(list(map(int, input().split())))
print('data: ', data)
s,x,y=map(int, input().split()) # s초 후에 (x,y)의 숫자는? (행, 열)

# 4가지 이동 방향에 대한 리스트 - 상하좌우 -
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(k):
  for i in range(n):
    for j in range(n):
      if data[i][j]==k: # 만약 k 바이러스라면 전파
        virus(i,j,k)
        return

# (x,y)에서 상하좌우로 바이러스 전파하는 메서드
def virus(x,y,k):
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx >=0 and nx<n and ny >=0 and ny<n:
      if data[nx][ny] ==0:
        data[nx][ny]=k

# 이중 for문을 써야하는건가
for i in range(s):
  # 매개변수로 받은 숫자의 dfs 실행
  for j in range(1, k+1): # 1번 바이러스부터 k번 바이러스까지
    dfs(j)

print('data: ', data)

if data[x-1][y-1] == 0:
  print(0)
else:
  print(data[x-1][y-1])