### CLI

> command line interface



1. GUI는 CLI에 비해 사용하기 쉬우나, 단계가 많고 컴퓨터 성능을 더 소모함
2. 서버, 개발 시스템이 CLI를 지원함



### ./: 현재 작업 중인 폴더

### ../: 현재 작업 중인 폴더의 상위 폴더



touch = 파일 생성자

```bash 
$ touch 파일명.확장자
$ touch .hidden.md    # 숨김 파일 만들기
```



ls = 현재 위치의 파일 목록 확인

```bash
$ ls
$ ls -a    # 현재 디렉토리의 숨김파일과 현재, 상위 디렉토리도 확인가능
$ ls -l    # ll과 동일
$ ls -al   # ll -al과 동일
```



pwd = 현재 작업 위치 절대경로로 확인

```bash
$ pwd
```



cd = 작업 중인 현재 위치(디렉토리) 이동

```bash
$ cd ..                    # 상위 위치로 이동
$ cd 특정 폴더명/특정 폴더명   # 여러 폴더를 뛰어넘을 수도 있음
$ cd c:user:Desktop        # 등으로 절대 위치로 이동 가능
```
mkdir = 디렉토리(폴더) 생성자




rm = 파일, 디렉토리 삭제자

```bash
$ rm 파일명
$ rm -r 디렉토리
```
