from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pandas as pd
import numpy as np
import re
import datetime
from sqlalchemy import create_engine
import schedule

# 크롬버전에 맞는 드라이버 자동 설치
drive_path = chromedriver_autoinstaller.install()


########################################################################################## 데이터베이스 변수설정
# 날짜 제한을 두자.
def date_collect(x):
    return (datetime.date.today() + datetime.timedelta(days=-x)).strftime('%Y%m%d')  # 사이트마다 타입이 달라서 숫자8개로 통일


dtday = datetime.date.today().strftime('%Y-%m-%d')
coll_day = list(map(date_collect, range(0, 4)))

column_list = ['OKEY', 'ORIGIN', 'LINK', 'TITLE', 'TAG', 'CONF', 'TDAY']
conn = None


########################################################################################## 데이터베이스 연결
def maria_db_conn():
    global conn

    try:
        db_url = "mysql+pymysql://root:3dbankdb1218@175.126.176.174:3307/3dbank_new"
        engine = create_engine(db_url)
        conn = engine.connect()
        print("DBConnection is success!!")

    except:
        print("DBConnection is not availableon this machine")
        exit()


########################################################################################## 마리아db로 인서트
def maria_db_insert(result_list, orign_key):
    if len(result_list) > 0:
        df = pd.DataFrame(data=result_list, index=np.arange(1, len(result_list) + 1),
                          columns=['OKEY', 'ORIGIN', 'LINK', 'TITLE', 'TAG', 'CONF', 'TDAY'])

        # 빈값 삭제
        df['LINK'] = df['LINK'].replace('', np.nan)
        df['TITLE'] = df['TITLE'].replace('', np.nan)
        df.dropna(subset=['LINK', 'TITLE'], how='any', inplace=True)

        # 중복값 삭제
        df.drop_duplicates(subset=['LINK'], keep='first', inplace=True, ignore_index=True)
        df.drop_duplicates(subset=['TITLE'], keep='first', inplace=True, ignore_index=True)

        # DB로 인서트
        try:
            query = f"select OKEY, ORIGIN, LINK, TITLE from tn_tdb_crawling where okey='{orign_key}'"
            result_df = pd.read_sql_query(query, conn)
            conn.commit()

            # 기존 db에 등록되어 있는 중복값 제거
            df = df.merge(result_df, how='outer', on=['TITLE'], indicator=True).loc[
                lambda x: x['_merge'] == 'left_only']

            # merge 이후에 필요한 컬럼만
            df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6]]
            df.columns = column_list

            if len(df) > 0:
                df.to_sql('tn_tdb_crawling', conn, if_exists='append', index=False)  # db insert
                conn.commit()
                print(f"{len(df)} Insert success")
            else:
                print(f"No recent data")

        except:
            print("DBConnection is not availableon this machine")


##########################################################################################코참넷 > 경제자료 > 보도자료
def crawling_101():
    driver = webdriver.Chrome()
    tap_num = 1
    result_list = []
    orign_key = '101'
    orign_text = "대한상공회의소-경제자료-보도자료"
    tag_text = '보도자료'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/Economy/appl/KcciReportList.asp")
    time.sleep(3)

    for _ in range(0, 2):

        try:
            tap_xpath_link = f"/html/body/div/section[1]/div[2]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        detail_xpath_link = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[3]/p"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')

                            # 자바스크립트 처리
                            link_list = re.findall('[0-9]+', link_text)
                            if len(link_list) == 2:
                                link_list1 = link_list[0]
                                link_list2 = link_list[1]
                                link_text = f"https://www.korcham.net/nCham/Service/Economy/appl/KcciReportDetail.asp?SEQ_NO_C010={link_list1}&CHAM_CD=B{link_list2}"
                                title_text = detail_data.text
                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])
                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break
    driver.close()
    maria_db_insert(result_list, orign_key)


