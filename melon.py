# 멜론 사이트 접속하기
from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Chrome('C:\\Users\\Choi_AY\\Jupyter_ay\\chromedriver\\chromedriver.exe')
url='https://www.melon.com/chart/index.htm'
driver.get(url)

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
# song_data 곡, 가수명 저장
song_date=[]
rank=1

songs=soup.select('table>tbody>tr')
for song in songs:
    title=song.select('div.rank01>span>a')[0].text
    singer=song.select('div.rank02>a')[0].text
    song_date.append(['Melon',rank,title,singer])
    rank=rank+1

# song_data로 데이터프레임 만들기
import pandas as pd
columns=['서비스','순위','타이틀','가수']
pd_data=pd.DataFrame(song_date,columns=columns)
pd_data.head()

# 결과 엑셀로 저장
pd_data.to_excel('C:\\Users\\Choi_AY\\git-ay\\web_Crawling\\melon.xlsx',index=False)