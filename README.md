# 파이썬 기초

> 인프런. 김왼손의 왼손코딩(한입에 쏙 파이썬)

## 파이썬의 장점

- 다른 언어에 비해 쉽게 배울 수 있다.
- 참고할 자료가 많다.
- 빠르게 만들 수 있다.

## 파이썬으로 할 수 있는 것

- 구글의 핵심 3대 언어 중 하나
- 나사, 인스타그램등 많은 곳에서 사용 중
- 데이터 과학
- 인공지능
- 자동화 프로그램
- 게임(장고, 플라스크 사용해서)
- 웹 개발

## 파이썬 설치

> https://www.python.org/downloads/
>
> IDLE(대화형 셸) 로 기초 잡기에는 충분(검색 창 > IDLE 검색)

## Example

```py
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello world')
Hello world
>>> print("Hello world")
Hello world
>>> print(Hello world)
SyntaxError: invalid syntax
>>> print(1)
1
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print(1+2*3)
7
>>> print("a
      
SyntaxError: EOL while scanning string literal
>>> print("a" + 1)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("a" + 1)
TypeError: can only concatenate str (not "int") to str
>>> print("a"+"b")
ab
>>> 
```

- 자바 스크립트와 같이 `작은 따옴표나, 큰 따옴표`로 감싸면 문자열 취급을 한다.

## 제곱, 몫, 나머지

- 제곱(`**`), 몫(`//`), 나머지(`%`)

```py
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(5//2)
2
>>> print(5%2)
1
>>> print(5**2)
25
```

## 리스트

```py
>>> candies = ['딸기맛', '사과맛']
>>> print(candies)
['딸기맛', '사과맛']
>>> my_list = ['a', 'b', [1.0, 2.0, '3']]
>>> print(my_list)
['a', 'b', [1.0, 2.0, '3']]
>>> my_list.append(1)
>>> print(my_list)
['a', 'b', [1.0, 2.0, '3'], 1]
>>> my_list.remove(1)
>>> print(my_list)
['a', 'b', [1.0, 2.0, '3']]
>>> my_list.remove(asdf)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    my_list.remove(asdf)
NameError: name 'asdf' is not defined
>>> my_list.remove('a')
>>> print(my_list)
['b', [1.0, 2.0, '3']]
>>> my_list[1]
[1.0, 2.0, '3']
>>> del my_list[1]
>>> print(my_list)
['b']

>>> my_list[1:4]
['1', 'a', '2']
>>> my_list[1:10]
['1', 'a', '2']
>>> my_list[1:2]
```

- append() : 값 추가하기
- remove() : 값 제거하기
- `del 리스트[인덱스]`  : 값 제거하기
  - 리스트.remove(이름)
- `리스트[인덱스]` : 값 접근하기
- `리스트[인덱스시작 : 인덱스종료] : 시작 ~ 종료-1 까지의 값에 접근 
  - 인덱스 종료를 인덱스 길이보다 크게 줘도 에러 안남
- 리스트.sort() : 숫자별, 알파벳별 정렬을 수행해준다.
- 리스트.count(name) : name 에 해당하는 개수를 카운트한다.

## 반복문

```
for 변수 in 리스트:
  실행할 문장
```

```py
a = 10
for num in range(10):
        print(a + num)
        
for str in '무지개 색은 빨주노초파남보':
  print(str)  # 문자열이 한 글자 씩 줄바꿈 출력됨
```

## 순서열 만들기

- range(시작, 종료)
  - 자바처럼 시작 ~ 종료-1 까지 만큼 반복문을 실행한다.

```py
for x in range(2, 10):
    for y in range(1, 10):
        print(x, 'x', y, '=', x * y)
```
