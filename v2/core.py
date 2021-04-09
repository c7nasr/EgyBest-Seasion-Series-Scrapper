
import os
import re
import humanize
import requests
import sys
import time
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QTableWidgetItem
from selenium import webdriver
from urllib import request


def get_correct_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class EgybestLogic:
    def __init__(self):
        self.gecko = get_correct_path("geckodriver.exe")
        self.episodes_links = []
        self.season_name = ""
        self.direct_links = []
        self.sizes = []
        self.selected_quality = "1080p"

    def fetch_info(self):
        if self.state == "season":
            self.handle_season()
        elif self.state == "series":
            # self.handle_series()
            pass

    def handle_season(self):
        page = requests.get(self.url)
        self.change_status("Getting Season Info .... ")
        soup = BeautifulSoup(page.content, 'html.parser')
        slug = self.url.split("/season/")
        self.slug = slug[1].replace("/", "")
        season_name_div = soup.find(class_="movie_title")
        for tag in season_name_div:
            self.season_name = tag.text
        episodes = soup.find_all(href=re.compile("/episode/"), class_="movie")
        for link in set(episodes):
            self.episodes_links.append(link['href'])
        self.episodes_links.sort()
        print(self.episodes_links)
        self.tableWidget.setRowCount(len(self.episodes_links))
        for i, episode in enumerate(self.episodes_links):
            self.tableWidget.setItem(
                i, 0, QTableWidgetItem(str(f"Episode {i+1}")))
            self.tableWidget.setItem(
                i, 1, QTableWidgetItem(str("0.00 MB")))
            self.tableWidget.setItem(
                i, 2, QTableWidgetItem(str("Fetching info...")))
            self.tableWidget.setItem(
                i, 3, QTableWidgetItem(str(self.season_name)))

        self.change_status("Fetching Direct Link Started .... ")

    def single_episode_info(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        self.driver = webdriver.Chrome(options=chrome_options)
        for i, episode in enumerate(self.episodes_links):
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str("Phase I")))
            req = requests.get(episode)
            soup = BeautifulSoup(req.content, 'html.parser')
            stream_link = soup.find(class_="auto-size")['src']
            self.change_status(f"Fetching Episode {i+1} ")
            self.driver.get(f"https://{self.base_domain}{stream_link}")
            self.driver.find_element_by_xpath('/html/body/div').click()
            while "&r" not in self.driver.current_url:
                time.sleep(2)
            else:
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(str("Phase II")))
                self.driver.find_element_by_xpath('/html/body/div').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div').click()
                self.driver.find_element_by_xpath('/html/body/div').click()
                while True:
                    try:
                        self.driver.find_element_by_xpath(
                            '//*[@id="video"]/div[4]/div[14]/button').click()
                        self.driver.find_element_by_xpath(
                            '//*[@id="video"]/div[4]/div[14]/div/ul/li[1]').click()
                        break
                    except:
                        time.sleep(0.1)
                        continue
                self.tableWidget.setItem(
                    i, 2, QTableWidgetItem(str("Phase III")))
                self.listener(i)
        self.driver.quit()
        self.save_and_clean()

    def listener(self, i):
        is_found = False
        while not is_found:
            JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
            network_requests = self.driver.execute_script(
                JS_get_network_requests)
            for n in network_requests:
                self.driver.find_element_by_xpath('/html/body/div').click()
                if ".m3u8" in n["name"]:
                    is_HD = self.check_filename(n["name"], i)
                    if is_HD:
                        self.driver.delete_all_cookies()
                        self.change_status(f"Episode {i+1} Done")
                        is_found = True
                    else:
                        self.change_status("Listening ..")

    def check_filename(self, url, i):
        url = url.replace("/stream/", "/dl/")
        url = url.replace("/stream.m3u8", "")
        filename = request.urlopen(request.Request(url)).info().get_filename()
        file_size = request.urlopen(request.Request(
            url)).info()["Content-Length"]
        if self.selected_quality in filename:
            self.direct_links.append(url)
            self.sizes.append(int(file_size))
            file_size = humanize.naturalsize(file_size)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(file_size)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str("Done")))
            return True
        else:
            return False

    def save_and_clean(self):
        try:
            with open(self.season_name + '.txt', 'w') as f:
                for item in self.direct_links:
                    f.write("%s\n" % item)
            self.episodes_links = []
            self.direct_links = []
            self.season_name = ""
            self.tableWidget.setRowCount(0)
            self.lineEdit.clear()
            self.change_status("Done, Waiting New Session ..")
            self.pushButton.setEnabled(True)
            self.msgbox_thread("Done, {} Saved in text file. Total Season(s) Size: {}".format(
                self.season_name, humanize.naturalsize(sum(self.sizes))))
        except Exception as e:
            print(e)
