import math             # 루트 계산해야해서 불러와야함
def distance(p1, p2) :
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) # **은 제곱


def c_pair(p) :
    n = len(p)
    midist = float('inf')
    for i in range(n-1) :
        for j in range(i+1, n) :
            dist = distance(p[i], p[j])
            if dist < midist :
                midist = dist
    return midist

p = [(2,3), (12, 30), (40, 50), (12, 10), (3, 4) ]

print(p)
print()
print('최근접거리 : ', c_pair(p))
