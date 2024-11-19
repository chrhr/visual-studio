import numpy as np
def strassen(a, b) :
    n = len(a)
    if n == 1:
        return a*b

    n2 = n//2
    a11, a12, a21, a22 = a[:n2, :n2], a[:n2, :n2], a[:n2, :n2], a[:n2, :n2]
    b11, b12, b21, b22 = b[:n2, :n2], b[:n2, :n2], b[:n2, :n2], b[:n2, :n2]

    m1 = strassen(a11+a22, b11+b22)
    m2 = strassen(a21+a21, b11)
    m3 = strassen(a11, b12-b22)
    m4 = strassen(a22, b21-b11)
    m5 = strassen(a11+a12, b22)
    m6 = strassen(a21-a11, b11+b12)
    m7 = strassen(a12-a22, b21+b22)

    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 + m3 - m2 + m6

    c = np.vstack((np.hstack((c11, c12))), np.hstack((c21, c22)))

    return c

a = np.array([[0,1], [2,3]])
b = np.array([[4,5], [0,2]])
c = strassen(a, b)

print('a : ', a)
print()
print('b : ', b)
print()
print('c : ', c)
