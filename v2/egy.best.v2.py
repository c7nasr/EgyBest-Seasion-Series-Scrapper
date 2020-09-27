# -*- coding: utf-8 -*-
import ctypes  # An included library with Python install.
import os
import sys
import time
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = input("Season: ")
quality = input("Quality (1 = 1080,2 = 720, 3 = 480, 4 = 360): ")
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')

seasons_links = []
episodes_links = []
download_links = []
name = link.split("season/")
name = name[1].replace("/", "")
name = name.split("?")
c = []
seasons = soup.find_all(href=re.compile("/season/"), class_="movie")
for link in set(seasons):
    seasons_links.append(link['href'])

page = requests.get(seasons_links[0])
soup = BeautifulSoup(page.content, 'html.parser')
episodes = soup.find_all(href=re.compile("/episode/"), class_="movie")
for link in set(episodes):
    episodes_links.append(link['href'])

opt = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=opt)

for link in episodes_links:
    try:
        driver.get(link)
        clickHereLinks = driver.find_element_by_css_selector("#watch_dl > table > tbody > tr:nth-child(" + str(
            quality) + ") > td.tar > a.nop.btn.b.dl._open_window").click()
        driver.switch_to.window(driver.window_handles[-1])
        DownloadLink = driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").get_attribute("href")
        download_links.append(DownloadLink)

        # clickDownloadLink = driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").get_attribute("href")

    except NoSuchElementException:
        c.append(link)
        continue
print(download_links)
print(c)
final = []

for goToVidStream in download_links:
    i = 0
    if "egybest" in goToVidStream:

        print(goToVidStream)

    else:
        driver.get(goToVidStream)
        try:

            DownloadLink = driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").get_attribute("href")

            if DownloadLink is None:
                DownloadLink = driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").click()
            else:

                final.append(DownloadLink)

        except:
            continue

with open(str(name) + '.txt', 'a') as f:
    final.sort()

    for item in final:
        f.write("%s\n" % item)
