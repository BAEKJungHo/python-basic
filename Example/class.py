# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재


# 예제 1
class Dog:
    species = 'maltiz'

    # __init__ 은 생성자라고 생각하면된다.
    def __init__(self, name, age): # self 는 자바의 this
        self.name = name
        self.age = age

print(Dog)
print(Dog.species)

dog1 = Dog("milk", 2)
dog2 = Dog("moca", 2)

print(dog1.age, dog2.name)
print(dog1 == dog2, id(dog1), id(dog2))

# 네임스페이스
print('dog1', dog1.__dict__)
print('dog2', dog2.__dict__)


# 예제2
# self의 이해
class SelfTest:
    def func1(): # self 가 붙지 않은 메서드는 클래스 메서드이기 때문에 "클래스명.메서드명" 으로 접근한다.
        print('Func1 called')
    def func2(self): # self 가 붙은 것은 인스턴스 메서드이기 때문에 "인스턴스변수명.메서드명" 으로 접근한다. or "클래스명.메서드명(인스턴스변)"
        print(id(self))
        print('Func2 called')

f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()
SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f)

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name): # __init__ 은 생성자라고 생각하면된다.
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self): # __del__ 메서드는 객체가 소멸할 때 자동으로 호출되는 함수이다.
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 0.0094
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)


# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))
