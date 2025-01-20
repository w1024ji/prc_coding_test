# [DFS_BFS] 감시 피하기

from itertools import combinations

n = int(input())
board = [] # 복도 정보
teachers = [] # 선생님들의 위치 정보
spaces = [] # 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님들 위치 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
        # 빈 공간 위치 저장
        if board[i][j] == 'X':
            spaces.append((i,j))

# 왼, 오, 위, 아래로 감시 진행 (학생 발견: True, 미발견: False)
def watch(x, y, direction):
    # 왼쪽으로 쭉 보기
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1                  # 'X'인 경우엔 y만 줄이고 다시 반복
    # 오른쪽으로 쭉 보기
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽으로 쭉 보기
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽으로 쭉 보기
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return False

# 장애물 설치해보고, 학생이 한 명이라도 감지되는가?
def process():
    for x,y in teachers:        # 선생님의 위치
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False 

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x,y in data:
        board[x][y] = 'O'
    # 선생이 학생을 못 찾는 경우
    if not process():
        find = True
        break
    # 원상복귀
    for x,y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")

