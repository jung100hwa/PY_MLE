"""
1.한국생산기술연구원 알림마당 > 사업공고
2.한국생산기술연구원 알림마당 > 입찰공고

여기도 거의 업데이트가 안됨.
오늘 날짜로 3일전까지만 검색. 중복된 것은 삭제

# todo 이 파일은 운영서버 적용하기전에 터널링 작업을 위한 전단계이고 실제 운영서버는 3D_BusinessNotice_final_ad_real 대체됨
# todo 운영서버 적용전에 여기서 테스트를 한다음 3D_BusinessNotice_final_ad_real 이 파일에 적용하여 반영하면 됨
"""

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

# 터널링때문에 모든 결과를 여기에다 담는다.
G_Result_list = []
G_Okey_list = []

########################################################################################## 딕셔너리
DIC_INFO = {
    "201": "한국생산기술연구원-알림마당-사업공고",
    "202": "한국생산기술연구원-알림마당-입찰구매",
}

########################################################################################## 데이터베이스 변수설정

# 날짜 제한을 두자.
def date_collect(x):
    return (datetime.date.today() + datetime.timedelta(days=-x)).strftime("%Y%m%d")  # 사이트마다 타입이 달라서 숫자8개로 통일

dtday = datetime.date.today().strftime("%Y-%m-%d")
coll_day = list(map(date_collect, range(0, 4)))

column_list = ["OKEY", "ORIGIN", "LINK", "TITLE", "TAG", "CONF", "TDAY"]
conn = None

########################################################################################## 데이터베이스 연결
def maria_db_conn():
    global conn

    try:
        db_url = "mysql+pymysql://root:3dbankdb1218@175.126.176.174:3307/3dbank_v1" # 나중에 수정해야 함
        engine = create_engine(db_url)
        conn = engine.connect()
        print("DBConnection is success!!")

    except:
        print("DBConnection is not availableon this machine")
        exit()


########################################################################################## 마리아db로 인서트
def maria_db_insert():
    for ii, result_list in enumerate(G_Result_list):
        orign_key = G_Okey_list[ii]

        if len(result_list) > 0:
            df = pd.DataFrame(
                data=result_list,
                index=np.arange(1, len(result_list) + 1),
                columns=["OKEY", "ORIGIN", "LINK", "TITLE", "TAG", "CONF", "TDAY"],
            )

            # 빈값 삭제
            df["LINK"] = df["LINK"].replace("", np.nan)
            df["TITLE"] = df["TITLE"].replace("", np.nan)
            df.dropna(subset=["LINK", "TITLE"], how="any", inplace=True)

            # 중복값 삭제
            df.drop_duplicates(
                subset=["LINK"], keep="first", inplace=True, ignore_index=True
            )
            df.drop_duplicates(
                subset=["TITLE"], keep="first", inplace=True, ignore_index=True
            )


            # DB로 인서트
            try:
                query = f"select OKEY, ORIGIN, LINK, TITLE from tn_tdb_busicrawling where okey='{orign_key}'"
                result_df = pd.read_sql_query(query, conn)

                # 기존 db에 등록되어 있는 중복값 제거(todo 나중에 속도에 문제가 있으면 이 부분은 삭제하는게 좋을 듯)
                df = df.merge(result_df, how="outer", on=["TITLE"], indicator=True).loc[
                    lambda x: x["_merge"] == "left_only"
                ]

                # merge 이후에 필요한 컬럼만
                df = df.iloc[:, [0, 1, 2, 3, 4, 5, 6]]
                df.columns = column_list

                if len(df) > 0:
                    df.to_sql(
                        "tn_tdb_busicrawling", conn, if_exists="append", index=False
                    )  # db insert
                    conn.commit()
                    print(f"{len(df)} Insert success")
                else:
                    print(f"No recent data")
            except:
                print("Data insert error")
        else:
            print(f"No recent data")


