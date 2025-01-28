# [Greedy] 숫자 카드 게임

# n행 m열
n, m = map(int, input().split())

cards = []
for i in range(n):
    cards.append(map(int, input().split()))
    
min_cards = []
for i in range(n):
    min_cards.append(min(cards[i]))

min_cards.sort() 

print(min_cards[-1]) 