# ##########################################################################################코참넷 > 경제자료 > 브리프 & 인포
def crawling_102():
    driver = webdriver.Chrome()
    tap_num = 1
    orign_key = '102'
    result_list = []
    orign_text = "대한상공회의소-경제자료-브리프 인포"
    tag_text = '인사이트'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/Economy/appl/NewsBriefList.asp")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div/section[1]/div[2]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        detail_xpath_link = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[3]/p"
                        reg_date = driver.find_element(By.XPATH, reg_date).text

                        if reg_date:
                            reg_date = re.sub('[.-/]', '', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')
                            link_text1 = link_text.find(",")
                            link_text2 = link_text.lower().rfind("pdf")
                            if link_text1 > 0 and link_text2 > 0:
                                link_text = link_text[int(link_text1) + 2:int(link_text2) + 3]
                                link_text = f"https://www.korcham.net/new_pdf/target/{link_text}"
                            else:
                                link_text = ""

                            title_text = detail_data.text
                            result_list.append(
                                [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])
                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


##########################################################################################코참넷 > 경제자료 > 온라인 세미나
def crawling_103():
    driver = webdriver.Chrome()
    tap_num = 1
    orign_key = '103'
    result_list = []
    orign_text = "대한상공회의소-경제자료-온라인 세미나"
    tag_text = '산업소식'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/Economy/appl/OnlineSeminarList.asp")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div/section[2]/div[2]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        # 첫번째 페이징과 나머지가 section 다르네.
                        if tap_num == 1:
                            caption_link = "/html/body/div/section[1]/figure/figcaption/a"
                            caption_data = driver.find_element(By.XPATH, caption_link)

                            # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                            reg_date = f"/html/body/div/section[1]/figure/figcaption/a/span[2]"
                            reg_date = driver.find_element(By.XPATH, reg_date).text

                            if reg_date:
                                reg_date = re.findall('[0-9]+', reg_date)
                                reg_date = ''.join(reg_date)
                                reg_date = coll_day.count(reg_date)
                            else:
                                reg_date = 0

                            if reg_date == 0:
                                forexit = False
                                break

                            if caption_data:
                                caption_text = caption_data.get_attribute('href')
                                caption_list = re.findall('[0-9]+', caption_text)
                                if len(caption_list) > 0:
                                    caption_text = caption_list[0]
                                    cappton_link_text = f"https://www.korcham.net/nCham/Service/Economy/appl/OnlineSeminarDetail.asp?pageno={tap_num}&ONSEMI_ID={caption_text}"
                                    caption_title_text = caption_data.text
                                    caption_title_index = caption_title_text.find("\n")
                                    if caption_title_index > 0:
                                        caption_title_text = caption_title_text[0:caption_title_index]
                                    result_list.append(
                                        [orign_key, orign_text, cappton_link_text, caption_title_text, tag_text,
                                         conf_text, dtday])

                            detail_xpath_link = f"/html/body/div/section[2]/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                            detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                            # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                            reg_date = f"/html/body/div/section[2]/div[1]/table/tbody/tr[{detail_num}]/td[3]/p"
                            reg_date = driver.find_element(By.XPATH, reg_date).text

                            if reg_date:
                                reg_date = re.findall('[0-9]+', reg_date)
                                reg_date = ''.join(reg_date)
                                reg_date = coll_day.count(reg_date)
                            else:
                                reg_date = 0

                            if reg_date == 0:
                                forexit = False
                                break

                        else:
                            detail_xpath_link = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                            detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                            # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                            reg_date = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[3]/p"
                            reg_date = driver.find_element(By.XPATH, reg_date).text

                            if reg_date:
                                reg_date = re.findall('[0-9]+', reg_date)
                                reg_date = ''.join(reg_date)
                                reg_date = coll_day.count(reg_date)
                            else:
                                reg_date = 0

                            if reg_date == 0:
                                forexit = False
                                break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')

                            # 자바스크립트 처리
                            link_list = re.findall('[0-9]+', link_text)
                            if len(link_list) > 0:
                                link_text = link_list[0]
                                link_text = f"https://www.korcham.net/nCham/Service/Economy/appl/OnlineSeminarDetail.asp?pageno={tap_num}&ONSEMI_ID={link_text}"
                                title_text = detail_data.text
                                title_index = title_text.find("\n")
                                if title_index > 0:
                                    title_text = title_text[0:title_index]
                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])
                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


