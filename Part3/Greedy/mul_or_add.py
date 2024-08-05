s = input()
array=[]
for i in s:
  array.append(int(i))

result=

while array:
  temp = array.pop()
  if temp == 0:
    continue
  elif temp == 1:
    result += temp
  else:
    result *= temp

print(result)