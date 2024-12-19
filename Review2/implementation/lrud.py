from collections import deque
n = int(input()) 
q = deque(map(str, input().split()))

print(q)

# initial (x,y)
x,y=1,1

while( q ) : # q가 비어있지 않다면
  where = q.popleft()
  if where == 'l' and y > 1:
    y = y-1
  elif where == 'r' and y < n:
    y = y+1
  elif where == 'u' and x > 1:
    x = x-1
  elif where == 'd' and x < n:
    x = x+1
  else: 
    continue

print(x, y)
    


