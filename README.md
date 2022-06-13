# Wantid Pre On Boarding 사전과제

- 아래 서비스 개요 및 요구사항을 만족하는 REST API 서버를 구현합니다.
- 사용가능 언어 와 프레임워크: **Python - Django, Flask** / **Javascript** - **Express**, **NestJS**


# 요구사항 분석

- 본 서비스는 기업의 채용을 위한 웹 서비스 입니다.
- 회사는 채용공고를 생성하고, 이에 사용자는 지원합니다.


## CRUD
- CRUD는 DJango Rest Framework의 내장라이브러리인 serializer를 사용하였고, mixin과 viewsets을 이용하여 시리얼라이저화한 데이터를 요구사항에 맞게 로직을 구현하였습니다.
- 내장 함수 get_queryset과 get_serializer 등 함수를 적극적으로 활용하여서 로직을 구현하였습니다.
- serializer는 읽기, 수정, 삭제 등등 같은 화면에서 처리가 가능한 메서드들만 묶어서 세분화 하였고, REST API를 개발 노력하였습니다.

### 1. 채용공고를 등록합니다.
<img width="1142" alt="image" src="https://user-images.githubusercontent.com/81574795/173415658-a6afcb3b-c514-4084-89eb-0cfba3f3c0cb.png">

- url -> "http://127.0.0.1:8000/api/post/"  <POST>

 ```
#input ex.

HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "company": 1,
    "position": "웹 백엔드 개발자",
    "compensation": 3000000,
    "skill": "JAVA",
    "content": "JAVA 개발자 모집"
}
```
회사 id, 채용포지션, 채용보상금, 사용기술, 채용내용 순서대로 CREATE 데이터 값을 입력해서 생성합니다.



### 2. 채용공고를 수정합니다.
<img width="1086" alt="image" src="https://user-images.githubusercontent.com/81574795/173416585-cce1da10-1f49-4146-a420-8cbb284980c0.png">

- url -> "http://127.0.0.1:8000/api/post/8/"  <PATCH>

 ```
#input ex.

HTTP 200 OK
Allow: GET, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "position": "웹 백엔드 개발자",
    "compensation": 3000000,
    "skill": "JAVA",
    "content": "JAVA 개발자 모집 --> 변경해보겠습니다~"
}
```
채용공고 상세화면에서 회사 id 이외의 채용포지션, 채용보상금, 사용기술, 채용내용을 수정할 수 있도록 구현하였습니다.


### 3. 채용공고를 삭제합니다.
<img width="1152" alt="image" src="https://user-images.githubusercontent.com/81574795/173416821-9d97c40d-cc6a-42db-9452-daa91787228c.png">

- url -> "http://127.0.0.1:8000/api/post/8/"  <DELETE>
  
 ```
#input ex.

HTTP 204 No Content
Allow: GET, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
```
채용공고 상세화면에서 DELETE 기능을 구현하였습니다.


### 4-1. 채용공고 목록을 가져옵니다.
<img width="1028" alt="image" src="https://user-images.githubusercontent.com/81574795/173417289-7f0a72b6-4188-4108-922b-0472fbeb7f6f.png">

- url -> "http://127.0.0.1:8000/api/post/"  <GET>

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 1500000,
        "skill": "Django",
        "created": "2022-06-10T00:45:32.484779+09:00"
    },
    {
        "id": 5,
        "company_name": "카카오",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 10000000,
        "skill": "Python",
        "created": "2022-06-10T01:44:15.507336+09:00"
    },
    {
        "id": 6,
        "company_name": "NCSOFT",
        "company_country": "한국",
        "company_region": "서울",
        "position": "유니티 개발자",
        "compensation": 2000000,
        "skill": "유니티",
        "created": "2022-06-10T16:15:26.570529+09:00"
    },
    {
        "id": 7,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "JAVA 백엔드 개발자",
        "compensation": 111111111,
        "skill": "Spring",
        "created": "2022-06-13T19:31:16.570814+09:00"
    }
]
```
채용공고 id, 회사이름, 회사거주나라, 회사거주지역, 채용포지션, 채용보상금, 사용기술, 채용공고 생성일자를 출력하였습니다. 


### 4-2. <선택사항 및 가산점요소> 채용공고 검색 기능 구현
<img width="1135" alt="image" src="https://user-images.githubusercontent.com/81574795/173418413-bd623012-5c5b-42ff-b362-8bb014d0c5ef.png">

- 검색기능은 내장라이브러리이면서 admin 검색기능과 유사한 Search Filter를 구현하였습니다.
  ```
    filter_backends = [SearchFilter]
    search_fields = ['position', 'company__company_name', 'skill']
  ```
- url -> "http://127.0.0.1:8000/api/post/?search=네이버"  <GET>

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 1500000,
        "skill": "Django",
        "created": "2022-06-10T00:45:32.484779+09:00"
    },
    {
        "id": 7,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "JAVA 백엔드 개발자",
        "compensation": 111111111,
        "skill": "Spring",
        "created": "2022-06-13T19:31:16.570814+09:00"
    }
]
```

