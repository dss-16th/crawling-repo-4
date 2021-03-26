# 코로나 알림 크롤링 프로젝트
<img width="702" alt="스크린샷 2021-03-26 오후 3 35 34" src="https://user-images.githubusercontent.com/78460413/112592362-318ccd00-8e49-11eb-919e-806c6c056aca.png">

***
## 1. INTRO
### 1-1 목적
- 크롤링한 코로나 정보를 기반으로 이용자들에게 문자 알림으로 해당 정보를 제공하는 크롤링 프로젝트 입니다.
- 매일 변동되는 코로나 상황을 매일 아침 카카오톡 메세지를 이용하여 전달하며, 코로나 기간 내 이동과 생활 전반에 도움이 될 서비스를 구축 및 관리 하는 것이 목표로 합니다.
- 본 프로젝트의 목적은 scrapy를 활용한 크롤링 방법을 익히고 수집 된 데이터베이스를 정제 및 관리하기 위함에 있습니다.

### 1-2 수집 데이터
- 코로나바이러스감염증-19(COVID-19) 
    - http://ncov.mohw.go.kr/
- 코로나19 예방 접종
    - https://ncv.kdca.go.kr/
  
- 네이버 통합 검색 뉴스 메뉴(기간 옵션 : 1일)
  - 키워드 별 크롤링 진행
      - 코로나 수도권 확진 : https://search.naver.com/search.naver?where=news&query=코로나%20수도권%20확진&pd=4
      - 코로나 국내 백신 : https://search.naver.com/search.naver?where=news&query=코로나%20국내%20백신&pd=4
      - 코로나 사회적거리두기 : https://search.naver.com/search.naver?where=news&query=코로나%20사회적거리두기&pd=4
      - 코로나 정부 재난지원금 : https://search.naver.com/search.naver?where=news&query=코로나%20정부%20재난지원금&pd=4 

### 1-3 팀원 / 역할
- [이지홍]
  - https://github.com/jihong7107
  -  코로나 확진자, 거리두기, 백신 현황 데이터 크롤링, mongodb 관리, 카카오 api를 통한 메세지 전송 기능 구현, 메세지 내 웹 서버 링크 연동, 리드미 작성 
- [이경무]
  - https://github.com/rudan916
  - 백신, 사회적거리두기, 재난지원금, 확진 이슈 키워드별 검색결과 데이터 크롤링, mongodb 관리, Flask를 통한 웹 서버 배포, DB와 웹 연동, 리드미 작성

## 2. PROCESS
 
<img width="1159" alt="스크린샷 2021-03-19 오후 2 24 37" src="https://user-images.githubusercontent.com/78460413/111735157-e447b300-88be-11eb-8e21-08fb17a9832c.png">

### 2-1. 크롤링
- AWS서버를 이용한 확진 현황 사이트, 키워드별 검색결과 데이터 수집
- Scrapy 프레임 워크를 활용한 모듈작성

### 2-2. 데이터베이스 저장
- 작성한 모듈파일 저장
- mongodb 활용

### 2-3 Kakaotalk API 

### 2-4 Flask


### 3. 진행 결과
<img width="1149" alt="스크린샷 2021-03-19 오후 2 18 53" src="https://user-images.githubusercontent.com/78460413/111734876-4e138d00-88be-11eb-8f07-ea5e457f4004.png">


### 3. 진행상황, 계획 및 현재 진행 중 이슈 
#### 3-1 진행상황
- 웹 데이터 수집 완료
- mongodb 데이터 적재 완료
- corntab 설정 확인

#### 3-2 계획
- 확진자 현황, 백신 접종 현황 카톡 발송
- 발송된 메시지 flask로 구축된 키워드별 최신 기사(링크) 웹 링크 첨부

#### 3-3 진행 중 이슈
- 카톡 링크 설정 이슈
- mongodb 데이터 리셋(파이프라인, flask) 


