# [DFS_BFS] 블록 이동하기 p.355

from collections import deque

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [ [1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    # BFS
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        # (n,n)에 로봇이 도달했다면, 최단거리이므로 리턴
        if (n,n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않았다면, 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)

    return 0    

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과(이동 가능한 위치들)
    pos = list(pos) # 현재 정보를 집합에서 -> 리스트로 변환
    p1_x, p1_y, p2_x, p2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        p1n_x, p1n_y, p2n_x, p2n_y = p1_x+dx[i], p1_y+dy[i], p2_x+dx[i], p2_y+dy[i]
        # 이동하고자 하는 두 칸이 모두 비어있다면
        if board[p1n_x][p1n_y] == 0 and board[p2n_x][p2n_y] == 0:
            next_pos.append( {(p1n_x, p1n_y), (p2n_x, p2n_y)} )
        
    # 로봇이 가로로 있다면
    if p1_x == p2_x:
        # 위로 회전, 또는 아래로 회전
        for i in [-1, 1]:
            # 위 또는 아래 두 칸이 모두 비어있다면
            if board[p1_x + i][p1_y] == 0 and board[p2_x + i][p2_y] == 0:
                next_pos.append( {(p1_x, p1_y), (p1_x + i, p1_y)} )
                next_pos.append( {(p2_x, p2_y), (p2_x + i, p2_y)} )
    # 로봇이 세로로 있다면
    elif p1_y == p2_y:
        # 왼쪽 또는 오른쪽으로 회전
        for i in [-1, 1]:
            # 왼쪽 또는 오른족 두 칸이 모두 비어있다면
            if board[p1_x][p1_y + i] == 0 and board[p2_x][p2_y + i] == 0:
                next_pos.append( {(p1_x, p1_y), (p1_x, p1_y + i)} )
                next_pos.append( {(p2_x, p2_y), (p2_x, p2_y + i)} )
    return next_pos

# example
board = [[0,0,0,1,1], [0,0,0,1,0], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,0,0]]

print(solution(board))



