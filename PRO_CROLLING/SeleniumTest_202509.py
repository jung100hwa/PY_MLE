from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# 현재 크롬버전에 맞는 드라이버를 자동 설치. 존재하면 스킵
# 위치는 path에 잡혀 있고 lib아래 설치된다.
drive_path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

# 수집사이트 정의
driver.get("https://www.naver.com")

# 수집사이트 로딩 시간을 준다. 원래 이렇게 하면 안됨. 이건 네트워크를 고려하지 않은 단지 시간 정지
# time.sleep(3)

# 엘레멘터로 값불러오기
element_selector = "#shortcutArea > ul > li:nth-child(5) > a > span.service_name"
try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_selector)))
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, element_selector))
    # )
    element.click()
    print(element.text)
except TimeoutException:
    print("loading error")
except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다: {e}")

# value_group = driver.find_element(By.CSS_SELECTOR, element_selector)
# value_group.click() # 수집된 항목 선택

input()