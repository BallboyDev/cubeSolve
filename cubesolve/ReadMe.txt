"""===========================================
파일이름 : cubesolve
함수기능 : test폴더의 cubesolve 모듈, 클래스 설명 파일 참조
최초개발 : 2017. 8. 27
최종수정 : 2017. 11. 17
copyright ⓒ 2017 S.W.Yang All Rights Reserved
==========================================="""

설명
시작 파일 : main.py

main.py를 실행하면 Next command? 가 출력된다.
이곳에 큐브의 회전과 상태출력 해법 명령어를 입력한다.

1) 회전 명령어
- L, L', R, R', U, U'. D, D', F, F'. B, B'
- 회전 명령어는 공식 큐브 회전 기호를 따른다.

2) 상태 명령어
- print : 현재 큐브의 상태를 출력한다.
- init : 큐브를 완성된 상태로 초기화 한다.

3) 해법 명령어
- solve : 큐브를 자동으로 풀어 주는 명령어
-> solve를 입력시 큐브를 더 섞을수 있도록 회전 명령어를 더 입력할수 있다.