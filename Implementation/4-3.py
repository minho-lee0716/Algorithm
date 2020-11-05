'''
[입력 조건]
첫째 줄에 8 x 8 좌표 평면에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
입력 문자는 a1처럼 열과 행으로 이뤄진다.

[출력 조건]
첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.

[입력 예시]
a1

[출력 예시]
2
'''

def my_solution():
    current_location = input()

    x = current_location[0]
    y = int(current_location[1])

    row_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for index, element in enumerate(row_list):
        if x == element:
            x = int(index + 1)

    mx = [2, 2, -2, -2, -1, 1, -1, 1]
    my = [-1, 1, -1, 1, 2, 2, -2, -2]
    count = 0

    for i in range(8):
        rx = x + mx[i]
        ry = y + my[i]
        if rx < 1 or rx > 8 or ry < 1 or ry > 8:
            continue
        count += 1

    print(count)
    return 0

def sample_answer1():

    # 현재 나이트의 위치 입력받기
    input_data = input()
    row = int(input_data[1])
    column = int(ord(input_data[0])) - int(ord('a')) + 1

    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]
        # 해당 위치로 이동이 가능하다면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1

    print(result)
    return 0

my_solution()
#sample_answer1()
