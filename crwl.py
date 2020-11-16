import pip._vendor.requests as req
import typing
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
#r = req.get("http://hleecaster.com/python-web-crawling-with-beautifulsoup")
#html = r.text
#f = open('justHtml.html', mode='wt',encoding='utf-8')
#f.write(html)
#f.close()
#soup = BeautifulSoup(html,'html.parser')

#https://www.bing.com/images/search?q=cosmos+flower&form=HDRSC2&first=1&scenario=ImageBasicHover
#https://www.bing.com/images/search?q=rose%20flower&qs=n&form=QBIR&sp=-1&pq=rose%20flower&sc=7-11&cvid=6949EEA2CB5A404C894055242B07B719&first=1&scenario=ImageBasicHover
#https://www.bing.com/images/search?q=rose+flower&form=HDRSC2&first=1&scenario=ImageBasicHover
#https://www.bing.com/images/search?q=new%20york%20city&qs=n&form=QBIR&sp=-1&pq=new%20york%20city&sc=8-13&cvid=5119A666DB5249F6838E3D3A21F68ECC&first=1&scenario=ImageBasicHover
#https://www.bing.com/images/search?q=new+york+city&form=HDRSC2&first=1&scenario=ImageBasicHover

def make_target_URL(keywords : str) -> str :
    splited_key = keywords.split(" ")
    rejoined_key = "+".join(splited_key)
    #https://www.bing.com/images/search?q=new+york+city&form=HDRSC2&first=1&scenario=ImageBasicHover
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
        print(count, " : ", ea.get('data-src'))
        data_src_list.append(ea.get('data-src'))
    return data_src_list

def return_url_filename_tuple(url_list : list, nametopic: str) :
    count = 0
    numbering = ""
    listX = []
    for ea in url_list:
        count = count + 1
        numbering = str(count).zfill(3)
        newfilename = nametopic + numbering
        newtuple = (ea,newfilename)
        listX.append(newtuple)
    print(listX)  

def download_image(url : str, filename : str) -> str:
    urllib.request.urlretrieve(url,filename)
    return filename

html = get_html(make_target_URL("new york city"))
src_list = return_img_data_src(html)
return_url_filename_tuple(src_list, "newyork")




