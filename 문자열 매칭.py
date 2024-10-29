def string_m(T, P) :
    n = len(T)
    m = len(P)
    for i in range(n-m+1) :
        j = 0
        while j < m and P[j]==T[i+j] :
            j = j + 1
        if j == m :
            return i
    return -1

while True :
    x = int(input('입력 : 1 / 종료 : 2   - '))
    if x == 1 :
        mun = input('string1 : ')
        num = input('string2 : ')

        result = string_m(mun, num)
        print(num, 'in', mun, ' = ', result)
    elif x == 2 :
        print('end')
        break
