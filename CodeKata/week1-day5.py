'''
strs은 단어가 담긴 배열입니다.
공통된 시작 단어(prefix)를 반환해주세요.
'''

import unittest

def get_prefix(string):

    # For empty 'string' Argument
    if len(string) == 0:
        return ''

    string = sorted(string)
    result = ''

    for i in string[0]:
        if string[-1].startswith(result+i):
            result += i
        else:
            break

    return result

class CheckAlgorithm(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_prefix(['aa', 'aa']), 'aa')
    def test2(self):
        self.assertEqual(get_prefix(['flower', 'fly', 'fairy']), 'f')
    def test3(self):
        self.assertEqual(get_prefix([]), '')

if __name__ == '__main__':
    unittest.main()
