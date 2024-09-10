def find_max(A) :
    max = A[0]
    for i in range(len(A)) :
        if A[i] > max :
            max = A[i]
        return max

array = [20, 50, 60, 39, 79, 58]

print(array)
print()
print('max : ', find_max(array))
