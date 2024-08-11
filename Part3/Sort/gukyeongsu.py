# n 학생 수
n = int(input())
students =[]
for i in range(n):
  students.append(list(map(str, input().split()))) # 문자열때문에 int 못해

# 삽입정렬 사용
for i in range(1, n):
  for j in range(i,0,-1):
    if students[j][1] > students[j-1][1]:
      students[j], students[j-1] = students[j-1], students[j]
    elif students[j][1] == students[j-1][1]:
      if students[j][2] < students[j-1][2]:
        students[j], students[j-1] = students[j-1], students[j]
      elif students[j][2] == students[j-1][2]:
        if students[j][3] > students[j-1][3]:
          students[j], students[j-1] = students[j-1], students[j]
        elif students[j][3] == students[j-1][3]:
          if (students[j][0]) < (students[j-1][0]):
            students[j], students[j-1] = students[j-1], students[j]
          else:
            break
        else:
          break
      else:
        break
    else:
      break


for stu in students:
  print(stu[0])

