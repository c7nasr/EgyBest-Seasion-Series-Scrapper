import requests
from bs4 import BeautifulSoup
import re
# c = requests.get("https://deer.egybest.biz/episode/perry-mason-season-1-ep-6")
#
# print(c.content[''])

# c= "qr0onHXmk4yLFjXCu3Ezqqh3o30dByiXvERXgthiQ2iJvPCTp%2ChsZjO-EPlWKWNf-rpQG4La7Ra3Gvk8O4pBBRBUyN-99IWWeZTaq%2C%2CYTLtk7uSD1uZmkRR%2CEEXBDI8qo"
# api = "https://deer.egybest.biz/api?call=VcccSZBcScKcSqATPqpjWbKaSKScScCqcScKcSblVtqcryHHSHEtlmcFgCKcSKScSHNbcScKcSqYcqcqjqqScSKScSlkfPHNjlsScKqYcKTSKHqPqPKHqKqKKScSHNLcScKcSqYjBmKqUmcqUmqqPcSKScSjDQcScKcSmucHLqsSKScSbNBScKcSkNBNbNsnrKmcScP&auth=e253c99c6f4145955ae9acc295141b9c"

# req = requests.get("https://vidstream.kim/")
#
# print(req.cookies['PHPSID'])
# headers={
#
#     'cookie':"PHPSID="+str(req.cookies['PHPSID'])+ ";"
# }
# req2 = requests.get("", headers=headers)
#
# print(req2.headers)
# soup = BeautifulSoup(req2.content, 'html.parser')
# episodes = soup.find_all(class_="bigbutton")

# print(episodes)
#
#
#
# print(episodes[0]['href'])

import json

from selenium import webdriver

opt = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=opt)
driver.get("https://deer.egybest.biz/episode/perry-mason-season-1-ep-3/?ref=tv-p1")
agent = driver.execute_script("return navigator.userAgent")

print(agent)

