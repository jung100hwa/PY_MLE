from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# 크롬버전에 맞는 드라이버 자동 설치
drive_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

search_word = "사과"
driver.get(f"https://shoppinghow.kakao.com/search/{search_word}")
target_tag = "a[data-tiara-layer='listing_product product']"

# time.sleep(3)
# data = driver.find_elements(By.CSS_SELECTOR, target_tag)
# if len(data) >= 0:
#     for detail in data:
#         link_text = detail.get_attribute('href')
#         title_text = detail.get_attribute('title')
#         print(link_text, title_text)

# 이렇게 할수도 있다.
try:
    wait = WebDriverWait(driver, 10)
    data = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, target_tag)))

    if len(data) > 0:
        for detail in data:
            link_text = detail.get_attribute('href')
            title_text = detail.get_attribute('title')
            print(link_text, title_text)
except TimeoutException:
    print("loading error")
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다: {e}")



