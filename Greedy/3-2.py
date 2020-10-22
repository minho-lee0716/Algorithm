'''
조건1. 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.

조건2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.

조건3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.
'''

# 나의 풀이
n, m, k = map(int, input().split()) # 첫째 줄에 n, m, k의 값을 받아와줍니다.
numbers = list(map(int, input().split())) # 둘쨰 줄에 n개 만큼의 자연수를 받아와줍니다.
numbers.sort() # 정렬을 시켜줍니다.

# 가장 큰 수와 그 다음 큰 수를 각각 top1, top2의 변수에 담아줍니다.
top1 = numbers[n-1]
top2 = numbers[n-2]

# 최종 합을 가질 변수를 0으로 초기화 시켜줍니다.
result = 0

# top1과 top2의 값이 같다면 최대 중복 가능 횟수인 k에 상관없이 m번 만큼 반복하여 합을 구해줍니다.
if top1 == top2:
    for _ in range(m):
        result += top1

# top1과 top2의 값이 다르다면, 가장 큰 수를 k번 만큼 반복하여 더해주고 top2를 더해줍니다.
else:
    i = 0
    for _ in range(m):
        if i == k:
            result += top2
            i = 0

        else:
            result += top1
            i += 1

print(result)

# 단순하게 푸는 답안 예시
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = numbers[n - 1] # 가장 큰 수
second = numbers[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result) # 최종 답안 출력

# 답안 예시
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = numbers[n - 1] # 가장 큰 수
second = numbers[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second

print(result) # 최종 답안 출력
