from itertools import count
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome(executable_path='C:\pyselenium\selenium\chromedriver.exe') # chromedriver 절대경로 설정
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl") # 구글 이미지 링크

elem = driver.find_element_by_name("q") # 검색창 선택
elem.send_keys("강동원") # 검색어 입력
elem.send_keys(Keys.RETURN) # 엔터

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") # 브라우저의 높이를 알 수 있는 자바스크립트 코드

while True: 
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 브라우저 끝까지 스크롤을 내리겠다.

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME) # 로딩 대기

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight") # 다시 브라우저의 높이를 구한다.
   
    if new_height == last_height:
        try:    
            driver.find_element_by_css_selector(".mye4qd").click()   # 검색 더보기
        except:
            break
    
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # 전체 사진을 뜻하는 코드
count = 1
for image in images:
    try:
        image.click() # 사진 클릭
        time.sleep(3) # 3초 대기
        imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") # 이미지 scr 불러오기
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") # 불러온 이미지 저장
        count = count + 1
    except:
        pass
driver.close()