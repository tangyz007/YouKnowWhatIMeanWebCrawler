#coding:utf-8
from bs4 import BeautifulSoup as bs
from random import randint
import requests as req
import argparse
import time
import gc
import re

headers = {
"User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

def slp():
    time.sleep(randint(1, 5))

def mkdir(path):
    path = path.strip()
    path = path.rstrip('\')
    if not os.path.exists(path):
        os.makedirs(path)
        print 'mkdir ' + path + 'succuess'
        return True
    else:
        print 'mkdir' + path + 'error'
        return False
    
def downLoadImageURL(imageURL,folder):
    r = req.get(imageURL,headers=headers)
    if r.status_code == 200:
        open(imageURL[-15:], 'wb').write(r.content)
    else:
        print "Error !",imageURL

def search(keyWord):
    URL = "https://e-hentai.org" 

    r = req.get(URL,headers=headers)
    return bs(r.content,"lxml")
    

def main():
    hentai = {}
    b = init()
    a = search()
    list = a.findAll(attrs={'class':"it5"})
    for i in list:
        print i.find('a')['href']
        URL = i.find('a')['href']
        mkdir()
        temp = g(URL)
        hentai[URL] = temp
                
def g(URL):
    sub_hentai = {}
    r = res.get(URL,headers=headers)
    a = bs(r.content,"lxml")   
    list = a.findAll(attrs={'class':"gdtm"})
    for i in list:
        print i.find("a")['href']
        sub_URL = i.find("a")['href']
        temp = s(sub_URL)
        sub_hentai[sub_URL] = temp


def s(URL):
    r = res.get(URL,headers=headers)
    a = bs(r.content,"lxml")   
    img = a.find(attrs={'id':"img"})
    imgURL = img['src']
    return imgURL;

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Process some integers.')
    #parser.add_argument()
    #args = parser.parse_args()
    main()


# http://104.171.113.18:14901/h/9481a2a8936dc2da1637019e94afa4ad48d9759a-403997-1280-1844-jpg/keystamp=1508955900-e43fa08568;fileindex=37471025;xres=1280/1.jpg
# http://104.168.32.154:33333/h/a77be1cea02f6afab0f31cf71191710f00e8bb23-507698-1280-1844-jpg/keystamp=1508956200-0038ef2005;fileindex=37471042;xres=1280/3.jpg
# http://104.168.32.154:33333/h/a77be1cea02f6afab0f31cf71191710f00e8bb23-507698-1280-1844-jpg/keystamp=1508956200-0038ef2005;fileindex=37471042;xres=1280/3.jpg
# http://104.168.32.154:33333/h/a77be1cea02f6afab0f31cf71191710f00e8bb23-507698-1280-1844-jpg/keystamp=1508956500-0a3cd2c97f;fileindex=37471042;xres=1280/3.jpg
# http://104.171.113.18:14901/h/9481a2a8936dc2da1637019e94afa4ad48d9759a-403997-1280-1844-jpg/keystamp=1508956200-7a68c17fe7;fileindex=37471025;xres=1280/1.jpg
# http://205.185.122.226:27999/h/7b6092d5a96afbf57267abf44f312194c2ba308d-240091-1280-1824-jpg/keystamp=1508956800-3992493fc4;fileindex=55066081;xres=1280/p_001.jpg

# https://e-hentai.org/g/1133378/778cf05d80/ p=1 ...  class = ptds get all href
# https://e-hentai.org/g/1110729/64ed6b00db/ class = gdtm get all href
# https://e-hentai.org/?f_doujinshi=1&f_manga=1&f_artistcg=1&f_gamecg=1&f_western=1&f_non-h=1&f_imageset=1&f_cosplay=1&f_asianporn=1&f_misc=1&f_search=reCreator&f_apply=Apply+Filter
# https://e-hentai.org/?f_doujinshi=1&f_manga=1&f_artistcg=1&f_gamecg=1&f_western=1&f_non-h=0&f_imageset=1&f_cosplay=1&f_asianporn=1&f_misc=1&f_search=reCreator&f_apply=Apply+Filter
# https://e-hentai.org/s/2d2bd4a5a7/1133380-1
# https://e-hentai.org/s/71eb21c7ab/1133380-3
# https://e-hentai.org/s/6675c67690/1133380-40
# https://e-hentai.org/s/be9ae78ab2/1133348-1