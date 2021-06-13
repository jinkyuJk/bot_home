# 패키지 만들기 실습(package_test.py 파일 및 my_package 패키지 생성 후 실습)
# from 패키지 import 모듈 (ex. from my_package import sum)

from my_package import sum, sub
x = sum.sum_ab(1,2)
print(x)

y = sub.sub_ab(3,1)
print(y)
# from 패키지.모듈 import 함수, 클래스 (ex. from my_package.sum import sum_ab)

from my_package.sum import sum_ab,Calculator
from my_package.sub import sub_ab
x2 = sum_ab(5,6)
y2 = sub_ab(7,6)
print(f"x2:{x2},y2:{y2}")



c = Calculator(1,2)
print(f"c.sum():{c.sum()}")
# __name__ ? => 현재 모듈의 이름을 담고 있는 내장 변수

if __name__ == '__main__': #packgae지 관련 해당파일실행시만 main이고 package의 name은 각모듈의 이름이들어감
    x2 = sum_ab(5, 6)
    y2 = sub_ab(7, 6)
    print(f"x2:{x2},y2:{y2}")