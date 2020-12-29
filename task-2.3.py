month = int(input('Введите номер месяца: '))

if month <= 0 or month >= 13:
    print('12 месяцев в году')
elif month >= 3 and month <= 5:
    print('Весна')
elif month >= 6 and month <= 8:
    print('Лето')
elif month >= 9 and month <= 11:
    print('Осень')
else:
    print('Зима')