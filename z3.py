n = int(input('Введите натуральное число '))
delitel = []
for i in range(1, n + 1):
    if n % i == 0:
        delitel.append(i)

max_delitel = max(delitel)
min_delitel = min(delitel)

print(delitel)
print(max_delitel)
print(min_delitel)
