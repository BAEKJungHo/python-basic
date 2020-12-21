# packing & unpacking ex

"""
패킹은 인자로 받은 여러개의 값을 하나의 객체로 합쳐서 받을 수 있도록 한다.
1. tuple 형태 = 위치인자 패킹 * 한개를 매개변수 앞에 붙여서 사용한다.
2. dictionary 형태 = 위치인자 패킹 ** 두개를 매개변수 앞에 붙여서 사용한다.

언패킹은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어준다.
동일하게 위치인자를 unpacking 하는 경우는 * 를, 키워드인자를 unpacking하는 경우 ** 를 사용# 다.
"""

# 이런식으로 매개변수 앞에 * 하나를 붙이면 매개변수로 보낸 모든 객체들을 하나의 객체로 관리한다.
def func(*args):
    print(args)
    print(type(args))


# (1, 2, 3, 4, 5, 6, 'a', 'b')
# <class 'tuple'>
func(1, 2, 3, 4, 5, 6, 'a', 'b')


def kwpacking(**kwargs):
    print(kwargs)
    print(type(kwargs))

# {'a': 1, 'b': 2, 'c': 3}
# <class 'dict'>
kwpacking(a=1, b=2, c=3)

# unpacking

def sum(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
# sum(numbers) # error

# [1, 2, 3]을 인자로 보낼때, *을 붙이면 unpacking이 발생 한다.
print(sum(*numbers))

# unpacking 순서
"""
1. sum(*numbers)
2. sum(*[1, 2, 3])
3. sum(1, 2, 3)
"""

# 위치인자를 unpacking 할때는 위에 예에서는 list 타입이였지만, Container 객체라면 다 가능하다.
# set타입과 dict타입은 순서정보를 가지고 있지 않기 때문에 결과가 다를 수 있다.
sum(*'abc') # 'abc'
sum(*(4, 5, 6)) # 15
sum(*{'가', '나', '다'}) # '나다가'
sum(*{'치킨': 3, '피자': 12, '음료수': 10}) # '치킨피자음료수'

# 동일한 방식으로 키워드인자로 unpacking 할 수 있습니다. unpacking 하기 위해서는
# 인자가 key 와 인자로 구성되어 있는 mapping 타입, 즉 dict 가 필요하다.
def cal(first, op, second):
    if op == '+':
        return first + second
    if op == '/':
        return first / second
    if op == '-':
        return first - second
    if op == '*':
        return first * second

prob = {
  'first': 12,
  'second': 34,
  'op': '*'
}

cal(**prob) # 결과 : 408

# unpack 동작

"""
1. cal(**prob)
2. cal(prob = {
  'first': 12,
  'second': 34,
  'op': '*'
})
3. cal(first=12, second=34, op='*')
"""

# 만약 비어있는 인자를 unpacking를 하면 무시한다.
# 이러한 특성이 있기 때문에 함수의 packing과 unpacking을 이용하여,
# 다음과 같이 어떠한 함수에도 반응하는 함수를 작성할 수 있다.

# 함수와 함수에 인자들을 받아서 시작전 알림과 함께 함수를 실행시켜주는 함수
def start(func, *args, **kwargs):
    print("함수를 시작")
    return func(*args, **kwargs)

# 실행할 함수를 인자로 받고, 그 함수를 실행할 때 넣을 위치인자와 키워드인자를 넣는다.
start(print, '안녕하세요', '파이썬 꿀잼!', sep='~~ ')
