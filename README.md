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
