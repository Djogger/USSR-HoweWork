import math

a = int(input('Введите значение a: ', ))
b = int(input('Введите значение b: ', ))
c = int(input('Введите значение c: ', ))

d = int(b**2 - 4*a*c)

if d > 0:
    x1 = (-1*b + math.sqrt(d))/(2*a)
    x2 = (-1*b - math.sqrt(d))/(2*a)
    print('Первый корень: ', x1, 'Второй корень: ', x2)

if d == 0:
    x1 = (-1*b)/(2*a)
    print('Корень: ', x1)

if d < 0:
    print('Корней не существует')
