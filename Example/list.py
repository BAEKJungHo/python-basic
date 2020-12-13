# 파이썬 리스트
# 자료구조에서 중요
# 파이썬 배열 제공X
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]

# 인덱싱 및 슬라이싱
print(a[:])
print(b[:])
b.append('1')
print(b[:])
print(c)
print(c[:])
print(f)
print(f[1])
print(e[2]) # ['Ace', 'Base', 'Captine']
print(e[2:]) # [['Ace', 'Base', 'Captine']]
print(e[2][:]) # ['Ace', 'Base', 'Captine']
print(e[2][-1]) # Captine
print(f[-1]) # 3.14159
print(d[2:100])

# 연산
print(c + d)
print(c * 3)

# 값 비교
print(c == c[:3] + c[3:])

# 같은 id 값
temp = c
print(c == temp)

# 리스트 수정, 삭제
print('>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print(c)

# 리스트 함수
print(c.pop(1))
c.append(1)
print(c)
print(c.pop(2))
print(c)
c.append(1)
c.sort()
print(c)
print(c.index(1))
print(c.index(80))
c.insert(2, 5)
print(c)
c.reverse();
print(c)
print(c.count(1))
ex = [8, 10]
c.extend(ex)
print(c)

# 삭제 remove, pop, del
# pop() 마지막 인덱스 부터 꺼낸다

# 반복문 활용
while c:
    l = c.pop()
    print(4 is l)
