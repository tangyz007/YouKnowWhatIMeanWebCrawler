#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from random import randint
import requests as req
import argparse
import time
import gc
import re

b = webdriver.Chrome()
b.get("https://tumblr.com")
time.sleep(2)
login_button = b.find_element_by_id("signup_login_button")

login_button.click()
email_button = b.find_element_by_id('signup_determine_email')
email_button.send_keys("username")

time.sleep(2)
login_button = b.find_element_by_id('signup_forms_submit')
login_button.click()
time.sleep(2)
password_button = b.find_element_by_id('signup_password')
password_button.send_keys("password")
login_button.click()

b.get("https://www.tumblr.com/likes")

js = "window.scrollTo(0,1000);"
b.execute_script(js)

all_Html = b.find_element_by_tag_name('body')
all_Html.get_attribute('innerHTML')

