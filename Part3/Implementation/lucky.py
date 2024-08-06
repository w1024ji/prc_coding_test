n = input() # string 으로 먼저 받고 반으로 쪼갤까
half = len(n)//2 # 한 쪽의 길이가 얼마나 되는가? e.g) 3

# left랑 right를 구해서 if문으로 비교해볼까
left,right=0,0

for i in range(half): # 0 1 2
  left += int(n[i]) # 0 1 2 
  right += int(n[-1-i]) # 5 4 3

if left == right:
  print("LUCKY~")
else:
  print("READY")
  
