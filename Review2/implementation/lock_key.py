# key와 lock은 2차원 배열로 받는다
key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]

# lock + key 했을 때 lock의 모든 원소가 1이 되어야 한다.
# Brute-Force인가?
# key를 회전하거나 상하좌우로 움직이는 함수를 만들어야 하나?

def rotate_90_degree(a):
  n = len(a)      #행 길이
  m = len(a[0])   #열 길이
  result = [ [0] * n for _ in range(m) ] # 90도 회전한 리스트
  for i in range(n):
    for j in range(m):
      result[j][n - i - 1] = a[i][j]
  
  return result

# 3배 불려놨던 자물쇠의 가운데 부분이 모두 1인지 확인 (모두 1이면 성공한거임)
def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        print('False.')
        return False
  print('True!')
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  
  # lock의 크기를 기존의 3배로 변환
  new_lock = [ [0] * (n*3) for _ in range(n*3) ]
  # 정 가운데에 진짜 lock을 넣는다
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]

  # 4가지 rotation을 확인
  for rotation in range(4):
    key = rotate_90_degree(key) # key 회전!
    for x in range(n*2):
      for y in range(n*2):
        # lock에 key를 끼워 넣기 (합이 1이 되면 맞는거임)
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] += key[i][j]
        if check(new_lock): # 여기에 걸리면 True 리턴하고 끝
          return True
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] -= key[i][j]

  return False # 끝까지 맞지 않으면 False 리턴

print(solution(key, lock))