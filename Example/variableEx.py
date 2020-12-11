# 파이썬 변수 Example

# 기본선언
apple = "apple"
a = 700

print(a * 700)

# type 함수는 해당 변수의 자료형을 알려준다.
print(type(a)) # <class 'int'>

# 동시선언
x = y = z = 1000
print(x, y, z)

# 값의 재할당
var = 75
var = "Water"
print(var)
print(type(var))

# Object Reference
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300) # print(300) 이란 놈을 수행하깅 위해서 Object Reference 가 일어난다.

# ex2)
n = 123
print(n, type(n))

m = n
print(m)

# id(identity)확인 : 객체의 고유값 확인
m = 800
n  = 655
print(id(m))
print(id(n))
print(id(m) == id(n)) # false

# 같은 오브젝트 참조
# 4개의 변수를 선언했지만 사실상 내부적으로는 1개만 가지고 있는 셈이다. (아이디 값이 전부 동일)
# 똑같은 변수를 계속 복사해서 값을 남발할 필요는 없다고 생각(파이썬 - 인터프리터)
# 즉, 여러 변수명에 같은 값이 할당되어있을 때 결과적으로는 하나의 오브젝트만 생성된다.
m = 800
n  = 800
x = 800
y = 800
print(id(m))
print(id(n))
print(id(m) == id(n)) # true

# 다양한 변수 선언
# Camel Case :  numberOfCollegeGraduates # -> Method or Variable 선언 규칙(자바에서 많이 사용)
# Pascal Case :  NumberOfCollegeGraduates -> 언어 상관없이 Class 생성 시 사용하는 선언 방
# Snake Case :  number_of_college_graduates -> 파이썬에서 변수 선언시 많이 사용

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not
class	from	or
continue	global	pass
"""
