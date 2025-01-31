# 카드 번호는 3, 4, 5, 6, 9로 시작
# 카드 번호에 "-"이 들어갈 수 있으며 "-"를 제외한 숫자의 개수는 16개이다
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램 만들기

# 입력 : 첫 번째 줄에 테스트 케이스 T, 각 테스트 케이스는 한개의 줄로 이루어지며, 각 줄에는 '자연수'와 '-'로 이루어진 길이가 1 이상인 문자열

# 출력 : 각 테스트 케이스마다, 주어진 카드 번호로 신용카드를 만들 수 있으면 1 없으면 0 출력

T = int(input())
s_list = ['3', '4', '5', '6', '9']

for t in range(T):
    C = input()

    if '-' in C:
        C = C.replace('-', '')

    if len(C) != 16:
        print(f'#{t+1} {0}')

    else:
        if C[0] in s_list:
            print(f'#{t+1} {1}')
            
        else:
            print(f'#{t+1} {0}')
