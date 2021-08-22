## import
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

## 지니사이트 접속
driver=webdriver.Chrome('C:\\Users\\Choi_AY\\Jupyter_ay\\chromedriver\\chromedriver.exe')
url='https://www.genie.co.kr/chart/top200'
driver.get(url)

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

## 반복문/ 곡, 가수명/ song_data 저장
song_data=[]
rank=1

songs=soup.select('tbody>tr')
for song in songs:
    title=song.select('a.title')[0].text.strip()
    singer=song.select('a.artist')[0].text
    song_data.append(['Genie',rank,title,singer])
    rank=rank+1
#### strip() 타이틀에 공백이 포함되어 있기때문에

## song_data 데이터 프레임
columns=['서비스','순위','타이틀','가수']
pd_data=pd.DataFrame(song_data,columns=columns)

pd_data.head()

## 엑셀 저장
pd_data.to_excel('C:\\Users\\Choi_AY\\git-ay\\web_Crawling\\genie.xlsx',index=False)