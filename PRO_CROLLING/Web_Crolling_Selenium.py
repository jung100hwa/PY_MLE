from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import urllib.request

# 구글이미지를 다운로드
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(executable_path='chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

URL = "https://www.google.co.kr/imghp?hl=ko&ogbl"
driver.get(url=URL)

# 원하는 항목을 찾을 때가지 10초간 대기
xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
wait = WebDriverWait(driver, 10)
elem = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

elem.send_keys("tiger")
elem.send_keys(Keys.RETURN)


# 이미지 리스트를 가져오기 위한 것 어찌보면 디렉명이라고 해야 할까
# imageList = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# imageList = driver.find_elements_by_css_selector("T1diZc KWE8qe")
# imageList = driver.find_elements('//*[@id="yDmH0d"]/div[2]/c-wiz')
imageList = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")



# 구글이미지는 스크롤 끝까지 하고 더보기 버튼까지 해서 한화면에 모두 나타나게 하기 위한 것
SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            # driver.find_element_by_css_selector(".mye4qd").click()
            driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
        except:
            break
    last_height = new_height


# 모든 이미지를 저장한다.
count = 1
for image in imageList:
    try:
        image.click()
        time.sleep(3)
        
        # 클릭하면 하나의 창에 이미지 명만 달리하니까. xpath, full xpath는 동일하다.
        # imgurl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        imgurl = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        mem=urllib.request.urlopen(imgurl).read()
        savename = "imagedown\\" + str(count) + ".jpg"
        with open(savename, mode="wb") as f:
            f.write(mem)    
        count = count + 1
        break;
    except:
        pass
   
driver.close()