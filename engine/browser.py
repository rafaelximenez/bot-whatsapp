from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import os

class Browser:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()

        chromedriver_autoinstaller.install()

        profile = os.path.join(os.getcwd(), "profile", "wpp")

        #chrome_options.add_argument("--user-data-dir=./tmp/browser/")
        chrome_options.add_argument(r"user-data-dir={}".format(profile))
        chrome_options.add_argument("--profile-directory=Default")
        

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    
    def __del__(self):
        self.driver.close()