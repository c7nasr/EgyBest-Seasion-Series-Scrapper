import os
import re
import sys
import threading
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def handle_quality(q):
    if q == "1080p":
        quality = 1
    elif q == "720p":
        quality = 2
    elif q == "480p":
        quality = 3
    elif q == "360p":
        quality = 4
    else:
        quality = 1
    return quality


def get_correct_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class egybest:
    def __init__(self):
        self.seasons_links = []
        self.episodes_links = []
        self.api_call = []
        self.download_links = []
        self.video_stream_links = []
        self.scrapping_thread = None
        self.slug = ""
        self.root = tk.Tk()
        self.root.style = ttk.Style()
        self.root.style.theme_use("vista")
        self.opt = webdriver.ChromeOptions()
        self.opt.add_argument("hide_console")
        self.chrome_path = get_correct_path("chromedriver.exe")
        self.args = ["", ]
        self.opt.add_argument('headless')

        w = self.root.winfo_reqwidth()
        h = self.root.winfo_reqheight()
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('+%d+%d' % (x, y))
        self.root.resizable(False, False)
        self.root.title("Egy.best")

        self.status_text = tk.StringVar(self.root)

        ttk.Label(self.root, text="لينك السيزون").grid(sticky="e", padx=2, )
        season_link = tk.StringVar(self.root)

        self.s_link = ttk.Entry(self.root, textvariable=season_link)
        self.s_link.grid(sticky="n,s,e,w", pady=5, padx=2, )

        ttk.Label(self.root, text="اختار الجوده").grid(sticky="e", padx=2, )
        quality = tk.StringVar(self.root)
        choices = ["لو مخترتش  هديك اعلا جوده", '1080p', '720p', '480p', '360p']
        quality.set(choices[0])  # set the default option

        self.option_menu = OptionMenu(self.root, quality, *choices)
        self.option_menu.grid(sticky="n,s,e,w", padx=2)

        user_request_selection = tk.StringVar()
        user_request_selection.set("1")

        self.status = ttk.Label(self.root, textvariable=self.status_text)
        self.status.grid(sticky="e", pady=10, )
        self.status_text.set("الحاله: مستنينك تدوس")

        self.start = ttk.Button(self.root, text="هات اللينكات المباشره",
                                command=lambda: self.handle_link(quality.get(), user_request_selection.get(),
                                                                 season_link.get()))

        self.start.grid(sticky="n,s,e,w")

        def on_closing():
            self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        self.root.mainloop()

    def handle_link(self, q, req, link):

        if "season/" not in link:
            messagebox.showerror("مينفعش!", "لازم اللينك يكون بتاع السيزون مش بتاع حلقه من المسلسل.")
        else:
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            slug = link.split("season/")
            slug = slug[1].replace("/", "")
            self.slug = slug.split("?")[0]

            episodes = soup.find_all(href=re.compile("/episode/"), class_="movie")
            for link in set(episodes):
                self.episodes_links.append(link['href'])

            quality = handle_quality(q)
            self.start_get_service(quality, req)

    def start_get_service(self, q, req):
        try:
            self.scrapping_thread = threading.Thread(target=self.get_download_urls, args=(req, q))
            self.scrapping_thread.daemon = True
            self.scrapping_thread.start()
            self.root.after(100, self.check_scrapping_thread)
        except Exception as e:
            print("oh im from start_submit_thread: " + str(e))

    def check_scrapping_thread(self):
        try:
            if self.scrapping_thread.is_alive():
                self.start.config(state='disabled')
                self.option_menu.config(state='disabled')
                self.s_link.config(state='disabled')
                self.root.after(100, self.check_scrapping_thread)
            else:
                self.start.config(state='normal')
                self.option_menu.config(state='normal')
                self.s_link.config(state='normal')


        except Exception as e:
            print("oh im from check_submit_thread: " + str(e))

    def sync_with_db(self):
        print(self.slug)

    def get_download_urls(self, req, q):
        self.status_text.set("الحاله: ما قبل الطور الاول")

        global w
        global agent
        global i

        driver = webdriver.Chrome(self.chrome_path, options=self.opt, service_args=self.args)
        not_valid = []
        driver.get(self.episodes_links[0])
        cookie = driver.get_cookie("PSSID")['value']
        print(cookie)
        i = 1
        for link in self.episodes_links:
            try:
                driver.get(link)
                self.status_text.set("الطور الاول الحلقه: " + str(i))
                agent = driver.execute_script("return navigator.userAgent")
                api = driver.find_element_by_css_selector("#watch_dl > table > tbody > tr:nth-child(" + str(
                    q) + ") > td.tar > a.nop.btn.g.dl._open_window").get_attribute('data-url')
                self.api_call.append(api)
                i += 1
            except NoSuchElementException:
                continue
        driver.quit()
        i = 1
        for call in self.api_call:
            self.status_text.set("الطور الثاني الحلقه: " + str(i))

            try:
                w = "https://deer.egybest.biz" + call
                headers = {
                    'user-agent': str(agent),
                    'cookie': "PSSID=" + str(cookie) + ";"
                }
                req = requests.post(w, headers=headers)
                soup = BeautifulSoup(req.content, 'html.parser')
                episodes = soup.find_all(href=re.compile("/v/"), class_="bigbutton")
                self.video_stream_links.append(episodes[0]['href'])
                i += 1
            except IndexError:
                print("Ex. But I'm gonna handle it xD")
                not_valid.append(w)
                continue

        if len(not_valid) > 0:
            print(not_valid)
            for not_v in not_valid:
                w = not_v
                headers = {
                    'user-agent': str(agent),
                    'cookie': "PSSID=" + str(cookie) + ";"
                }
                req = requests.post(w, headers=headers)
                print(req.content)
                soup = BeautifulSoup(req.content, 'html.parser')
                episodes = soup.find_all(href=re.compile("/v/"), class_="bigbutton")
                self.video_stream_links.append(episodes[0]['href'])
        self.get_last_links()

    def get_last_links(self):
        global i
        i = 1
        self.status_text.set("قبل الطور الاخير الحلقه: " + str(i))

        global sleep
        domains = [".kim", ".to", ".online"]
        valids = []

        for video in self.video_stream_links:
            video = video.replace("/v/", "/f/")
            for d in domains:
                link = "https://vidstream" + d + video
                req = requests.get(link)
                soup = BeautifulSoup(req.content, 'html.parser')
                is_valid = soup.find_all(class_="bigbutton")

                if len(is_valid) > 0:
                    valids.append(link)
                    i += 1
                    self.status_text.set("قبل الطور الاخير الحلقه: " + str(i))
        sleep = 5

        driver = webdriver.Chrome(self.chrome_path, options=self.opt, service_args=self.args)
        i = 1
        for l in valids:
            i += 1

            driver.get(l)
            time.sleep(sleep)

            dl = driver.find_element_by_xpath("/html/body/div[1]/div/p[2]/a[1]").get_attribute("href")
            self.status_text.set("الطور الاخير الحلقه: " + str(i))
            if dl is None:
                print("A none one")
            else:
                self.download_links.append(dl)
        # Best Method? And Not Valids to array
        driver.quit()
        self.status_text.set("خلصنا")

        self.save_to_text()

        messagebox.showinfo("مبروك!", "تمام. جيبنالك اللينكات وهتلاقيها في ملف تيكست بأسم السيزون والمسلسل")

    def save_to_text(self):
        with open(str(self.slug) + '.txt', 'a') as f:
            self.download_links = set(self.download_links)
            for item in self.download_links:
                f.write("%s\n" % item)

    # update status -> toDo


if __name__ == '__main__':
    app = egybest()
