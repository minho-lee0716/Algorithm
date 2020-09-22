def solution(n, lost, reserve):

    students = ['O' for element in range(n)]

    # 일단 전체 학생들 중에서 체육복을 도난당한 학생들을 구해줍니다.
    for element in lost:
        students[element-1] = 'X'

    # 도난당한 학생들 중 여분의 체육복이 있다면 자기껄로 입습니다. 그리고 reserve배열에서 그 학생들은 없애줍니다.
    for element in reserve:
        if students[element-1] == 'X':
            students[element-1] = 'O'
            reserve.remove(element)

    return students.count('O')
