# [Greedy] 문자열 뒤집기

string = list(input())

result = 0
first = string[0]

# 1부터 n-1까지
for i in range(len(string)-1):
    if string[i] != string[i+1] and string[i] == first:
        result += 1
    
print(result)

