strings = input() # 문자열 입력

sum=0
lst=[]

for string in strings:
  if string.isalpha():
    lst.append(string)
  elif string.isdigit():
    sum += int(string)

# lst를 알파벳 순으로 Sort
lst.sort()

if sum !=0: # 숫자가 있었다면
  lst.append(str(sum)) # 맨 뒤에 추가

print(''.join(lst))