# ##########################################################################################코참넷 > 경제자료 > 경제컬럼
def crawling_104():
    driver = webdriver.Chrome()
    tap_num = 1
    result_list = []
    orign_key = '104'
    orign_text = "대한상공회의소-경제자료-경제컬럼"
    tag_text = '인사이트'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/Economy/appl/EconColumnList.asp")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div/section[1]/div[2]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        detail_xpath_link = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[3]"
                        reg_date = driver.find_element(By.XPATH, reg_date).text

                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')

                            # 자바스크립트 처리
                            link_list = re.findall('[0-9]+', link_text)
                            if len(link_list) > 0:
                                link_list1 = link_list[0]
                                link_text = f"https://www.korcham.net/nCham/Service/Economy/appl/EconColumnDetail.asp?pageno={tap_num}&nKey={link_list1}"
                                title_text = detail_data.text
                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])
                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


# ##########################################################################################코참넷 > 산업소식 > 경제정책정보
def crawling_105():
    driver = webdriver.Chrome()
    tap_num = 1
    orign_key = '105'
    result_list = []
    orign_text = "대한상공회의소-산업소식-경제정책정보"
    tag_text = '정책정보'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/EconBrief/appl/EconInfoList.asp")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div/section[1]/form/div[2]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        detail_xpath_link = f"/html/body/div/section[1]/form/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/section[1]/form/div[1]/table/tbody/tr[{detail_num}]/td[4]/p"
                        reg_date = driver.find_element(By.XPATH, reg_date).text

                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')

                            # 자바스크립트 처리
                            link_list = re.findall('[0-9]+', link_text)
                            if len(link_list) > 0:
                                link_list1 = link_list[0]
                                link_text = f"https://www.korcham.net/nCham/Service/EconBrief/appl/EconInfoDetail.asp?nPageNo={tap_num}&SEQNO={link_list1}"
                                title_text = detail_data.text
                                title_index = title_text.find("\n")
                                if title_index > 0:
                                    title_text = title_text[0:title_index]

                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])
                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


##########################################################################################코참넷 > 산업소식 > 유관기관소식
def crawling_106():
    driver = webdriver.Chrome()
    tap_num = 1
    orign_key = '106'
    result_list = []
    orign_text = "대한상공회의소-산업소식-유관기관소식"
    tag_text = '산업소식'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/EconBrief/appl/ExternalList.asp")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div/section[1]/div[2]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        detail_xpath_link = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[2]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/section[1]/div[1]/table/tbody/tr[{detail_num}]/td[4]/p"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')

                            # 자바스크립트 처리
                            link_list = re.findall('[0-9]+', link_text)
                            if len(link_list) > 0:
                                link_list1 = link_list[0]
                                link_text = f"https://www.korcham.net/nCham/Service/EconBrief/appl/ExternalDetail.asp?SEQ_NO={link_list1}"
                                title_text = detail_data.text

                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])

                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


def crawling_107():
    # 여기는 신기하게도 업데이트가 정말 빠르네. 그리고 여기만 탭3번까지 돌자. 특이하네.
    driver = webdriver.Chrome()
    tap_num = 1
    orign_key = '107'
    result_list = []
    orign_text = "대한상공회의소-산업소식-기업뉴스"
    tag_text = '산업소식'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.korcham.net/nCham/Service/EconBrief/appl/ComNewsList.asp")
    time.sleep(3)

    # 여기만 업데이트가 빨라 3번 돈다.
    for _ in range(0, 3):
        try:
            tap_xpath_link = f"/html/body/div/section[2]/div[3]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        detail_xpath_link = f"/html/body/div/section[2]/div[2]/table/tbody/tr[{detail_num}]/td[2]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/section[2]/div[2]/table/tbody/tr[{detail_num}]/td[3]/p"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute('href')

                            # 자바스크립트 처리
                            link_list = re.findall('[0-9]+', link_text)
                            if len(link_list) > 0:
                                link_list1 = link_list[0]

                                # 이사이트는 특이하게 3일치만 보여주나 보네
                                tod1 = datetime.date.today().strftime('%Y%m%d')
                                tod2 = (datetime.date.today() + datetime.timedelta(days=-3)).strftime('%Y%m%d')

                                link_text = f"https://www.korcham.net/nCham/Service/EconBrief/appl/ComNewsDetail.asp?pageno=1&STRYNO={link_list1}&GUBUN=N&daybt=OldNow&m_OldDate={tod2}&m_NowDate={tod1}"
                                title_text = detail_data.text

                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])

                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


