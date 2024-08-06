# 볼링공의 개수 n, 무게 m
n,m= map(int, input().split())
# 볼링공들 bolls
bolls = list(map(int, input().split()))
bolls.sort()

num=0
# 종류와 개수로 나눠서 생각해야 하나?
for i in range(n-2): # 최대 몇 번 뽑을 수 있는가 - k
  num += len(bolls) - (i+1)
  # 자신과 같은 무게라면 무시
  # 나랑 같은 무게인게 뒤에 몇 개가 있는가?(cnt)
  cnt=0
  for j in range(i+1, n-1):
    if bolls[i] == bolls[j]:
      cnt+=1
  num-=cnt # 일단 다 더하고 같은 무게인 공의 수를 빼주자

print(num) # 성공!

