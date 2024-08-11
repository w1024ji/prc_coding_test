# 스택 예제

stack=[]

# 삽입
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 7이 나왔겠지
stack.append(1)
stack.append(4)
stack.pop() # 4가 나옴

# 최하단 원소부터 출력
print(stack)
print(stack[::-1]) # 최상단 원소부터 출력