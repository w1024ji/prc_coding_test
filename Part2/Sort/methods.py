# sorted()
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array) # array 자체는 유지됨
print("result: " , result)
print("array: ", array)

# 리스트 객체의 내장 함수 sort()
array2 = [5,4,7,2,4,3,9,8,1,9]

array2.sort() # array2 자체를 바꿔버린다.
print("array2: ", array2)

# key parameter 사용
array3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

# def setting(data):
#   return data[0]

result3 = sorted(array3, key=lambda data:data[1]) # key값은 정렬 기준이 된다. 여기선 숫자
print("result3: ", result3)