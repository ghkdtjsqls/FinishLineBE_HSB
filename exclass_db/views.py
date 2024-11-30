from django.shortcuts import render
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re  # 정규 표현식 모듈 추가
from .models import MajorSubject

# Create your views here.
def every_crawl(request):
    url = "https://info.cku.ac.kr/haksa/undergraduate/subject_search_all.jsp"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    #학과 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table:nth-child(2) > tbody > tr > td:nth-child(2) > input[type=radio]'))
    )
    element.click()

    #소프트웨어 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table:nth-child(2) > tbody > tr > td:nth-child(2) > select > option:nth-child(42)'))
    )
    element.click()

    #검색 클릭
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > table:nth-child(2) > tbody > tr > td:nth-child(5) > img'))
    )
    element.click()

    html = driver.page_source  # 현재 페이지의 HTML 소스 가져오기
    soup = BeautifulSoup(html, 'html.parser')

    # table 내 모든 tr 태그에 대해 반복하면서 크롤링
    rows = soup.select("body > table:nth-child(5) > tbody > tr")  # 모든 tr 선택

    for row in rows:
        # 각 행에서 필요한 데이터 추출
        sub_area = row.select_one("td:nth-child(2)")  # 이수구분/전필
        sub_code = row.select_one("td:nth-child(3)")  # 과목코드
        sub_name = row.select_one("td:nth-child(4) > a:nth-child(1)")  # 과목명
        sub_credit = row.select_one("td:nth-child(5)")  # 학점

        # 데이터가 존재하는 경우만 출력
        if sub_area and sub_code and sub_name and sub_credit:
            sub_area = sub_area.text.strip()
            sub_code = sub_code.text.strip()
            sub_name = sub_name.text.strip()
            sub_credit = sub_credit.text.strip()

            # 정규 표현식을 사용해 학점에서 소수 부분만 추출
            match = re.search(r'[\d\.]+$', sub_credit)  # 소수점을 포함한 마지막 숫자 추출
            if match:
                credit = match.group(0)  # .5 출력

            # 크롤링한 데이터를 MySQL에 저장
            subject = MajorSubject(
                sub_area=sub_area,
                sub_code=sub_code,
                sub_name=sub_name,
                sub_credit=credit
            )
            subject.save()  # 데이터베이스에 저장

            print(f"저장된 과목: {sub_name} ({sub_code}) 학점: {credit}")

    # 로그인 후 값 반환, 웹사이트 닫기
    time.sleep(2)  
    driver.quit()

if __name__ == '__main__':
    every_crawl()