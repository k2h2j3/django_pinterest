# django_pinterest

## 1. 목표와 기능

### 1.1 목표
Django를 사용하여 pinterest기능 구현

Vultr, docker, portainer를 사용하여 배포

<hr>

### 1.2 기능과 진행상황

1. 회원가입
2. 로그인, 로그아
3. 개인 페이지
4. 비밀번호 변경
5. 회원 탈퇴
6. 로그인 데코레이터
7. 프로필
8. Article(게시판)
9. 댓글
10. 프로젝트(카테고리)
11. 구독기능 <------------- 진행
12. 배포
    
<hr>

## 2. 개발환경 및 배포 URL

### 2.1 개발 환경
- Django
- Docker, Nginx
- html, css
- Bootstrap
- MagicGrid
- 그 외는 requirements.txt 참조

### 2.2 배포 URL

<hr>

## 3. 데이터베이스 ERD

<hr>

## 4. 프로젝트 구조

<hr>

## 5. UI

<hr>

## 6. 메인 기능

<hr>

## 7. 추가 기능

<hr>

## 8. 개발하며 배운 점

### 8.1 개발

<hr>

### 8.2 배포

배포 순서

cmd창에서 'ssh root@158.247.243.153(서버ip)' 입력 -> vultr홈페이지에서 나와있는 패스워드 입력 후 접속 
-> vultr에서 서버 구동 후 docker ps 커맨드명령어로 docker가 작동되는지 확인 -> 158.247.243.153:9000 로 portatiner접속(portainer는 gui로 컨테이너를 생성 및 연결할 수 있다)
-> admin 아이디 , 비밀번호 입력 후 접속(처음이면 생성) -> 


컨테이너간의 연결에서 시간이 매우 오래걸렸다.
처음에 연결했을 때, nginx.conf를 적용했는 데도 불구하고 css,media 적용이 되지 않았는데 볼륨(volume) 연결에서 헷갈린 부분이있었다.

![django_container_gunicorn볼륨(volume)](https://github.com/k2h2j3/django_pinterest/assets/74819625/4a83420d-f0a5-4b54-9fa1-3e791d7d90a1)

문제를 nginx 볼륨에서 해결하려고하였으나 여러 번 제대로 입력하고도 되지 않아 django_container_gunicorn 의 볼륨을 수정해보았더니 정상적으로 작동되었다.
문제가 생긴 이유는 위의 /home/디렉토리 이후에 내 레포지토리 디렉토리를 입력해야하는데 '/home/pragmatic/staticfiles/'로 입력한것이 착오였다.
위의 사진처럼 입력해주었더니 css도 잘 적용되고 이미지업로드도 잘 작동되었다.

![nginx볼륨(volume)](https://github.com/k2h2j3/django_pinterest/assets/74819625/22907c2e-5492-4414-abba-3c147cf099c7)

-> nginx의 볼륨(volume)

