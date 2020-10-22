'''
첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
(1 <= N, M <= 100)

둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다.
각 숫자는 1 이상 10,000 이하의 자연수이다.
'''

'''
# 나의 풀이
n, m = map(int, input().split())

smaller_in_rows = []

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    smaller_in_rows.append(data[0])

smaller_in_rows.sort()
print(smaller_in_rows[-1])
'''

# min() 함수를 이용하는 답안 예시
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
