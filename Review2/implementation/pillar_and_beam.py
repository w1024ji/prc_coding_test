# [기둥과 보] [구현 p.331]

def solution(n, build_frames):
  answer = []
  for frame in build_frames: # frame의 개수는 최대 1000개
    x,y,stuff,operate = frame
    # 삭제하는 경우라면, 일단 먼저 삭제를 해본 후에 answer가 possible한지 아닌지 보고 만약 possible하지 않는다면
    # 삭제 취소 (즉, 다시 append()하기)
    if operate == 0: 
      answer.remove([x, y, stuff])
      if not possible(answer):
        answer.append([x, y, stuff])
    # 설치하는 경우도 마찬가지이다.
    if operate ==1:
      answer.append([x, y, stuff])
      if not possible(answer):
        answer.remove([x, y, stuff])
        
  # for문이 다 돌면 최종 결과를 반환
  return sorted(answer)

# 조건을 맞추는가?
def possible(answer):
  for x, y, stuff in answer:
    if stuff == 0: # 기둥을 설치하고 싶어
      # 1. 바닥에 있거나, 2. 보의 한쪽 끝에 있거나, 3. 다른 기둥 위에 있으면 ok
      if y==0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
        continue
      return False
    elif stuff == 1: # 보를 올리고 싶어
      # 1. 나한테 기둥이 연결되어 있거나, 2. 나랑 연결된 보가 기둥이랑 연결되어 있으면 ok
      if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1]) in answer:
        continue
      return False
      
  # for문을 다 돌았는데도 return False에 걸리지 않았다면 너는 True다!
  return True


# 예제 시험
build_frames = [ [0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1], [3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1] ]

print(solution(5, build_frames))
