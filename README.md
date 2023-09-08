# django_pinterest

## 1. 목표와 기능

### 1.1 목표
Django를 사용하여 pinterest기능 구현

Vultr, docker, portainer를 사용하여 배포

<hr>

### 1.2 기능과 진행상황

1. 회원가입
2. 로그인, 로그아웃
3. 개인 페이지
4. 비밀번호 변경
5. 회원 탈퇴
6. 로그인 데코레이터
7. 프로필
8. Article(게시판)
9. 댓글
10. 프로젝트(카테고리)
11. 구독기능 
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

- http://158.247.243.153/ (현재 서버 닫혀있는 상태)

<hr>

## 3. 데이터베이스 ERD


![Django_pinterest](https://github.com/k2h2j3/django_pinterest/assets/74819625/c62fb4f0-11d8-4c57-b735-5c628426d61b)


<hr>

## 4. 프로젝트 구조

```bash
pragmatic
|
+---accountapp
|   +---migrations
|   |   \---__pycache__
|   +---templates
|   |   \---accountapp
|   \---__pycache__
+---articleapp
|   +---migrations
|   |   \---__pycache__
|   +---templates
|   |   \---articleapp
|   \---__pycache__
+---commentapp
|   +---migrations
|   |   \---__pycache__
|   +---templates
|   |   \---commentapp
|   \---__pycache__
+---media
|   +---article
|   +---profile
|   \---project
+---pragmatic
|   +---settings
|   |   \---__pycache__
|   \---__pycache__
+---profileapp
|   +---migrations
|   |   \---__pycache__
|   +---templates
|   |   \---profileapp
|   \---__pycache__
+---projectapp
|   +---migrations
|   |   \---__pycache__
|   +---templates
|   |   \---projectapp
|   \---__pycache__
+---static
|   \---js
+---subscribeapp
|   +---migrations
|   |   \---__pycache__
|   +---templates
|   |   \---subscribeapp
|   \---__pycache__
\---templates
    \---snippets
```

<hr>

## 5. UI

1. 회원가입

![스크린샷 2023-07-30 143845](https://github.com/k2h2j3/django_pinterest/assets/74819625/bcbf50d5-35c1-4855-980f-bf6a885ea9a0)

2. 메인화면

   ![스크린샷 2023-07-30 153352](https://github.com/k2h2j3/django_pinterest/assets/74819625/785a015a-b2fe-44dc-88c0-fb25608a6d21)

3. 프로젝트목록

   ![스크린샷 2023-07-30 153444](https://github.com/k2h2j3/django_pinterest/assets/74819625/5115d695-4de5-47d7-b94d-e552df218f0e)


4. 구독상태


![스크린샷 2023-07-30 153530](https://github.com/k2h2j3/django_pinterest/assets/74819625/b989fe9c-d1a1-42bc-b31d-27b44fa5f78d)






<hr>

## 6. 메인 기능

- 회원가입
- 로그인, 로그아웃
- 회원 탈퇴
- 프로필 CRUD
- 게시판 작성
- 게시글 CRUD
- 댓글 생성,삭제

<hr>

## 7. 추가 기능

- 구독 기능

<hr>

## 8. 개발하며 배운 점

### 8.1 개발

<hr>

### 8.2 배포

배포 순서

cmd창에서 'ssh root@158.247.243.153(서버ip)' 입력 -> vultr홈페이지에서 나와있는 패스워드 입력 후 접속 
-> vultr에서 서버 구동 후 docker ps 커맨드명령어로 docker가 작동되는지 확인 -> 158.247.243.153:9000 로 portatiner접속(portainer는 gui로 컨테이너를 생성 및 연결할 수 있다)
-> admin 아이디 , 비밀번호 입력 후 접속(처음이면 생성) -> 


#### 1) image 생성

   Dockerfile 작성 -> portainer에서 image 생성

   

#### 2) nginx 컨테이너와 django_container_gunicorn 컨테이너 연결


![1](https://github.com/k2h2j3/django_pinterest/assets/74819625/b2006d79-09b3-4161-a375-9a0442824734)


컨테이너간의 연결에서 시간이 매우 오래걸렸다.
처음에 연결했을 때, nginx.conf를 적용했는 데도 불구하고 css,media 적용이 되지 않았는데 볼륨(volume) 연결에서 헷갈린 부분이있었다.

![django_container_gunicorn볼륨(volume)](https://github.com/k2h2j3/django_pinterest/assets/74819625/4a83420d-f0a5-4b54-9fa1-3e791d7d90a1)

문제를 nginx 볼륨에서 해결하려고하였으나 여러 번 제대로 입력하고도 되지 않아 django_container_gunicorn 의 볼륨을 수정해보았더니 정상적으로 작동되었다.
문제가 생긴 이유는 위의 /home/디렉토리 이후에 내 레포지토리 디렉토리를 입력해야하는데 '/home/pragmatic/staticfiles/'로 입력한것이 착오였다.
위의 사진처럼 입력해주었더니 css도 잘 적용되고 이미지업로드도 잘 작동되었다.

![nginx볼륨(volume)](https://github.com/k2h2j3/django_pinterest/assets/74819625/22907c2e-5492-4414-abba-3c147cf099c7)

-> nginx의 볼륨(volume)

#### 3) django_container_gunicorn 컨테이너에서 DB를 외부 mariadb로 설정 후 연결


![2](https://github.com/k2h2j3/django_pinterest/assets/74819625/8085f3bb-108d-44fd-8c64-056ddb49dcb5)


DB를 외부로 돌리기 위해서는 settings.py의 기능을 local(개발환경)과 deploy(배포환경)을 나눠서 설정해주어야한다.

1.  pragmatic 디렉토리에서 settings 디렉토리를 만든 후(python package로 만들 것) local, deploy, base파일로 나눈다.

![settings](https://github.com/k2h2j3/django_pinterest/assets/74819625/4e347d12-b77b-4f7b-a775-cdc66dbbfbcb)

2. local환경과 deploy환경설정을 해준다. local환경은 settings.py의 기능을 그대로 사용해주면 된다.(pragmatic/settings/local.py 참조)
   deploy환경은 외부에서 사용할 DB를 넣어주고 DEBUG=False로 설정해준다(pragmatic/settings/deploy.py 참조)
   기존의 settings.py는 base.py로 rename 해준다.

3. settings라는 패키지를 추가했으므로 manage.py 변경

   
![managepy설정](https://github.com/k2h2j3/django_pinterest/assets/74819625/b3a28526-5235-413f-8ea1-ec7bcfdf28ef)


4. base.py의 BASE_DIR설정도 뒤에 .parent를 붙여준다


![BASEDIR](https://github.com/k2h2j3/django_pinterest/assets/74819625/07bff94b-6286-43a1-8298-64bf66a73e3e)


5. Dockerfile 수정 후 portainer에서 image를 새로 만든 후 그 image를 기반으로 새 django_container_gunicorn 컨테이너 생성


#### 4) 컨테이너->Service로 만들고 노드로 묶기

   서버를 돌리는 중에 django_container_gunicorn이 도중에 꺼지면 연동되어있는 다른 컨테이너또한 작동이 되지않아 서버가 다운될 것이다. 그러면 다시 컨테이너를 수동으로 켜주어야하는데 24시간내내 서버를 지킬수가 없기 때문에 자동적으로 서버를 구동시켜주는 시스템이 필요하다. 그것이 Service이다


   ![3](https://github.com/k2h2j3/django_pinterest/assets/74819625/b3654dd6-30af-4d26-8576-573cf3e0f793)


   1. cmd에서 root계정으로 가상서버에 접속한 후 'docker swarm init' 입력
  
![1](https://github.com/k2h2j3/django_pinterest/assets/74819625/834568d5-064f-4113-a013-a03b6e8bbcb4)

2. yml파일 작성, yml파일은 스택을 생성하기위해 필요한 파일로, 이 파일에는 그 동안 컨테이너들을 만드는데 입력한 volume,network,image등의 정보가 있다.


   ![2](https://github.com/k2h2j3/django_pinterest/assets/74819625/29966efc-5394-4f20-9530-3b834c20a402)


3. yml파일을 사용하여 스택 생성


![3](https://github.com/k2h2j3/django_pinterest/assets/74819625/e219d5f5-7df6-4758-bbc9-0835f4c875a7)


#### 5) docekr secret 설정


![4](https://github.com/k2h2j3/django_pinterest/assets/74819625/2407387f-2cca-4807-a2f6-76f01987eed5)

docker swarm으로 노드 1개를 만든 상태다. 여기서 DJANGO_SECRET_KEY처럼 외부에 공개하면 안되는 비밀정보들을 Docker에서 관리할 수 있는데 Docker secret 기능이다.


![5](https://github.com/k2h2j3/django_pinterest/assets/74819625/043fe1a7-519a-4cc3-a7b3-b3dfd16ed175)


1. secret에서 DJANGO_SECRET_KEY, MYSQL_ROOT_PASSWORD, MYSQL_PASSWORD 를 생성한다


![1](https://github.com/k2h2j3/django_pinterest/assets/74819625/b0f414b2-7001-4d55-aa39-0b7907f0d566)


2. yml 파일 수정(commit log 참조)


3. pragmatic/settings/delpoy.py 에서 코드 수정한다(read_secret 메서드생성 및 적용)


![2](https://github.com/k2h2j3/django_pinterest/assets/74819625/a0dc3218-76b2-4d80-8ba0-30ecba662e85)


![3](https://github.com/k2h2j3/django_pinterest/assets/74819625/e7f89199-47e8-41b5-b2fa-b975a07b18ed)


4. Dockerfile 수정(commit log 참조)


5. 수정된 Dockerfile을 바탕으로 새 image생성 후, 새 image, yml을 사용하여 새 stack 생성

   




   



