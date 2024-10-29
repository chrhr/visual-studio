def nsort(a) :
    n = len(a)
    for i in range(n-1) :
        least =  i
        for j in range(i+1, n) :
            if a[j]<a[least] :
                least = j
        a[i], a[least] = a[least], a[i]
        print("step ", i+1, a)

data = []

while True :
    x = int(input('추가 : 1 / 삭제 : 2 / 재정렬 : 3 / 종료 : 4  - '))
    if x == 1 :
        y = int(input('append : '))
        data.append(y)
        print('data : ', data)
    elif x == 2 :
        z = int(input('remove : '))
        data.remove(z)
        print('data : ', data)
    elif x == 3 :
        print()
        print("original : ", data)
        print()
        nsort(data)
        print()
        print("selection : ", data)
        print()
    elif x == 4 :
        print('end')
        break
