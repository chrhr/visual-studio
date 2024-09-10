A = { 1, 3, 5, 7 }
B = { 1, 2, 3, 5 }

a1 = A.union(B)  #합집합
a2 = A.intersection(B)  #교집합
a3 = A - B  #차집합

print(A, B, sep = '\n')
print()
print('합집합 : ', a1)
print('교집합 : ', a2)
print('차집합 : ', a3)
