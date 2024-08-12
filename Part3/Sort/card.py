# n개의 카드 묶음
n = int(input())
cards=[]
for i in range(n):
  cards.append(int(input()))

print('cards: ', cards)

totals=[]

check=[False]*n # False면 아직 안 한거

for i in range(n):
  cnt=0
  sums=[]
  for j in range(i+1, n):
    if check[i] == False and check[j] == False:
      sums.append(cards[i]+cards[j])
      check[i]=True
      check[j]=True
      cnt+=1
    elif check[i]==True and check[j]==False:
      sums.append(cards[j]+sums[cnt-1])
      cnt+=1
  print('sums: ', sums)
  totals.append(sum(sums))
  print('totals: ', totals)

print(min(totals))

  