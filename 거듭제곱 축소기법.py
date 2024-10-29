def slow_power(x, n) : 		# 반복으로 x**n을 구하는 함수 
    result = 1.0
    for i in range(n):			# 루브: n번 반복
        result = result * x
    return result

def power(x, n) :
    if n == 0 :						# 종료 조건
        return 1						# 모든 수의 0승은 1
    elif (n % 2) == 0 :				# n이 짝수 
        return power(x*x, n//2)			# 정수의 나눗셈
    else :							# n이 홀수 
        return x * power(x*x, (n-1)//2)	

a = int(input('x = '))
b = int(input('n = '))

x = a
n = b

import time		# time 모듈 포함
print("    억지기법(", x, '*', n, ')', power(x, n))
print("축소정복기법(", x, '*', n, ')', slow_power(x, n))

t1 = time.time()
for i in range(100000) : power(x, n)			# 축소정복 10만회 
t2 = time.time()
for i in range(100000) : slow_power(x, n)	# 억지기법 10만회
t3 = time.time()

print("    억지기법 시간... ", t3-t2)
print("축소정복기법 시간... ", t2-t1)
