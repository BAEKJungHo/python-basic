# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
# 클래스, 함수, 변수 등을 한 파일에 모아둔다음 사용하고자 하는 곳에서 import math, import random 이런식으로
# import 한 다음 random.random() 이런식으로 사용할 수 있다.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y

def power(x, y):
    return x ** y


# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)

# __name__ 사용
# 외부에서 import 해서 사용하는경우에는 main 이 아니므로 해당 코드는 실행 안함
# 해당 모듈 파일 내에서는 실행 가능 함
# 실제로 모듈을 만들 때 main 키워드를 사용해서 테스트 코드를 작성함
# 모듈 파일 내에서 __name__ == "__main__" 은 해당 모듈에 대한 정보를 참고하거나 테스트 코드용으로 많이 사용한다.
if __name__ == "__main__":
    print('-' * 15)
    print('called! __main__')
    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(divide(10,2))
    print(power(5,3))
    print('-' * 15)
