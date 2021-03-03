# 크롤링 프로젝트
코로나 알림 서비스 제공

***
## 1. 개요
### 1-1 목적
- 국내 코로나 수도권, 전국 단위의 사회적거리두기 단계 설정과 확진자 현황 코로나 알림 서비스를 통해 확인
- 국내 코로나 감염증에 관련한 백신과 사회적거리두기, 재난지원금, 확진 이슈와 같은 키워드별 최신 뉴스 알림

### 1-2 수집 데이터
- 코로나바이러스감염증-19(COVID-19) http://ncov.mohw.go.kr/
  
- 네이버 통합 검색 뉴스 메뉴(기간 옵션 : 1일)
  - 키워드
  - 코로나 수도권 확진 : https://search.naver.com/search.naver?where=news&query=코로나%20수도권%20확진&pd=4
  - 코로나 국내 백신 : https://search.naver.com/search.naver?where=news&query=코로나%20국내%20백신&pd=4
  - 코로나 사회적거리두기 : https://search.naver.com/search.naver?where=news&query=코로나%20사회적거리두기&pd=4
  - 코로나 정부 재난지원금 : https://search.naver.com/search.naver?where=news&query=코로나%20정부%20재난지원금&pd=4 

### 1-3 팀원 / 역할
- [이지홍](https://github.com/***) 코로나 확진자 현황, 사회적거리두기 현황 데이터 수집
- [이경무](https://github.com/rudan916) 백신, 사회적거리두기, 재난지원금, 확진 이슈 키워드별 검색결과 데이터 수집

## 2. 내용
### 2-1. 크롤링 방법
- AWS서버를 이용한 확진 현황 사이트, 키워드별 검색결과 데이터 수집
- Scrapy 프레임 워크를 활용한 모듈작성

### 2-2. 데이터베이스 저장
- 작성한 모듈파일 저장
- mongodb 활용

### 2-3. 크롤링 스케쥴
- 
