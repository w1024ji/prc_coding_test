# [문자열 재정렬] pg.322

n = input() # str형으로 받고

# n을 문자랑 숫자로 두동강 내고 
# 계산한 다음, 다시 합쳐야 하나?
alphas = ''
digits = 0

for i in range(len(n)):
  if n[i].isnumeric():
    digits += int(n[i])
  else:
    alphas += n[i]

# sorted()는 리스트를 반환한다. 
# ''.join()은 리스트의 요소를 '' (빈 문자열)로 연결해서 하나의 문자열로 만든다
print(''.join(sorted(alphas)) + str(digits))

