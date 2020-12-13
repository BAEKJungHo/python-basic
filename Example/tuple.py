# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

"""
tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다. (immutable)
list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없습니다.
REPL에서 확인해봅니다.

list와 마찬가지로 다양한 타입이 함께 포함될 수 있습니다.

ex) 중요한 데이터들이 한번 저장되서 값이 변경되면 안되는 경우 사용
"""

# 선언
a = ()
b = (1,)
c = (11, 12,13,1, 4)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

print(b)
print('e - ', e[-1][1]) # e -  Base
print('e - ', list(e[-1][1])) # e -  ['B', 'a', 's', 'e']

# 튜플 연산
print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'Test' + c[0] - ", 'Test' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))

# 팩킹 & 언팩킹(Packing, and Unpacking)
# 언팩킹 : 묶여있던 원소를 풀어서 각각 대입

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t

# 출력확인
print(x1)
print(x2)
print(x3)
print(x4)

# 언팩킹2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(x1)
print(x2)
print(x3)
print(x4)

# 팩킹 & 언팩킹
t2  =1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)
