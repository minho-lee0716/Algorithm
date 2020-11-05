'''
숫자인 num을 인자로 넘겨주면, 뒤집은 모양이 num과 똑같은지 여부를 반환해주세요.
'''

def same_reverse(num):
    a = str(num)
    b = a[::-1]
    return a == b
