# [Greedy] 곱하기 혹은 더하기

string = list(input())   # list()를 쓰면 각 char를 리스트의 요소로 만들어준다

s_int = [int(item) for item in string] # 숫자들을 계산하려면 모든 요소를 int로 바꿔줘야
s_int.sort()
print(s_int)

max_sum = 0

for s in s_int:
    if s != 0 and max_sum != 0:
        max_sum *= s
    elif s != 0 and max_sum == 0:
        max_sum = s
    else:
        continue

print(max_sum)





