def gcd(a, b) :
    print('gcd', (a, b))
    while b != 0 :
        r = a % b
        a = b
        b = r
        print('gcd', (a, b))
    return a

x = int(input('x : '))
y = int(input('y : '))
print(x, '과(와)', y, '의 최대 공약수 : ', gcd(x, y)) 
