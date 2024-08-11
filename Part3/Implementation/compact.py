s= input() # 알파벳 소문자로만

# 단위를 기준으로 생각해봐야 하나?
# 문자열의 절반이 단위의 최대치.
'''
단위가 1인것부터 시작해서 증가(1/2까지)
각각 비교. 앞에꺼랑 뒤에꺼? 얼마나 반복되는지?
'''
def solution(s):
  answer = len(s)
  # 첫 번째 for문은 "단위"
  for step in range(1, len(s)//2 +1):
    compressed="" # 최종 문자열
    prev = s[0:step] # 주어진 단위로 끊은 덩어리
    count=1

    for j in range(step, len(s), step): # step만큼 증가해야 다음 덩어리에 접근 가능
      if prev == s[j:j+step]: # 같은 덩어리가 나왔다면 
        count+=1 
      else: # 다른 덩어리라면
        compressed += str(count) + prev if count >= 2 else prev
        prev = s[j:j+step] # prev의 위치를 그다음 덩어리로 대체
        count =1
        
    # 한 단위가 끝났으면 남아있는 문자열 정리. 그리고 길이 비교
    compressed += str(count) + prev if count>=2 else prev
    answer = min(answer, len(compressed))
      
  return answer


print(solution(s))