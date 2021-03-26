# 코로나 알림 크롤링 프로젝트
<img width="702" alt="스크린샷 2021-03-26 오후 3 35 34" src="https://user-images.githubusercontent.com/78460413/112592362-318ccd00-8e49-11eb-919e-806c6c056aca.png">

***
## 1. INTRO
### 1-1 목적
- 이용자들에게 문자 알림으로 코로나 관련 정보를 제공하는 크롤링 프로젝트 입니다.
- 본 프로젝트는 매일 변동되는 코로나 상황과 관련 키워드 기사 웹 페이지를 매일 아침 카카오톡 메세지를 이용하여 전송함을 목표로 합니다.
- 본 프로젝트의 목적은 scrapy를 활용한 크롤링 방법을 익히고 수집 된 데이터베이스를 MongoDB를 활용하여 정제 및 관리하기 위함에 있습니다.
- /Scrapy 프레임워크 활용한 크롤링 방법과 수집한 데이터를 데이터베이스(MongoDB)에 적재하고 카카오톡 메시지 발송과 웹 페이지 구성, 수집 데이터 출력의 활용 방법을 학습합니다.

### 1-2 수집 데이터
- 코로나바이러스감염증-19(COVID-19) 
    - http://ncov.mohw.go.kr/
- 코로나19 예방 접종
    - https://ncv.kdca.go.kr/
  
- 네이버 통합 검색 뉴스 메뉴(기간 옵션 : 1일)
  - 키워드 별 크롤링 진행
      - 코로나 수도권 확진 : https://search.naver.com/search.naver?where=news&query=코로나%20수도권%20확진&pd=4
      - 코로나 국내 백신(https://search.naver.com/search.naver?where=news&query=코로나%20국내%20백신&pd=4)
      - 코로나 사회적거리두기 : https://search.naver.com/search.naver?where=news&query=코로나%20사회적거리두기&pd=4
      - 코로나 정부 재난지원금 : https://search.naver.com/search.naver?where=news&query=코로나%20정부%20재난지원금&pd=4 

### 1-3 팀원 / 역할
- [이지홍](https://github.com/jihong7107)
  - 코로나 확진자, 거리두기, 백신 현황 데이터 크롤링, mongodb 관리, 카카오 api를 통한 메세지 전송 기능 구현, 메세지 내 웹 서버 링크 연동, 리드미 작성 
- [이경무](https://github.com/rudan916)
  - 백신, 사회적거리두기, 재난지원금, 확진 이슈 키워드별 검색결과 데이터 크롤링, mongodb 관리, Flask를 통한 웹 서버 배포, DB와 웹 연동, 리드미 작성

## 2. PROCESS
 
<img width="1159" alt="스크린샷 2021-03-19 오후 2 24 37" src="https://user-images.githubusercontent.com/78460413/111735157-e447b300-88be-11eb-8e21-08fb17a9832c.png">

### 2-1. 크롤링
- 아마존 AWS에서 제공하는 리눅스 서버 이용
- 코로나 바이러스감염증-19 사이트 : 전체 확진자 현황, 수도권과 비수도권 거리두기 현황 데이터 수집
- 코로나 19 예방접종 사이트 : 백신,거리두기, 확진, 재난지원금 총 4가지 키워드 검색결과 내 기사 데이터 수집
- /코로나 19 예방접종 사이트 : 수도권 코로나 백신 접종 현황 데이터 수집
- /네이버 뉴스 검색결과 : 백신,거리두기, 확진, 재난지원금 총 4가지 키워드 검색결과 내 기사 데이터 수집
- Scrapy 프레임 워크를 작성하여 크롤링 모듈 작성
- /Scrapy 프레임 워크 내 spider.py 작성으로 데이터 크롤링 모듈 작성

### 2-2. 데이터베이스 저장
- 작성한 모듈 파일 저장
- MongoDB와 Scrapy pipeline 연동을 위한 mongodb.py 작성
- Scrapy 프레임 워크 내 pipeline.py 를 활용하여 MongoDB 내 적재
- 하루에 한번 주기로 크론탭을 설정하여 정해진 시간에 업데이트 되어진 크롤링 된 데이터를 저장
- /하루 한번 주기로 작성된 Scrapy 프레임워크가 작동 되도록 리눅스 크론탭을 활용한 스케쥴링으로 데이터 저장

### 2-3 Kakao API 
- pipeline.py 내 Kakao API를 사용하기 위한 모듈 작성
    - selenium을 활용하여 oauth code를 발급받아 Aaccess token 발급
    - Kakao API 내 메세지 보내기 기능 사용
    - 크롤링 된 데이터 첨부 및 링크 연결
- Shell script 파일 생성

### 2-4 Flask
- Flask 모듈 작성
    - kword.py : 키워드별 웹페이지 경로 지정, MongoDB에 적재된 데이터를 추출
    - html.index(html, juquery 작성) : html 코드 작성으로 웹 페이지 형태 구성, jquery를 작성하여 버튼 클릭시 kword.py와 연동하여 데이터 출력




## 3. CONCLUSION

### 3-1 실행 결과
<img width="1149" alt="스크린샷 2021-03-19 오후 2 18 53" src="https://user-images.githubusercontent.com/78460413/111734876-4e138d00-88be-11eb-8f07-ea5e457f4004.png">

### 3-1 추후 진행 계획
- 코로나 기간 내 이동과 생활 전반에 도움이 될 서비스를 구축 및 관리 하는 것을 향후 목표로 삼고 있습니다.
- 현재의 서비스에서 내가 있는 위치에 확진자 동선 알림 내용을 추가하여 확장 하고자 합니다.


