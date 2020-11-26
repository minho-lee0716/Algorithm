'''
인자인 height는 숫자로 이루어진 배열입니다.
그래프로 생각한다면 y축의 값이고, 높이 값을 갖고 있습니다.
아래의 그래프라면 height 배열은 [1, 8, 6, 2, 5, 4, 8, 3, 7] 입니다.
'''

def get_max_area(height):
    area = 0
    for i in range(0, len(height)-1):
        for j in range(i+1, len(height)):
            if height[i] == height[j]:
                if height[i] * (j - i) > area:
                    area = height[i] * (j - i)
                else:

            if min(height[i], height[j]) * (j - i) > area:
                area = min(height[i], height[j]) * (j - i)

    return area
