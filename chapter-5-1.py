def solution(answers):

    # People's patterns
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    # Increase by answers
    lena = len(answers)

    while len(pattern1) < lena:
        pattern1 += pattern1
    while len(pattern2) < lena:
        pattern2 += pattern2
    while len(pattern3) < lena:
        pattern3 += pattern3

    count1 = 0
    count2 = 0
    count3 = 0

    # Checking people's patterns and answers
    for index, element in enumerate(answers):
        if pattern1[index] is element:
            count1 += 1
        if pattern2[index] is element:
            count2 += 1
        if pattern3[index] is element:
            count3 += 1

    # Find maxValue among count1, count2 and count3
    maxValue = max(count1, count2, count3)
    right_people = []

    if maxValue is count1:
        right_people.append(1)
    if maxValue is count2:
        right_people.append(2)
    if maxValue is count3:
        right_people.append(3)

    return right_people

answers = [1,1,1,1,1,1,1,1,1,1,2,2]
solution(answers)
