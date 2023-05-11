from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

# 드라이버 설정
driver = webdriver.Chrome()

# 사용할 웹페이지
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")

# 검색창 찾기
elem = driver.find_element(By.NAME, "q")

# 검색할 키워드 제공
elem.send_keys("chat gpt")

# 검색
elem.send_keys(Keys.RETURN)

# 이미지 로딩시간 부여
time.sleep(3)

# #스크롤 내리기
# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
    

#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
        

#         try:
#             driver.find_element(By.CSS_SELECTOR, ".r0zKGf").send_keys(Keys.ENTER)
#         except:
#             print("d1")
    
#         try:
#             driver.find_element(By.CSS_SELECTOR, ".mye4qd").send_keys(Keys.ENTER)
#         except:
#             print("d2")
        
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break

#     last_height = new_height

# 이미지 선택
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd") # 변경된 부분
count = 1

for image in images:
    try:
        print(count)
        image.click()
        time.sleep(3)
        # url 가져와서 변수에 담기
        imgUrl = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "test" + str(count) + ".jpg")
        count += 1
        if count > 10: # 이미지가 너무 많으면 멈추도록 설정
            break
    except:
        pass