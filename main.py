from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

CHROMEDRIVER_PATH = "C:\chromedriver.exe"
URL = "https://www.google.com"

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=600,600")

driver = webdriver.Chrome(executable_path = CHROMEDRIVER_PATH ,chrome_options = options)
driver.get(URL)

#用xpath定位搜尋Textbox
search_input = driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
#輸入搜尋
search_input.send_keys("hello selenium ^_^")
#按下Enter
search_input.send_keys(Keys.ENTER)

os.system("pause")

driver.close()
