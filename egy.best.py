# -*- coding: utf-8 -*-
import ctypes  # An included library with Python install.
import os
import sys
import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

ctypes.windll.user32.MessageBoxW(0, "Copy Series Link And Click OK, Let Me Doing Boring Stuff For You!", "Made With <3 By NASR")
link = ''
while True:
    clip = pyperclip.paste()
    if "season" in clip:
        link = clip
        pyperclip.copy('') 
        break
    

name = link.split("season/")

name = name[1].replace("/","")
name = name.split("?")

path = os.path.join(sys._MEIPASS,"chromedriver.exe" )
opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(path,options=opt)


driver.get(link)
baseURL = link.split("/")[2]
baseURL = "https://"+baseURL
time.sleep(1)
episodeLinks = []
downloadLinks  = []

directLinks = []

shortLinks = driver.find_elements_by_css_selector('#mainLoad > div:nth-child(7) > div.movies_small a')

print(name)
for link in shortLinks:
    episodeLinks.append(link.get_attribute("href"))



for link in episodeLinks:
    driver.get(link)
    clickHereLinks = driver.find_element_by_css_selector("#watch_dl > table > tbody > tr:nth-child(1) > td.tar > a.nop.btn.g.dl._open_window").get_attribute("data-url")
    downloadLinks.append(clickHereLinks)
    


for goToVidStream in downloadLinks:
    callLink = baseURL+goToVidStream
    driver.get(callLink)
    while True:
        try:
            DownloadLink = driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").get_attribute("href")
            if DownloadLink == None:
                ClickOnAds= driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").click()
            else:
                directLinks.append(DownloadLink)
                break
        except:
            pass

with open(str(name)+'.txt', 'a') as f:
    for item in directLinks:
        f.write("%s\n" % item)  

ctypes.windll.user32.MessageBoxW(0, "Done, Check Text File Now", "Made With <3 By NASR")

driver.quit()
