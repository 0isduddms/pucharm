# 사용자로부터 입력을 받는 명령어 (input())
# x = input("입력하세요 : ")
#   1) 할당 연산자 (=) 오른쪽부터 실행
#   2) input() 함수 실행시, 입력을 기다림
#   3) 사용자가 데이터를 입력하고 엔터 입력
#   4) input 함수 자리에 데이터가 들어감

x = input("입력하세요 : ")
print(x)

y = int(input("숫자를 입력하세요 : "))
print(y)

# 자료형 확인하기 : type(x)
# str = 문자열

# 사용자로부터 두 개의 숫자를 입력받고, 더한 결과를 출력
x = input("첫번째 숫자를 입력하세요 : ")
y = input("두번째 숫자를 입력하세요 : ")

# print(type(x))
# print(type(y))

result = x + y
print(result)

#숫자형 변환 : int(데이터)

x = input("첫번째 숫자를 입력하세요 : ")
y = input("두번째 숫자를 입력하세요 : ")

result = int(x) + int(y)
print(result)


x = int(input("첫번째 숫자를 입력하세요 : "))
y = int(input("두번째 숫자를 입력하세요 : "))

result = x + y
print(result)