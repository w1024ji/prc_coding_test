# [문자열 압축] p.323
# 문자열 x 매개변수가 주어질 때, 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return하자

def solution(s): # 8
  answer = len(s)

  # 패턴길이의 범위는 1 ~ len(s)//2 이다
  for step in range(1, len(s) // 2 + 1):
    tmp = "" # 임시 문자열
    prev = s[0 : step]
    count = 1

    # step이 증가하면서 변하는 tmp
    for j in range(step, len(s), step):
      # 만약 이전 문자열과 동일하다면?
      if prev == s[j : j+step]:
        count += 1
      # 동일하지 않다면
      else:
        tmp += str(count) + prev if count >= 2 else prev
        prev = s[j : j+step] # 카운트 멈추고 새로운 패턴으로 인식. 다시 시작!
        count = 1

    # 남아 있는 문자열은 뒤에 추가
    tmp += str(count) + prev if count >= 2 else prev
    # 만들어진 것중에 가장 짧은 것이 정답
    answer = min(answer, len(tmp))

  return answer

