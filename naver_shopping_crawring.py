from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')

#웹사이트 열기
browser.get('https://www.naver.com/')
browser.implicitly_wait(3)

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, "#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(5) > a").click()
browser.implicitly_wait(3)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR,'#__next > div > div.header_header__24NVj > div > div > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > fieldset > div._gnbSearch_inner_2Zksb > div > input')
search.click()

# 검색어 입력
search.send_keys('쇼파'); search.send_keys(Keys.ENTER)  # 쇼파를 검색하고 엔터까지

# 스크롤 전 높이
before_h = browser.execute_script('return window.scrollY')

# 무한 스크롤 하기 (맨 아래로 스크롤 내리기)
while True:
    browser.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.END)
    time.sleep(1)   # 스크롤 할 때 부하가 걸리지 않도록
    after_h = browser.execute_script('return window.scrollY')
    if after_h == before_h:
        break   # 더이상 스크롤이 안되면(변화가 없으면) break
    before_h = after_h
print('Scroll End'); print()

# 파일 생성
f = open('C:\Ghost\네이버쇼핑몰크롤링_ver1.csv', 'w', encoding='cp949', newline='')
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR,'.basicList_info_area__TWvzp')
print(items)

for item in items:
    name = item.find_element(By.CSS_SELECTOR,'.basicList_title__VfX3c').text
    price = item.find_element(By.CSS_SELECTOR,'.price_num__S2p_v').text
    link = item.find_element(By.CSS_SELECTOR,'.basicList_title__VfX3c > a').get_attribute('href')
    print(name, price, link)
    csvWriter.writerow([name, price, link])

#파일 닫기
f.close()