def ssearch(A, key) :
    for i in range(len(A)) :
        if A[i] == key :
            return i
    return -1

data = [ 2, 4, 7, 6, 1, 9, 5 ]

print(ssearch)
