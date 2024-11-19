# 피보나치 (순환) : O(2^n)
def fib(n) :
    if n == 0 :
        return 0		        # 정복: 0번째 달
    elif n == 1 :
         return 1		        # 정복: 1번째 달
    else : 
        return fib(n - 1) + fib(n - 2)      # 분할(순환호출), 병합(결과 더하기)


# 피보나치 (반복): O(n)
def fib_iter(n) :
	if (n < 2): return n
	last = 0
	current = 1
	for i in range(2, n+1) :
		tmp = current
		current += last
		last = tmp
	return current


print('Fibonacci순환(5) = ', fib(5))
print('Fibonacci반복(5) = ', fib_iter(5))
for i in range (1, 35) :
    print()
    print('fib순환(%d)='%i, fib(i))
    print('fib반복(%d)='%i, fib_iter(i))
