'''
nums는 숫자로 이루어진 배열입니다.

가장 자주 등장한 숫자를 k 개수만큼 return해주세요.
'''

from collections import Counter

def top_k(nums, k):
  a = []
  b = Counter(nums).most_common()

  for i, element in enumerate(b):
    if i == k:
      break
    a.append(b[i][0])

  return a