- url -> "http://127.0.0.1:8000/api/post/?search=Django"  <GET>

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 1500000,
        "skill": "Django",
        "created": "2022-06-10T00:45:32.484779+09:00"
    },
    {
        "id": 5,
        "company_name": "카카오",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 10000000,
        "skill": "Python",
        "created": "2022-06-10T01:44:15.507336+09:00"
    }
]
```
검색기능에서는 회사이름, 채용포지션, 사용기술 세 가지의 검색이 가능하도록 구현하였습니다. 


### 5. 채용 상세 페이지를 가져옵니다.
<img width="1127" alt="image" src="https://user-images.githubusercontent.com/81574795/173418593-e24be8b8-0578-4a4e-8f7a-74477373c94c.png">

- url -> "http://127.0.0.1:8000/api/post/4/" <GET>

```
HTTP 200 OK
Allow: GET, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "result": {
        "id": 4,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 1500000,
        "skill": "Django",
        "content": "백엔드 주니어 개발자를 채용합니다. 자격요건은..",
        "created": "2022-06-10T00:45:32.484779+09:00",
        "supported_user": [
            1
        ]
    },
    "posts": [
        4,
        7
    ]
}
```
- <선택사항 및 가산점요소> 회사가 올린 다른 채용공고 : 상세 페이지에서 posts 데이터에세 채용공고 id를 리스트로 만들어서 출력하였습니다. 
```
"posts": [
        4,
        7
    ]
```
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 4,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "Django 백엔드 개발자",
        "compensation": 1500000,
        "skill": "Django",
        "created": "2022-06-10T00:45:32.484779+09:00"
    },
    {
        "id": 7,
        "company_name": "네이버",
        "company_country": "한국",
        "company_region": "서울",
        "position": "JAVA 백엔드 개발자",
        "compensation": 111111111,
        "skill": "Spring",
        "created": "2022-06-13T19:31:16.570814+09:00"
    }
]
```
같은 회사가 올린 채용공고 id가 4와 7을 생성하였을 때, posts 데이터에 4와 7이 리스트로 출력되게 하였습니다. 확인해보면 같은 회사인 네이버인 것을 확인할 수 있습니다.
  
  
### 6. <선택사항 및 가산점요소> 사용자는 채용공고에 지원합니다. 
<img width="1145" alt="image" src="https://user-images.githubusercontent.com/81574795/173420507-15d16252-982e-477c-976e-1dab26131927.png">
  
- 지원 기능은 원하는 방향대로 개발의 진행이 안되어서 출력된 데이터들이 이쁘고 프론트 입장에서 깨끗하게 사용할 수 있게끔 데이터를 출력하지 못한 점이 아쉬웠습니다.
  ```
          # 지원 하기
        # 지원 유저가 같은 공고에 지원하지 않았다면,
        if not Support.objects.filter(
            user_id=user,
            post=post
        ).exists():
            sup = Support.objects.create(
                user_id=user,
                post=post
            )
            sup.save()

            response = Response(status=status.HTTP_200_OK)
            serializer = SupportSerializer(sup, read_only=True)
            response.data = serializer.data
            print(response)
            return response
        # 지원 유저가 해당 공고에 이미 지원하였다면,
        else:
            return Response({'message': '이미 지원을 하였습니다.'})
  ```

- url -> "http://127.0.0.1:8000/api/post/6/support/"  <POST>
  
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "user": 1,
    "post": 6
}
```
POST 메서드로 지원을 하면 유저의 id와 지원한 채용공고 id가 출력되게 구현하였습니다.

```
HTTP 200 OK
Allow: GET, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "result": {
        "id": 6,
        "company_name": "NCSOFT",
        "company_country": "한국",
        "company_region": "서울",
        "position": "유니티 개발자",
        "compensation": 2000000,
        "skill": "유니티",
        "content": "C++ 사용경험이 많으신 분",
        "created": "2022-06-10T16:15:26.570529+09:00",
        "supported_user": [
            1
        ]
    },
    "posts": [
        6
    ]
}
```
결과 데이터를 보면 supported_user에 리스트 형식으로 지원한 유저의 id를 출력할 수 있게 구현하였습니다.
  
  
# 끝!
