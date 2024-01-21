import random
import string
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class Tools:
    def __init__(self):
        self.Session = requests.Session()


    def Souper(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def Requester(self, link, headers=None):
        return self.Session.get(link, headers=headers).content

    def Domainer(self, url):
        return urlparse(url).netloc

    def Compact(self, lst):
        return list(filter(None, lst))

    def FilterListByHttps(self, lst):
        return list(filter(lambda x: x.startswith('https'), lst))

    def GenrateId(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def isChromeInstalled(self):
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
            return True
        except:
            return False
