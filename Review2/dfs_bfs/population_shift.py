# [DFS_BFS] [인구 이동]

from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발, 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    united = []             # (x,y)의 위치와 연결된 나라 정보를 담는 리스트
    united.append((x,y))
    # BFS
    q = deque()
    q.append((x,y))
    union[x][y] = index     # 현재 연합 번호
    summary = graph[x][y]
    count = 1

    while q:
        x,t = q.popleft()
        for i in range(4):  # 현재 위치에서 4가지 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l <= abs(graph[x][ny] - graph[x][y]) <= r:
                    q.append((nx, n))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    
    # 연합 국가끼리 인구 분배
    for i,j in united:
        graph[i][j] = summary // count

    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [ [-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:       # 만약 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index +=1
    # 모든 이동이 끝났다면
    if index == n*n:
        break

    total_count += 1

print(total_count)
