s = input()
first = int(s[0])
last = int(s[-1])
change=0
print("len: ", len(s)) # 7이라면
for i in range(len(s)-1): # 0~5
  print("i: ", i)
  if s[i] != s[i+1]:
    change+=1
  
print("change: ", change)

if first == last: # 만약 양끝이 같은 수라면
  print(change//2)
else: # 양 끝이 다르다면
  print(change-(change//2))