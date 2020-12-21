# 람다식 lambda expression
# 장점 : 가독성, 메모리 절약, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

"""
lambda 파라미터 : 리턴
lambda 파라미터1,파라미터2...: 파라미터1 + 파라미터2 ...
"""

# 매개변수 두개를 받아 두수의 합을 리턴
# lambda 매개변수 : 표현식

def add(n,m):
    return n+m
print(add(2,3)) #5

print((lambda n,m:n+m)(2,3)) #5

# 람다를 변수에 할당하여 재사용
lambdaAdd = lambda n,m:n+m
print(lambdaAdd(2,3)) #5
print(lambdaAdd(4,5)) #9

# 람다식 안에서 조건
print((lambda n,m: n if n%2==0 else m)(1,3)) #3
print((lambda n,m: n if n%2==0 else m)(2,3)) #2

# map, filter, reduce
l = list(range(1,11))
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

m = list(map(lambda n:n*n, l))
print(m)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

f = list(filter(lambda n:n%2==0, l))
print(f)
# [2, 4, 6, 8, 10]

r = reduce(lambda n,m:n*m, l)
print(r)
# 3628800
