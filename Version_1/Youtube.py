from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Chrome()
b.get("https://youtube.com")
time.sleep(2)
search_button = b.find_element_by_id("search")
search_button.send_keys("ASMR")
