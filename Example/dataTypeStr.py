# 파이썬 문자형

# 문자열 생성
str1 = "I am Python."
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(len(str1))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'

# 출력1
print(escape_str1)
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String : 있는 그대로 문자열을 표시할 수 있다. 즉, 이스케이프 문자 사용안하고 문자열을 출력할 수 있다.
raw_s1 = r'D:\Python\python3'
raw_s2 = r"\\x\y\z\q"


# Raw String 출력
print(raw_s1)
print(raw_s2)

# 멀티라인
multi_str1 = \
    """
    문자열
    멀티라인 입력
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"
str_o5 = "BAEK Jung Ho"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('y' in str_o1) # True
print('n' in str_o1) # True
print('P' not in str_o2) # True
print('A' in str_o5) # True

# 문자열 형 변환
print(str(66))  # type 확인
print(str(10.1))
print(str(True))
print(str(complex(12)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha 등)
print("Capitalize: ", str_o1.capitalize()) # capitalize 는 맨 앞글자를 대문자로 바꿔준다.
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"])) # I'm python !
print("replace1: ", str_o1.replace('thon', ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("split: ", str_o4.split(' '))  # Type 확인 : list // split:  ['Seoul', 'Deajeon', 'Busan', 'Jinju']
print(type( str_o4.split(' ')))
print("sorted: ", sorted(str_o1))  # reverse=True // sorted:  ['h', 'n', 'o', 'p', 't', 'y']

print("reversed1: ", reversed(str_o2)) # list 형 변환 // reversed1:  <reversed object at 0x000001E9D44F7E80>
print("reversed2: ", list(reversed(str_o2))) # reversed2:  ['e', 'l', 'p', 'p', 'A']

# 반복(시퀀스) 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인 # im_str 문자열에서 사용할 수 있는 모든 것들이 나온다.

# __iter__ : 반복할 수 있다.

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_sl = 'Nice Python'
str_l1 = [1,2,3]

# 슬라이싱 연습
print(str_sl[0:3])
print(str_l1[1:])
print(str_sl[5:])
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::-1]) # 오른쪽 처음부터 끝까지 가져오기 nohtyP eciN
print(str_sl[::2]) # 처음부터 끝까지 2칸 간격으로 가져오기 Nc yhn

# 아스키코드
a = 'z'

print(ord(a))
print(chr(122))