##########################################################################################한국경제인협회 > 뉴스자료 > 보도자료 및 발표문
def crawling_201():
    driver = webdriver.Chrome()
    tap_num = 3  # 페이징이 특유하게 3번부터 시작하네
    orign_key = '201'
    result_list = []
    orign_text = "한국경제인협회-뉴스자료-보도자료 및 발표문"
    tag_text = '보도자료'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.fki.or.kr/kor/news/statement.do")
    time.sleep(2)

    # while True: # 실전에서는 while 문으로 하고
    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div[4]/div[2]/div[2]/div/div[1]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        # 찾고자 하는 속성이 포함된 엘리먼트를 찾고
                        detail_xpath_link = f"/html/body/div[4]/div[2]/div[2]/div/ul/li[{detail_num}]/div/div/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div[4]/div[2]/div[2]/div/ul/li[{detail_num}]/div/div/p[1]"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:

                            link_text = detail_data.get_attribute('onclick')
                            if link_text:
                                # 자바스크립트 처리
                                link_list = re.findall('[0-9]+', link_text)[0]
                                link_text = f"https://www.fki.or.kr/kor/news/statement_detail.do?bbs_id={link_list}&category=ST&pageIndex={tap_num - 2}&searchCnd=&searchWrd="

                                title_text = detail_data.text
                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])

                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 값이 없을 때
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


##########################################################################################한국경제인협회 > 이슈 앤 포커스 > FKI 인사이트
def crawling_202():
    driver = webdriver.Chrome()
    tap_num = 3  # 페이징이 특유하게 3번부터 시작하네
    orign_key = '202'
    result_list = []
    orign_text = "한국경제인협회-이슈앤포커스-FKI인사이트"
    tag_text = '인사이트'
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.fki.or.kr/kor/publication/globalInsight.do")
    time.sleep(2)

    # while True: # 실전에서는 while 문으로 하고
    for _ in range(0, 2):
        try:
            tap_xpath_link = f"/html/body/div[3]/div[2]/div[2]/div/div[1]/ul/li[{tap_num}]/a"
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        # 찾고자 하는 속성이 포함된 엘리먼트를 찾고
                        detail_xpath_link = f"/html/body/div[3]/div[2]/div[2]/div/ul/li[{detail_num}]"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div[3]/div[2]/div[2]/div/ul/li[{detail_num}]/div[2]/p[2]"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        if reg_date:
                            reg_date = re.findall('[0-9]+', reg_date)
                            reg_date = ''.join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:

                            link_text = detail_data.get_attribute('onclick')
                            if link_text:
                                # 자바스크립트 처리
                                link_list = re.findall('[0-9]+', link_text)[0]
                                link_text = f"https://www.fki.or.kr/kor/publication/globalInsight_detail.do?bbs_id={link_list}&category=GI&pageIndex={tap_num}"

                                title_text = detail_data.text
                                title_index = title_text.find("\n")
                                if title_index > 0:
                                    title_text = title_text[0:title_index]
                                result_list.append(
                                    [orign_key, orign_text, link_text, title_text, tag_text, conf_text, dtday])

                        else:
                            break  # 더이상 게시물이 없다고 가정
                        detail_num += 1
                    except:
                        break
            else:  # 더이상 값이 없을 때
                break
            tap_num += 1
        except:
            break

    driver.close()
    maria_db_insert(result_list, orign_key)


# schedule.every().monday.at("00:10").do(dirsearch) #월요일 00:10분에 실행
# schedule.every().day.at("10:30").do(dirsearch) #매일 10시30분에
# schedule.every().day.at("10:30").do(dirsearch) #매일 10시30분에
# schedule.every(10).seconds.do(dirsearch,strOrg, strExt) # 10초에 한번씩
# schedule.every(10).minutes.do(dirsearch) # 10분에 한번씩

def crawling_exe():
    print("=======================> collection start")
    maria_db_conn()
    crawling_101()
    crawling_102()
    crawling_103()
    crawling_104()
    crawling_105()
    crawling_106()
    crawling_107()
    crawling_201()
    crawling_202()
    conn.close()
    print("=======================> collection end")


schedule.every().day.at("01:30").do(crawling_exe) #매일 새벽 1시 30분에
# schedule.every(10).seconds.do(crawling_exe)  # 10초에 한번씩

if __name__ == "__main__":
    while True:
        print("===============> WebCrawling Processing")
        schedule.run_pending()
        time.sleep(3)
    # crawling_exe()