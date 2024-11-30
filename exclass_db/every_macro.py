from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def every_crawl():
    url = "https://everytime.kr/timetable"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    #시간표 추가 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#container > div > div.tablebody > table > tbody > tr > td:nth-child(3) > div.grids > div:nth-child(24)'))
    )
    element.click()

    #전공영역 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#subjects > div.filter > a:nth-child(3)'))
    )
    element.click()

    #전공 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#subjectCategoryFilter > div > ul > li:nth-child(1)'))
    )
    element.click()

    # 소프트웨어학과 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#subjectCategoryFilter > div > ul > ul.unfolded > li:nth-child(23)'))
    )
    element.click()


    # # 로그인 버튼 클릭
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, '#loginForm > fieldset > div.button > a.login'))
    # )
    # element.click()

    # soup = BeautifulSoup(driver.page_source, 'html.parser')

    # # 학번 추출
    # CrawlUserID = driver.execute_script('return document.querySelector("td.num").innerText')
    # print(CrawlUserID)

    # # 이름 추출
    # element = driver.find_element(By.CSS_SELECTOR, "#contents > div.dataArea > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    # CrawlUserName = element.text
    # print(CrawlUserName)

    # # 전공 추출
    # element = driver.find_element(By.CSS_SELECTOR, "#contents > div.dataArea > table > tbody > tr:nth-child(3) > td:nth-child(4)")
    # CrawlUserMajor = element.text
    # print(CrawlUserMajor)

    # 로그인 후 값 반환, 웹사이트 닫기
    time.sleep(2)  # 페이지 로드 대기
    driver.quit()

if __name__ == '__main__':
    every_crawl()