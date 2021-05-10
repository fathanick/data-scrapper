#https://stackoverflow.com/questions/49907917/how-to-scrape-youtube-comments-using-beautifulsoup
import time
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
URLs = []

with Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    for u in URLs:
        driver.get(u)

        for item in range(10):
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(3)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
            with open('raw-data.csv','w') as f:
                
                f.write(comment.text)    

'''
with Chrome() as driver:
    wait = WebDriverWait(driver,10)
    driver.get("https://www.youtube.com/watch?v=2D9KToeLoCE")

    for item in range(3): #by increasing the highest range you can get more content
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(3)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        print(comment.text)