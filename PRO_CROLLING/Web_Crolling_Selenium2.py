from selenium import webdriver

browser = webdriver.Chrome("chromedriver.exe")


url = 'https://www.naver.com'
browser.get(url)

browser.find_element(".link_service").click()

browser.quit()