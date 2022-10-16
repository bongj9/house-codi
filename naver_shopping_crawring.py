from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # 웹 브라우저를 시각적으로 띄우지 않는 headless chrome 옵션
    options.add_experimental_option('detach', True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 개발도구 로그 숨기기
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("start-maximized")  # 창 크기 최대로
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
    return driver


def shopping_category():
    driver = chrome_driver()
    keywords = ['샷시', '샤시', '창호']
    for keyword in keywords:
        url = f'https://search.shopping.naver.com/search/all?query={keyword}&frm=NVSHATC'
        driver.get(url)
        time.sleep(1.5)

        ul_tag = driver.find_element(By.CLASS_NAME, 'list_basis')
        lis = ul_tag.find_elements(By.CSS_SELECTOR, 'div > div > li')
        # print(f'상품수: {len(lis)}개')

        print(f'keyword: {keyword}')
        for li in lis:
            try:
                title = li.find_element(By.CLASS_NAME, 'basicList_title__3P9Q7').text.strip()
                if len(li.find_elements(By.CLASS_NAME, 'ad_ad_stk__12U34')):
                    title = '[AD] ' + title  # 광고노출상품
                print(title)

                category = ''
                category_div = li.find_element(By.CLASS_NAME, 'basicList_depth__2QIie').find_elements(By.TAG_NAME,
                                                                                                      'span')
                for categ in category_div:
                    # print(categ.text)
                    category += categ.text.strip() + '>'

                category = category[:-1]
                print(f'카테고리: {category}\n')
            except:
                continue

        print('=' * 50)

    driver.close()


shopping_category()