# [구현] [외벽 점검] p.335
from itertools import permutations

# 입력 예시
n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

def solution(n, weak, dist):
  # 원 길이를 2배 늘려서 일자 형태로 만들자
  length = len(weak)
  for i in range(length):
    weak.append(weak[i] + n)
    
  answer = len(dist) + 1 # answer 초기화

  
  for start in range(length):                            # 시작점을 바꿔보자
    for friends in list(permutations(dist, len(dist))):  # 친구들의 경우의 수
      count =1                                           # 투입할 친구의 수
      position = weak[start] + friends[count -1]         # 어떤 친구가 도달할 수 있는 위치
      
      for index in range(start, start + length):  # 취약점을 찾아보자
        if position < weak[index]:                # 만약 기존 인원으로 부족하다면
          count += 1                              # 친구 더 투입~~!!
          if count > len(dist):                   # 만약 더 투입이 불가능하다면 break
            break
          position = weak[index] + friends[count -1] # 친구 투입~~! 가랏
          
      answer = min(answer, count) # 친구 수의 최솟값
  
  if answer > len(dist): # 만약 모두 투입해도 불가능하면 -1 리턴
    return -1
    
  return answer
  
print(solution(n, weak, dist))
