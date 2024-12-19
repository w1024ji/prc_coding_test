n = int(input())

count = 0 
# n=0일때 어떻게 해야 하지???
# 해결!! for문의 range() 특성을 까먹지 말자~

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      time = str(i) + str(j) + str(k)
      # print(time)
      if "3" in time:
        count += 1

print(count)
    