key = [ [0,0,0], [1,0,0], [0,1,1] ]
lock = [ [1,1,1], [1,1,0], [1,0,1] ]
'''
회전 = 행,열을 바꾸기. 즉 x,y를 스위치 위치=(x,y)라면
흠.. key의 돌기 위치만을 따로 빼낸 리스트를 만들어야 하나?
'''
'''
def solution(key, lock):
  kk = [] # key의 돌기 위치 모음
  ll = [] # lock의 홈 위치 모음
  for i in range(len(key)):
    for j in range(len(key)):
      if key[i][j] == 1:
        kk.append((i,j)) 

  for i in range(len(lock)):
    for j in range(len(lock)):
      if lock[i][j] == 0:
        ll.append((i,j)) 

  print("kk: ", kk)
  print("ll: ", ll)

  # 만약 lock의 홈들을 만족시키는가?
  temp = False
  for l in ll:
    if l in kk:
      temp = True

  # 행-열을 스위치 해야하는데..
  if not temp: # temp가 False라면
    for k in kk:
  모르겠다!!!
  return True
'''

# 아래가 모범답안

def rotate_a_matrix_by_90_degree(a):
  n=len(a) # 행 길이
  m=len(a[0]) # 열 길이
  # 0으로 만들어진 2차원 리스트를 새로 만든 다음 90도 돌린 결과를 집어넣기
  result=[ [0]*n for _ in range(m) ]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]

  return result # 수정된 리스트 리턴

# 자물쇠의 가운데 부분이 1이 되면 딱 들어맞는다는 의미
def check(new_lock):
  lock_length = len(new_lock)//3
  for i in range(lock_length, lock_length*2): # 이따 다시 돌아오겠슴
    for j in range(lock_length, lock_length*2):
      if new_lock[i][j] != 1: # 1이 아니라면 들어맞지 않았다는 거임
        return False
  return True

def solution(key, lock):
  n=len(lock)
  m=len(key)
  # 자물쇠의 크기를 기존의 3배로 변환. 아마 인덱스 때문인듯?
  # 0으로 초기화 한 다음에 기존 내용 반영
  new_lock= [ [0]*(n+3) for _ in range(n+3) ]
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]

  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key) # 90도 돌리고
    for x in range(n*2): # n은 lock의 길이
      for y in range(n*2) :
        # 자물쇠에 열쇠 끼워넣어보기
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+i] += key[i][j] # lock이랑 key랑 각 원소끼리 더해서 1이면 들어맞는 거임
        if check(new_lock): # 체크해보기
          return True
        # 체크했는데 실패라면 열쇠 제거
        for i in range(m):
          for j in range(m):
            new_lock[x+i][y+i] -= key[i][j]

  return False
  
if solution(key, lock):
  print('true')
else:
  print('false')
