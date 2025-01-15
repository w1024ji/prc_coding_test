# [Greedy] [큰 수의 법칙]

# n개의 수가 주어질 때 m번 더해서 최대의 수를 구하라 (단, 연속은 k번까지만 가능하다)
n, m, k = map(int, input().split())

# n개의 수를 받는다
lst = list(map(int, input().split()))

lst.sort(reverse=True)
print(lst)

first_big = lst[0]
second_big = lst[1]

result = 0
# result = [제일큰수 x k x (몫)] + [두번째로큰수 x (나머지)] 
result = first_big * k * (m//k) + second_big * (m%k)
print(result)

