# print Example
# Reference : https://www.python-course.eu/python3_formatted_output.php

# 기본출력
print('a')
print(123)
print(1+2)
print("abc" * 10)
print('''python start''') # result : python start
print("""python start""") # result : python start

print() # 개행

# separator option
print('P', 'Y', 'T', 'H', 'O', 'N') # result : P Y T H O N
print('P', 'Y', 'T', 'H', 'O', 'N', sep='') # result : PYTHON
print('P', 'Y', 'T', 'H', 'O', 'N', sep='-') # result : P-Y-T-H-O-N
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')


print()

# end option
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file option
import sys

print('Learn Python', file=sys.stdout) # Learn Python 이라는 문자열을 file = '파일명' 에 쓸거라는 의미

print()

# format option(d : int, s : string, f : float)
print('%s%s' % ('one', 'two'))
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print('%s %s %s' % ('A', 'B', 'C'))

# %s
print('%10s' % ('nice',))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice',))
print('{:10}'.format('nice'))

print('{:_<10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('pythonstudy',))
print('{:.5}'.format('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42,))
print('{:4d}'.format(42))

# %f
print('%f' % (3.141592653589793,))
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))
print('{:06.2f}'.format(3.141592653589793))
