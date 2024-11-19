NO_OF_CHARS = 128
def shift_table(pat): 
    m = len(pat)                	                # 패턴의 길이
    tbl = [m]*NO_OF_CHARS       	# 시프트 테이블

    for i in range(m-1):     		# 패턴의 모든 문자에 대해
        tbl[ord(pat[i])] = m-1-i	                # 그 알파벳이 패턴의 몇번째 문자인지

    return tbl


def search_horspool(T, P): 
    m = len(P)                      # 패턴의 길이
    n = len(T)                      # 텍스트(입력)의 길이
    t = shift_table(P)              # shift 테이블 생성
    i = m-1                         # 패턴의 우측끝 문자 위치
    while(i <= n-1):                # 가능한 모든 위치에 대해 
        k = 0                       # 매칭된 개수
        while k <= m-1 and P[m-1-k]==T[i-k]:    # 뒤에서 앞으로
            k += 1                  # 맞으면 계속 앞으로 진행
        if k == m :                 # 매칭성공: 매칭위치(왼쪽) 반환
            return i-m+1
        else :                      # 매칭실패
            i += t[ord(T[i])]       # T[i]의 테이블 참조 --> 건너뜀
    return -1                       # 매칭실패 –1 반환

while True :
    x = input('LIST : ')
    y = input('INPUT : ')
    print("패턴의 위치 :", search_horspool(x, y))
    print()
    break

