'''
    턱걸이 평균 측정 프로그램
    턱걸이 횟수를 저장할 빈 리스트 생성
    일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장
    리스트에 저장된 데이터의 평균을 구해 출력

    1일차 턱걸이 횟수 >>>
    2일차 턱걸이 횟수 >>>
    3일차 턱걸이 횟수 >>>
    4일차 턱걸이 횟수 >>>
    5일차 턱걸이 횟수 >>>
    6일차 턱걸이 횟수 >>>
    7일차 턱걸이 횟수 >>>
'''

times = []
x = int(input("1일차 턱걸이 횟수 >>> "))
times.append(x)
x = int(input("2일차 턱걸이 횟수 >>> "))
times.append(x)
x = int(input("3일차 턱걸이 횟수 >>> "))
times.append(x)
x = int(input("4일차 턱걸이 횟수 >>> "))
times.append(x)
x = int(input("5일차 턱걸이 횟수 >>> "))
times.append(x)
x = int(input("6일차 턱걸이 횟수 >>> "))
times.append(x)
x = int(input("7일차 턱걸이 횟수 >>> "))
times.append(x)

sum = times[0] + times[1] + times[2] + times[3] + times[4] + times[5] + times[6]
print(sum)
avg = sum / 7

print("일주일간의 턱걸이 평균 횟수 :", avg)