def sort_balls(arr):
    n = len(arr)
    count = 0  # 총 교환 횟수
    
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]: # 흰 구슬이 검은 구슬 뒤에 있을 경우 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1  # 교환 횟수 증가
    
    return arr, count

a = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]

sorted_balls, swaps = sort_balls(a)
print()
print('a = ', a)
print()
print(f"정렬 결과 : {sorted_balls}")
print(f"총 교환 횟수: {swaps}")
print()


"""
a = []

while True :
    x = int(input('구슬 입력 (흰색 - 1, 검은색 2)   / 정렬 시작은 3 / 종료는 4   :  '))
    if x in (1, 2) :
        a.append(x)
        print(a)
        print()
    elif x == 3 :
        sorted_balls, swaps = sort_balls(a)
        print()
        print('a = ', a)
        print()
        print(f"정렬 결과 : {sorted_balls}")
        print(f"총 교환 횟수: {swaps}")
        print()
    elif x == 4 :
        print('end')
        break
"""
