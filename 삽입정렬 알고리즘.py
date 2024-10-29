def blabla(a, n):
    for i in range(1, n):
        j = i - 1
        while j >= 0 and a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]  # a[j]와 a[j+1]을 교환
            j -= 1


a = [4, 6, 8, 1, 3, 5]
print('a = ', a)
print()
n = len(a)
blabla(a, n)
print(a)
