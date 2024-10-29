def insertion_sort_recursive(A, n):
     if n <= 1:
        return

     insertion_sort_recursive(A, n - 1)
     key = A[n - 1]
     j = n - 2

     while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
        A[j + 1] = key
        printStep(A, n - 1)

def printStep(A, step):
    print(f"Step {step}: {A}")


A = [8, 7, 1, 9, 4, 2]
print('A = ', A)
print()
n = len(A)
insertion_sort_recursive(A, n)
print(A)
