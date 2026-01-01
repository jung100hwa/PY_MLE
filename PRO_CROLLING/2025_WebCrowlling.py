from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pandas as pd
import numpy as np

# 크롬버전에 맞는 드라이버 자동 설치
drive_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

# 검색어. 페이지 번호 초기 설정
search_word = "사과"
page_num = 1


result_list =  []

# while True: # 실전에서는 while 문으로 하고
for _ in range(0,2):
    driver.get(f"https://www.korcham.net/nCham/Service/Economy/appl/KcciReportList.asp")
    time.sleep(2) # WebDriverWait 이용할 수도 있음

    # 찾고자 하는 속성이 포함된 엘리먼트를 찾고
    target_tag = "a[data-tiara-layer='listing_product product']"
    data = driver.find_elements(By.CSS_SELECTOR, target_tag)

    if len(data) > 0:
        for detail in data:
            link_text = detail.get_attribute('href')
            title_text = detail.get_attribute('title')
            result_list.append([link_text, title_text])
    else:
        break

    page_num += 1

# 데이터프레임으로 변경
if len(result_list) > 0:
    df = pd.DataFrame(data=result_list, index=np.arange(1,len(result_list)+1), columns=['Link', 'Title'])

    # 빈값 삭제
    df['Link'].replace('',np.nan,inplace=True)
    df['Title'].replace('',np.nan,inplace=True)
    df.dropna(subset=['Link', 'Title'], how='any', inplace=True)

    # 중복값 삭제
    df.drop_duplicates(subset=['Link'], keep='first', inplace=True, ignore_index=True)
    df.drop_duplicates(subset=['Title'], keep='first', inplace=True, ignore_index=True)

    # 엑셀로 내보내기
    excel_export = pd.ExcelWriter('CrowlingResult.xlsx')
    df.to_excel(excel_export)
    excel_export.close()

