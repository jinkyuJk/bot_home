print("\n*************************************ex1*************************************")
'''
    리스트(list)? : 값을 나열해서 저장하는 것
    원소 : 리스트에 저장 된 각각의 값들
    인덱스(index, 색인) : 위치 값
    여기서 주의할 점은 리스트의 인덱스는 항상 0부터 시작한다는 점입니다.
    즉, 리스트 a의 첫 번째 원소는 a[0]
   '''

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# alpha = "ABCDEFGH"  # 리스트가 아닌 string 도 동일하게 인덱싱 가능
num = 1
# alpha의 자료형은 list  ( * abcdefgh 인 경우 자료형은 str)
print("type(alpha): ", type(alpha))
# num 의 자료형은 int
print("type(num): ", type(num))

# a 리스트 전체 출력
print("alpha: ", alpha)

'''
 인덱싱 : 인덱싱이라는 것은 무엇인가를 '가리킨다'는 의미입니다.
            즉, 문자열이나 리스트, 튜플 등에 번호를 부여하여 특정 위치를 가리키는 것을 말합니다. ex) A[0], A[-1]
'''
# a의 0번째 인덱스의 요소(값)는 0
print("alpha[0]: ", alpha[0])

print("alpha[4]:", alpha[4])

# len은 a라는 리스트의 길이를 알려주는 내장 함수
print("len(alpha): ", len(alpha))

# a[-1] 처럼 인덱스가 -1인 경우는 리스트의 마지막 원소가 출력
print("alpha[-1]:", alpha[-1])

# a[-2] 처럼 인덱스가 -2인 경우는 리스트의 뒤에서 두번째 원소가 출력
print("alpha[-2]:", alpha[-2])

print("alpha[0]+alpha[1] =", alpha[0]+alpha[1])


'''
슬라이싱 : 문자열, 리스트, 튜플 등을 특정 인덱스 구간에 맞춰 잘라 내는 것 
'''

# 인덱스 0부터 인덱스 3까지의 원소 출력
print("alpha[0:4]: ", alpha[0:4])
# 첫 인덱스(0)와 끝 인덱스는 생략가능 위 출력결과와 동일
print("alpha[:4]: ", alpha[:4])

# 인덱스 4 부터 끝까지
print("alpha[4:]: ", alpha[4:])

# 인덱스 2 부터 인덱스 5 까지
print("alpha[2:6]: ", alpha[2:6])


print("\n*************************************ex2*************************************")
a = ["안녕", "하세요", "저는", "홍길동", "입니다"]
print("a: ", a)
print("type(a): ", type(a))
print("a[0]: ", a[0])
print("a[4]:", a[4])
print("len(a): ", len(a))
print("a[-1]:", a[-1])
print("a[0]+a[1] =", a[0]+a[1])
print("정렬: ", sorted(a))  # 오름차순 정렬



print("\n*************************************ex3*************************************")
# 리스트 vs 튜플 : 튜플은 리스트와 동일하지만, 수정이 불가
a = [1, 2, 3]
b = (1, 2, 3)
print(f"a[0] : {a[0]}, b[0] : {b[0]}")

# a[1] = 5 # 에러 나지 않음
# print(a)
#
# b[1] = 5 # 에러 발생
# print(b)

data_lows = ['20201123','20201124','20201125','20201126','20201127']
time_rows = ['0900','0930','1000','1030']
main_rows = []
for item in data_lows:
    for item2 in time_rows:
     main_rows.append(item+item2)
print(main_rows)
