import random
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

from subprocess import CREATE_NO_WINDOW

class BypassAds:
    def __init__(self, xpath_element_to_trigger, url):
        self.element = xpath_element_to_trigger
        self.url = url

    def bypass(self, driver):
        while True:
            driver.get(self.url)
            if len(driver.find_elements(By.CLASS_NAME, "vjs-logo")) == 0:
                try:
                    # 1: Click on the element to trigger the ad
                    driver.find_element(By.XPATH, self.element).click()
                    # 2: Wait for ad to open in new tab
                    if len(driver.window_handles) > 1:
                        # 3: Change to the new tab
                        self.GoToPage(driver=driver)
                        # 4: Return to the main tab
                        self.GoToPage(driver=driver, close=False)
                        # 5: Click on the element to trigger the ad again
                        driver.find_element(By.CLASS_NAME, "auto-size").click()
                        # 6: Switch to the new tab
                        self.GoToPage(driver=driver)
                        # 7: Return to the main tab
                        self.GoToPage(driver=driver,close=False)
                        # 8: Go to IFrame for checking if the ad is bypassed
                        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
                        if len(driver.find_elements(By.CLASS_NAME, "vjs-logo")) == 0:
                            continue
                        cookies = {"status": True, "cookie": "PSSID=" + driver.get_cookie("PSSID")['value']}
                        driver.close()
                        return cookies
                except Exception as e:
                    driver.close()
                    print("Something went wrong, i'm trying again")
                    return {"status": False}

    def GoToPage(self, driver, close=True):
        page = driver.window_handles[-1]
        driver.switch_to.window(window_name=page)
        time.sleep(random.randint(3, 5))
        if close:
            driver.close()

    def ChromeOptions(self):
        chromedriver_autoinstaller.install(cwd=True)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--log-level=OFF')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")

        return chrome_options

    def Run(self):
        service = ChromeService()
        service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(options=self.ChromeOptions(),service=service)
        return self.bypass(driver)

