def b_search(a, key, low, high) :
    if (low <= high) :
        mid = (low + high)//2
        if key == a[mid] :
            return mid
        elif key < a[mid] :
            return b_search(a, key, low, mid-1)
        else :
            return b_search(a, key, mid+1, high)
    return -1

def bi_search(a, key, low, high) :
    while (low <= high) :
        mid = (low+high)//2
        if key == a[mid] :
            return mid
        elif key > a[mid] :
            low = mid + 1
        else :
            high = mid - 1
    return -1

a = [ 1, 3, 8, 13, 13, 16, 21, 26, 30, 33, 36, 39, 41, 44, 49 ]

print('입력 리스트 = ', a)
print()
print('탐색순환1 = ', b_search(a, 33, 0, len(a)-1))
print('반복탐색1 = ', bi_search(a, 33, 0, len(a)-1))
print('탐색순환2 = ', b_search(a, 32, 0, len(a)-1))
print('반복탐색2 = ', bi_search(a, 32, 0, len(a)-1))
