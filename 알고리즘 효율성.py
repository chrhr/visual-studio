def binary_digits(n):
    count = 1
    while n > 1 :
        count = count + 1
        n = n // 2
    return count

def binary_digits(n) :
    if n <= 1 :
        return 1
    else :
        return 1 + binary_digits(n//2)
