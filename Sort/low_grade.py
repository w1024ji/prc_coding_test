n = int(input())
dict = {}

for i in range(n):
  name, grade = map(str, input().split())
  dict[name] = int(grade)

print(dict.items())

result = sorted(dict.items(), key=lambda x:x[1])
print(result)

for i in range(n):
  print(result[i][0], end=' ')