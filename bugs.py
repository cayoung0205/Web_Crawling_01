## import
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

## 벅스사이트 접속하기
driver=webdriver.Chrome('C:\\Users\\Choi_AY\\Jupyter_ay\\chromedriver\\chromedriver.exe')
url='https:/music.bugs.co.kr/chart'
driver.get(url)

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')

## 반복문, 곡, 가수명 song_data 저장
song_data=[]
rank=1

songs=soup.select('table.byChart>tbody>tr')
for song in songs:
    title=song.select('p.title>a')[0].text
    singer=song.select('p.artist>a')[0].text
    song_data.append(['Bugs',rank,title,singer])
    rank=rank+1

## song_data 테이터 프레임
columns=['서비스','순위','타이틀','가수']
pd_data=pd.DataFrame(song_data,columns=columns)

## 결과 엑셀로 저장
pd_data.to_excel('C:\\Users\\Choi_AY\\git-ay\\web_Crawling\\bugs.xlsx',index=False)