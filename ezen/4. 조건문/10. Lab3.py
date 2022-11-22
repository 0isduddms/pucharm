# bmi = 체중 / (신장)^2

weigh = int(input("체중을 입력하세요 (kg) >>> "))
height = int(input("키를 입력하세요 (cm) >>> "))

bmi = weigh / ((height / 100) ** 2)
bmi = round(bmi, 2)


if bmi >= 30 :
    print('bmi 지수는 {}이며, 비만입니다.'.format(bmi))
elif (bmi >= 25) and (bmi <= 29) :
    print('bmi 지수는 {}이며, 과체중입니다.'.format(bmi))
elif (bmi >= 20) and (bmi <= 24):
    print('bmi 지수는 {}이며, 정상입니다.'.format(bmi))
else :
    print('bmi 지수는 {}이며, 저체중입니다.'.format(bmi))