import requests
import platform
import socket
import re
import uuid
import os
import psutil
from collections import namedtuple


class NSync:
    def __init__(self):
        self.API_LINK = "https://nhub-sync.herokuapp.com/sync/"
        self.headers = {
            'Content-Type': 'application/json'
        }

    def create_user(self):
        payload = {
            'session_id': str(self.session_id),
            'service': "EgyBest",
            'info': self.pc_info(),
        }
        requests.post(f"{self.API_LINK}user/new", json=payload)

    def update_user(self):
        payload = {
            'session_id': str(self.session_id),
            'data': self.sync_data,
            'ip': self.ip
        }
        requests.post(f"{self.API_LINK}user/update/egybest", json=payload)

    def pc_info(self):
        try:
            self.ip = requests.get(
                'http://ip.jsontest.com/').json()["ip"]
            info = {}
            info['platform'] = platform.system()
            info['PlatformRelease'] = platform.release()
            info['PlatformVersion'] = platform.version()
            info['architecture'] = platform.machine()
            info['hostname'] = socket.gethostname()
            info['LocalIP'] = socket.gethostbyname(socket.gethostname())
            info['ExternalIP'] = self.ip
            info['MacAddress'] = ':'.join(re.findall('..',
                                                     '%012x' % uuid.getnode()))
            info['processor'] = platform.processor()
            info['ram'] = str(
                round(psutil.virtual_memory().total / (1024.0 ** 3)))+" GB"
            info['username'] = os.getlogin()
            return info
        except Exception as e:
            self.info_box("It's Look like you aren't connected to internet!")
            exit()
