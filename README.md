# 파이썬

## 좋은 프로그램이란 ? 

- 코드의 가독성
  - 애플리케이션은 만든다고 끝이 아니라 수정과 개선이 이루어지기 때문에 코드의 가독성이 중요하다.
  - 또한 자신이 짠 코드를 다른 사람이 볼 수 있기 때문이다.
  - 코드의 가독성이 나쁘면 수정하는 사람 입장에서 다시 개발하는게 편하겠다라고 판단해서 개발하게되면 시간과 비용이 들어간다.
- 코드의 길이
  - 코드의 가독성과 연관이 있다.
- 변수의 이름
- 중복코드 줄이기

## 파이썬의 장점

- 다른 언어에 비해 쉽게 배울 수 있다.
- 참고할 자료가 많다.
- 빠르게 만들 수 있다.
- 무료, 오픈소스의 강력함(자바보다 85% 정도 많다고 함)
- 빠른 개발 속도(생산성)
- 협업이 수월하다.

## 파이썬으로 할 수 있는 것

- 구글의 핵심 3대 언어 중 하나
- 나사, 인스타그램, 구글, 유튜브 등 많은 곳에서 사용 중
- 데이터분석(pandas), 머신러닝
- 인공지능
- IOT : 라즈베리파이
- 자동화 프로그램
- 게임(장고, 플라스크 사용해서)
- GUI 프로그래밍 : pyQT
- 웹 프로그래밍 : flask, django

## 파이썬 환경 설정

1. Mac OS 환경 파이썬 설치 참고

- https://dejavuqa.tistory.com/60
- https://blockdmask.tistory.com/341
- https://eunguru.tistory.com/28

2. Atom Editor & 파이썬 연동 참고

- https://ddolbah.tistory.com/5
- https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/desc/atom_macos.md

  (파이썬 선택 실행)
- https://stackoverflow.com/questions/35546627/how-to-configure-atom-to-run-python3-scripts

3. 터미널 등록

- https://stackoverflow.com/questions/22390709/how-to-open-atom-editor-from-command-line-in-os-x

4. 한글 깨짐

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

5. 콘솔 폰트 사이즈

.script-view .line {
	font-size: 16px;
}

## 아톰 설정

- File > Settings > Install
	- autocomplete-python 검색 후 Install
	- script 검색 후 Install
