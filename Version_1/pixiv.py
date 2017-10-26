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

def init():
    b = webdriver.Chrome()
    b.get("https://pixiv.net")
    slp()
    login_button = b.find_element_by_class_name('signup-form__submit--login')
    login_button.click()
    slp()
    email_button = b.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[1]/input')
    password_button = b.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[2]/input')
    email_button.send_keys("username")
    password_button.send_keys("Password")
    submit_button = b.find_element_by_xpath('//*[@id="LoginComponent"]/form/button')
    submit_button.click()
    slp()
    search_button = b.find_element_by_xpath('//*[@id="suggest-input"]')
    search_button.send_keys(u'碧蓝航线')
    search_button.send_keys(Keys.RETURN)
    close_ar = b.find_element_by_tag_name('body')
    close_ar.click()
    return b

def begin_task(imageURL_to_num):
    
    for imageURL,nums in imageURL_to_num.items():
        for i in range(nums):
            imageURL_temp_jpg = imageURL[:20] + "img-original" + imageURL[40:75] + str(i) + ".jpg" 
            print imageURL_temp_jpg , "---"
            imageURL_temp_png = imageURL[:20] + "img-original" + imageURL[40:75] + str(i) + ".png" 
            print imageURL_temp_png , "---"
            refererURL_temp = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + imageURL[65:73]
            print refererURL_temp ,"---"
            downLoadImageURL(refererURL_temp,imageURL_temp_jpg)
            downLoadImageURL(refererURL_temp,imageURL_temp_png)
            slp()
         
def main():
    b = init()
    imageURL_to_num = {}
    while(True):
        slp()
        scoll(b)
        all_pic_div = b.find_element_by_xpath('//*[@id="js-react-search-mid"]')
        bsobj = bs(all_pic_div.get_attribute('innerHTML'),"lxml")
        list = bsobj.findAll(attrs={"data-src": True , "class" : "lazyloaded"})
        list_num = bsobj.findAll("span" ,attrs={"class" : ''})
        for i in list:
            print i['src']
            imageURL_to_num[i['src']] = 1
        for i in list_num:
            if i.find_parent().find_next_sibling(attrs={"data-src": True , "class" : "lazyloaded"}) != None:
                print i.get_text(),i.find_parent().find_next_sibling(attrs={"data-src": True , "class" : "lazyloaded"})['src']
                imageURL_to_num[i.find_parent().find_next_sibling(attrs={"data-src": True , "class" : "lazyloaded"})['src']] = int(i.get_text())
        for k,v in imageURL_to_num.items():
            print k, " " , v
        begin_task(imageURL_to_num)
        imageURL_to_num = {}
        next_page = b.find_element_by_xpath('//*[@id="wrapper"]/div[1]/div/nav/div/span[2]')
        if next_page.get_attribute("innerHTML") == u'':
            break
        next_page.click()
        slp()

def slp():
    time.sleep(randint(1, 5))

def downLoadImageURL(refererURL,imageURL):
    headers = {
    "User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    headers['Referer'] = refererURL
    r = req.get(imageURL,headers=headers)
    if r.status_code == 200:
        open(imageURL[-15:], 'wb').write(r.content)
    else:
        print "Error !",imageURL
        
def scoll(b):
    try:
        js = "window.scrollTo(0,"
        for i in range(6):
            js_temp = js + str(i*1000) + ');'
            b.execute_script(js_temp)
            slp()
    except Exception as e:
        print e

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Process some integers.')
    #parser.add_argument()
    #args = parser.parse_args()
    main()


#当前页面有的
#    单张：https://i.pximg.net/c/240x240/img-master/img/2017/10/25/03/08/38/65585282_p0_master1200.jpg
#    id: /member_illust.php?mode=medium&illust_id=65585282
#    无 span
#    原图 ： https://i.pximg.net/img-original/img/2017/10/25/03/08/38/65585282_p0.png#
#
#    多张：https://i.pximg.net/c/240x240/img-master/img/2017/10/25/01/36/49/65584485_p0_master1200.jpg
#    id: /member_illust.php?mode=medium&illust_id=65584485
#    a的子一级的div span 里有数字 图片个数#
#
#    原图 ： https://i.pximg.net/img-original/img/2017/10/25/01/36/49/65584485_p0.jpg
#    原图 ： https://i.pximg.net/img-original/img/2017/10/25/01/36/49/65584485_p1.jpg