import pip._vendor.requests as req
import typing
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib.request
import time
import os

def createFolder(folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print("")


def make_target_URL(keywords : str) -> str:
    splited_key = keywords.split(" ")
    rejoined_key = "+".join(splited_key)
    new_URL_head = "https://www.bing.com/images/search?q="
    new_URL_tail = "&FORM=HDRSC2"
    new_URL_full = new_URL_head + rejoined_key + new_URL_tail
    return new_URL_full


def get_html(targetURL : str):
    ua = UserAgent()
    headerX = {'User-Agent':'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.112.57'}
    r = req.get(targetURL,headers=headerX)
    result_html = r.text
    f = open('bingS1.html', mode='wt',encoding='utf-8')
    f.write(result_html)
    f.close()
    return result_html

def return_img_data_src(html : str) -> list :
    soup = BeautifulSoup(html, 'html.parser')
    img_list = soup.find_all("img", class_="mimg vimgld")
    count = 0
    data_src_list = []
    for ea in img_list :
        count = count + 1
        data_src_list.append(ea.get('data-src'))
    return data_src_list

def return_url_filename_tuple(url_list : list, nametopic: str) -> list:
    count = 0
    numbering = ""
    listX = []
    splited_nametopic = nametopic.split(" ")
    rejoined_nametopic = "_".join(splited_nametopic)
    createFolder(rejoined_nametopic)
    new_file_path = os.getcwd() + "\\" + rejoined_nametopic
    for ea in url_list:
        count = count + 1
        numbering = str(count).zfill(3)
        newfilename = new_file_path + "\\" + rejoined_nametopic + "_" + numbering + ".jpeg"
        newtuple = (ea,newfilename)
        listX.append(newtuple)
    return listX

def download_image(url : str, filename : str) -> str:
    try:
        urllib.request.urlretrieve(url,filename)
        print(filename, "-> download")
    except:
        print(filename," -> not downloaded")
    finally:
        return filename


def super_work(key_word : str):
    html = get_html(make_target_URL(key_word))
    src_list = return_img_data_src(html)
    url_filename_tuple = return_url_filename_tuple(src_list, key_word)

    print(" list len : ",len(url_filename_tuple))
    for fea in url_filename_tuple:
        time.sleep(0.88)
        download_image(fea[0],fea[1])
    time.sleep(0.71)

# Bing에서 검색할 키워드가 있는 텍스트파일을 입력
#with open("city_area3.txt","r") as f:
#    while True:
#        line = f.readline()
#        if not line:
#            break
#        else :
#            super_work(line.rstrip('\n'))
