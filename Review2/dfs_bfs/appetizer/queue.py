# 큐 예제

from collections import deque

# queue 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 오른쪽에서 들어가 왼쪽에서 나온다고 생각하자!
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꿔보기
print(queue)

