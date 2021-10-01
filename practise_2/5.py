a = int(input('Введите число\n'))
b = int(input('Введите число\n'))
c = int(input('Введите число\n'))
if a >= c <= b:
    print('Наименьшее число','',c)
elif c >= a <= b:
    print('Наименьшее число','',a)
else:
    print('Наименьшее число','',b)