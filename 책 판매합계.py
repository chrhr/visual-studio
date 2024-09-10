books = []
total = 0

while True :
    menu = int(input('리스트 수정 - 1, 리스트 삭제 - 2, 리스트 확인 - 3, 합계와 평균 - 4, 종료 - 5  : '))
    print()

    if menu == 1 :
        a = int(input('books에 추가할 수량 : '))
        books.append(a)

    elif menu == 2 :
        b = int(input('books에서 삭제할 항목 : '))
        del books[b]

    elif menu == 3 :
        print(books)

    elif menu == 4 :
        for x in books :
            total += x
        print('판매수량 합계 : ', total)
        print('판매수량 평균 : ', total / len(books))

    elif menu == 5 :
        break
