# 큐 예제
from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft() # 선입선출. 5가 나온다

queue.append(1)
queue.append(4)

queue.popleft() # 2가 나오겠지..

print(queue)
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기. queue 자체를 바꾼다
print(queue)