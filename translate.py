#encoding:utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://ai.youdao.com/streamingAudio.s')
browser.implicitly_wait(5)
time.sleep(5)

language = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div/img')
language.click()
browser.implicitly_wait(1)
start = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/button/span')
# while True:
#     start.click()
start.click()
time.sleep(1)
while True:
    if start.get_attribute('textContent') == '录 音':
        try:
            start.click()
            time.sleep(1)
        except:
            time.sleep(1)
    else:
        time.sleep(1)
