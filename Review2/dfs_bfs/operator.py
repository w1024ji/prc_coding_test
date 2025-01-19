# [DFS_BFS] [연산자 끼워 넣기]

n = int(input())
numbers = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 만약 연산자를 다 썼다면
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add >0:
            add -= 1
            dfs(i+1, now + numbers[i])
            add += 1
        if sub >0:
            sub -= 1
            dfs(i+1, now - numbers[i])
            sub += 1
        if mul >0:
            mul -= 1
            dfs(i+1, now * numbers[i])
            mul += 1
        if div >0:
            div -= 1
            dfs(i+1, int(now / numbers[i]))
            div += 1

dfs(1, numbers[0])

print(max_value)
print(min_value)

