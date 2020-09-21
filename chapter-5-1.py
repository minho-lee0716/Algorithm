def solution(answers):

    # 각 수포자의 찍기 패턴입니다.
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    # 최종적으로 answers와 비교될 찍기 패턴 리스트입니다.
    pattern1 = []
    pattern2 = []
    pattern3 = []

    '''
    answers가 들어온 크기만큼 찍기 패턴을 늘려주는 반복문입니다.
    만약에 그냥 patternK += patternK를 하게 될 경우, 크기가 배로 늘어나기 때문에
    리스트가 쓸데없이 커져서 patternK와 pK를 분리한 것입니다.
    '''
    while len(pattern1) < len(answers):
        pattern1 += p1
    while len(pattern2) < len(answers):
        pattern2 += p2
    while len(pattern3) < len(answers):
        pattern3 += p3

    # 각 수포자가 찍어서 맞춘 정답의 개수를 알려주는 변수를 선언해줍니다.
    count1 = 0
    count2 = 0
    count3 = 0

    '''
    수포자가 찍어서 맞춘 정답의 개수를 세주는 반복문입니다.
    enumerate 함수를 이용해 찍기 패턴과 answers의 각 요소를 비교하여
    같으면 countK를 증가시켜줍니다.
    '''
    for index, element in enumerate(answers):
        if pattern1[index] is element:
            count1 += 1
        if pattern2[index] is element:
            count2 += 1
        if pattern3[index] is element:
            count3 += 1

    # countK 중에서 제일 큰 값을 max 내장 함수로 찾아줍니다.
    maxValue = max(count1, count2, count3)

    # 최종적으로 return해줄 리스트를 선언해줍니다.
    right_people = []

    '''
    제일 많이 맞춘 정답의 개수와 동일하게 맞춘 사람을 골라
    최종적으로 return할 리스트에 추가해 줍니다.

    이때 수포자 1, 2, 3 순서대로 리스트에 추가를 해주기 때문에
    오름차순으로 따로 정렬을 할 필요가 없습니다.
    '''
    if maxValue is count1:
        right_people.append(1)
    if maxValue is count2:
        right_people.append(2)
    if maxValue is count3:
        right_people.append(3)

    return right_people
