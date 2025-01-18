# [DFS_BFS] [괄호 변환]

# 균형잡힌 괄호 문자열의 인덱스 리턴
def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count +=1
        else:
            count -=1
        if count == 0:
            return i

# 올바른지 판단 (True or False)
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count +=1
        else:
            if count ==0:       # )로 시작한다면 False 반환
                return False
            count -=1
    return True

# p를 올바르게 고치는 함수
def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)   # 균형잡힌 괄호의 인덱스 리턴
    u = p[ : index+1]
    v = p[index+1 : ]
    # u가 올바르다면, v만 고치면 된다 -> solution(v)
    if check_proper(u):
        answer = u + solution(v)
    # u가 올바르지 않다면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 괄호를 지운 나머지만 킵한다
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

p = '()))((()'
print(solution(p))

