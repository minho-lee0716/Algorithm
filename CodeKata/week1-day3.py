'''
String 형인 string 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.
'''

import unittest

def get_len_of_str(string):

    tmp_list = []
    count = result = 0

    for j in string:

        if j not in tmp_list:
            tmp_list.append(j)
            count = len(tmp_list)

        else:
            result = max(result, count)
            tmp_list = []
            tmp_list.append(j)
            count = 1

    return max(result, count)

class CheckAlgorithm(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_len_of_str('abcabcabc'), 3)
    def test2(self):
        self.assertEqual(get_len_of_str('aaaaa'), 1)
    def test3(self):
        self.assertEqual(get_len_of_str('sttrg'), 3)

if __name__ == '__main__':
    unittest.main()
