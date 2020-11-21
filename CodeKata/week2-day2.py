'''
숫자로 이루어진 배열인 nums를 인자로 전달합니다.

숫자중에서 과반수(majority, more than a half)가 넘은 숫자를 반환해주세요. 
'''

import unittest

def more_than_half(nums):
  for element in nums:
    if nums.count(element) > (len(nums) // 2):
      return element

class CheckAlgorithm(unittest.TestCase):

    def test1(self):
        self.assertEqual(more_than_half([1,2,3,3]), None)
    def test2(self):
        self.assertEqual(more_than_half([3,3,3,3,1,2,3,2,1,2,3]), 3)
    def test3(self):
        self.assertEqual(more_than_half([1,1,2,2,3,3,1,2,3,1,2,3,2]), None)

if __name__ == '__main__':
    unittest.main()

