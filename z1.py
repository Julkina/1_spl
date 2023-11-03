a = int(input('Введите целое число'))
n = str(a)
suma = 0
for i in n:
    if int(i) % 2 == 0:
        suma += int(i)

if suma == 0:
    print(0)
else:
    print('Сумма четных цифр числа', n, '=', suma)
