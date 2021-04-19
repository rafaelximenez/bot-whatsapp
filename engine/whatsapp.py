from engine.browser import *
import config
import urllib
import time

class Whatsapp(Browser):
    def __init__(self):
        super().__init__()
        self.driver.get(f'{config.BASE_URL}')
    
    def send_message(self, number, text):
        message = urllib.parse.quote(text)
        self.driver.get(f'{config.BASE_URL}/send?phone={number}&text={message}')

        xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        button_active = False
        while button_active == False:
            try:
                self.driver.find_element_by_xpath(xpath)
                button_active = True
                time.sleep(5)
            except:
                time.sleep(1)
        self.driver.find_element_by_xpath(xpath).send_keys(Keys.ENTER)