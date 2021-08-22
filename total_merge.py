## 엑셀 파일 통합
import pandas as pd
excel_names=['C:\\Users\\Choi_AY\\Desktop\\multi_cp\\Project\\웹크롤링_miniProject\\miniProject_01\\study\\melon.xlsx',
            'C:\\Users\\Choi_AY\\Desktop\\multi_cp\\Project\\웹크롤링_miniProject\\miniProject_01\\study\\bugs.xlsx',
            'C:\\Users\\Choi_AY\\Desktop\\multi_cp\\Project\\웹크롤링_miniProject\\miniProject_01\\study\\genie.xlsx']

appended_data=pd.DataFrame()
for name in excel_names:
    pd_data=pd.read_excel(name)
    appended_data=appended_data.append(pd_data)

## 결과 확인
appended_data.info()

## 통합데이터 엑셀 저장
appended_data.to_excel('C:\\Users\\Choi_AY\\git-ay\\web_Crawling\\total_merge.xlsx',index=False)