a = (1, -2, 3, 7, -9, 12, 13)
n = len(a)
#i = 0
q = 0
for i in range(0, n-1):
    if a[i] < 0:
        q = i
        break
a = list(a)
del a[q]
print(a)
