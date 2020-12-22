# 모듈 사용 실습

import sys
import time
import module

# module 은 sys 의 path 로 나오는 경로를 토대로 파이썬 엔진이 모듈을 검색한다.
print(sys.path)
print(module.multiply(10, 20))

# 모듈 경로 삽입
# 검증된 모듈이지 않는이상 이런식으로 사용하는건 비추
sys.path.append('C:/math')
