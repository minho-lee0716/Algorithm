'''
[입력 조건]
첫째 출에 정수 N이 입력된다. (0 <= N <= 23)

[출력 조건]
00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력한다.

[입력 예시]
5

[출력 예시]
11475
'''

def my_solution():

    n = int(input())
    count = 0

    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k): # if '3' in str(i) or str(j) or str(k): 는 왜 안되는지 모르겠음.
                    count += 1

    print(count)

    return 0

def sample_answer1():
    # H를 입력받기
    h = int(input())

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    print(count)
    return 0

my_solution()
#sample_answer1()