##########################################################################################생산기술연구원 > 알림마당 > 사업공고
def crawling_201():
    driver = webdriver.Chrome()
    tap_num = 1
    result_list = []
    orign_key = "201"
    orign_text = "한국생산기술연구원-알림마당-사업공고"
    tag_text = "사업공고"
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    # 사업공고 첫페이지
    driver.get("https://www.kitech.re.kr/research/page1-1.php")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            # 3일이전데이터가 없으면 빠져 나오자
            if not forexit:
                break

            # 게시판 하단 페이징 첫번째 넘버
            tap_xpath_link = (
                f"/html/body/div/div/div/div[3]/div[2]/div[5]/div/a[{tap_num}]"
            )
            tap_drive = driver.find_element(By.XPATH, tap_xpath_link)

            if tap_drive:
                tap_drive.click()
                time.sleep(3)

                # 게시물 링크주소 갱신 숫자
                detail_num = 1

                for _ in range(0, 30):
                    try:
                        # 게시글 중 타이틀
                        detail_xpath_link = f"/html/body/div/div/div/div[3]/div[2]/table/tbody/tr[{detail_num}]/td[2]/div[1]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 게시글 중 등록일자
                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/div/div/div[3]/div[2]/table/tbody/tr[{detail_num}]/td[4]"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        
                        if reg_date:
                            reg_date = re.findall("[0-9]+", reg_date)
                            reg_date = "".join(reg_date)
                            reg_date = coll_day.count(reg_date) # 최근 3일치가 있으면..
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        if detail_data:
                            link_text = detail_data.get_attribute("href")

                            # 자바스크립트 처리.
                            # 원래는 javascript 단어가 포함되어 있으면. 검사를 해야 하는데 이미 사이트 분석결과 있으니
                            link_list = re.findall("[0-9]+", link_text)
                            if len(link_list) > 0:
                                link_list1 = link_list[0]
                                link_text = f"https://www.kitech.re.kr/research/page1-2.php?idx={link_list1}"
                                title_text = detail_data.text
                                result_list.append(
                                    [
                                        orign_key,
                                        orign_text,
                                        link_text,
                                        title_text,
                                        tag_text,
                                        conf_text,
                                        dtday,
                                    ]
                                )
                        else:
                            break  # 더이상 게시물이 없다고 가정. 하나의 페이징 넘버에 게시글이 없다고 판다

                        detail_num += 1
                    except:
                        break
            else:  # 더이상 페이징이 없다고 가정
                break

            tap_num += 1

        except:
            break
    driver.close()

    G_Result_list.append(result_list)
    G_Okey_list.append(orign_key)


##########################################################################################생산기술연구원 > 알림마당 > 입찰구매 > 입찰공고
def crawling_202():
    driver = webdriver.Chrome()
    tap_num = 1
    result_list = []
    orign_key = "202"
    orign_text = "한국생산기술연구원-알림마당-입찰구매"
    tag_text = "입찰구매"
    conf_text = "0"
    forexit = True

    print(f"{orign_text} ==============> 수집시작")

    driver.get("https://www.kitech.re.kr/bbs/page2-1.php")
    time.sleep(3)

    for _ in range(0, 2):
        try:
            tap_xpath_link = (
                f"/html/body/div/div/div/div[3]/div[2]/div[6]/div/a[{tap_num}]"
            )
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
                        detail_xpath_link = f"/html/body/div/div/div/div[3]/div[2]/table/tbody/tr[{detail_num}]/td[3]/div[1]/a"
                        detail_data = driver.find_element(By.XPATH, detail_xpath_link)

                        # 입찰공고만 불러오기. 완전 개떡같네
                        reg_gubu = f"/html/body/div/div/div/div[3]/div[2]/table/tbody/tr[{detail_num}]/td[2]/span"
                        reg_gubu = driver.find_element(By.XPATH, reg_gubu).text
                        if reg_gubu != "입찰공고":
                            continue

                        # 등록일자를 구해서 오늘(새벽)을 기준으로 이전 3일치만 구하자.
                        reg_date = f"/html/body/div/div/div/div[3]/div[2]/table/tbody/tr[{detail_num}]/td[5]"
                        reg_date = driver.find_element(By.XPATH, reg_date).text
                        if reg_date:
                            reg_date = re.findall("[0-9]+", reg_date)
                            reg_date = "".join(reg_date)
                            reg_date = coll_day.count(reg_date)
                        else:
                            reg_date = 0

                        if reg_date == 0:
                            forexit = False
                            break

                        # 입찰종료일을 구하기 위해
                        detail_xpath_link2 = f"/html/body/div/div/div/div[3]/div[2]/table/tbody/tr[{detail_num}]/td[4]"
                        detail_data2 = driver.find_element(By.XPATH, detail_xpath_link2)
                        bid_exitday = detail_data2.text
                        if len(bid_exitday) > 0:
                            bid_exitday = f"(~{bid_exitday})"

                        if detail_data:
                            link_text = detail_data.get_attribute("href")

                            # 자바스크립트 처리
                            link_list = re.findall("[0-9]+", link_text)
                            if len(link_list) > 0:
                                link_list1 = link_list[0]
                                link_text = f"https://www.kitech.re.kr/bbs/page2-2.php?idx={link_list1}"
                                title_text = detail_data.text + bid_exitday
                                result_list.append(
                                    [
                                        orign_key,
                                        orign_text,
                                        link_text,
                                        title_text,
                                        tag_text,
                                        conf_text,
                                        dtday,
                                    ]
                                )
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
    G_Result_list.append(result_list)
    G_Okey_list.append(orign_key)


def crawling_exe():
    print("=======================> collection start")

    G_Result_list = []
    G_Okey_list = []

    maria_db_conn()

    crawling_201()
    crawling_202()

    maria_db_insert()

    conn.close()

    print("=======================> collection end")


# schedule.every().day.at("01:30").do(crawling_exe) #매일 새벽 1시 30분에

if __name__ == "__main__":
    # while True:
    #     print("===============> Business Processing")
    #     schedule.run_pending()
    #     time.sleep(3)
    crawling_exe()
