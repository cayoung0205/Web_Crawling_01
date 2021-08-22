## 설계

### 목표

1. 멜론, 벅스, 지니 site: 서비스, 순위, 타이틀, 가수  **데이터 수집**
2. **데이터 처리 ( DF )** ------> pandas
3. **파일저장( __.xlsx ) ** -----> melon.xlsx, bugs.xlsx, genie.xlsx ----> .to_excel()
   - **Total.xlsx (melon.xlsx, bugs.xlsx, genie.xlsx)**



#### 필요한 과정

- 대상 site 분석
- 데이터 위치 파악(경로) ----> 개발자 도구 활용
- BeautifulSoup, Selenium, Chromedrive
- 전처리 (데이터 전처리, 날짜/시간 등 형식 처리, 수치 처리)
- 문자열 처리( \n 개행문자) -----> split, replace
- pandas.to_exel() -----> 파일 저장
- read_excel() -----> melon.xlsx, bugs.xlsx, genie.xlsx 불러오기
- .append() : Total.xlsx

