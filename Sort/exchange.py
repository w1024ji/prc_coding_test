n, k = map(int, input().split())

arrayA = list(map(int, input().split())) # 1 2 5 4 3

arrayB = list(map(int, input().split())) # 5 5 6 6 5

arrayA.sort() # 1 2 3 4 5
arrayB.sort(reverse=True) # 5 5 5 6 6

print(arrayA)
print(arrayB)

for i in range(k):
  if arrayA[i] < arrayB[i]:
    arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
  else:
    break

print(sum(arrayA))
