# 집의 수 n
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값
print(data[(n-1) // 2])
    


  