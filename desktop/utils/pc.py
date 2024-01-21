

import os
import platform
from datetime import datetime

import cpuinfo
import psutil
import requests


class PCInfo:
    def get_size(self,bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def System_information(self,):
        uname = platform.uname()
        system = uname.system
        host = uname.node
        win = uname.version
        processor = cpuinfo.get_cpu_info()['brand_raw']
        boot_time = psutil.boot_time()
        boot_time = datetime.fromtimestamp(boot_time)
        boot_time = f"{boot_time.year}/{boot_time.month}/{boot_time.day} {boot_time.hour}:{boot_time.minute}:{boot_time.second}"
        ram = f"{self.get_size(psutil.virtual_memory().total)}"
        username = os.getlogin()
        ip = requests.get("https://ip.seeip.org/jsonip?").json()['ip']

        return system, host, win, processor, boot_time, ram, username, ip


