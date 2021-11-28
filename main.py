import json
# **************************  code for captacha filling ************************
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
import requests
string='success'
lst=[]
# header = ['Ip']
with open("ip.txt","r",encoding='utf-8') as f:
    for i in f.readlines():
        for check in i.split("   "):
            if string in check:
                lst.append(check)
                # print(lst)
            else:
                pass
for i in lst:
    a=i.replace(" => success","").split()
    for j in range(1):
        a[j]
# s=Service('C:\\Users\\ACER\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe')
# browser = webdriver.Chrome(service=s)
# url='https://www.freeproxylists.net/'
# browser.get(url)
# browser.find_element_by_xpath("//*[@id='recaptcha-anchor']/div[1]").click()
# browser.find_element_by_xpath("//*[@id='contents']/center/form/input").click()
# time.sleep(50)
# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contents']/center/form/input"))).click()

headers = {
    'Accept-Encoding: gzip, deflate, br',
    'Accept-Language: en-US,en;q=0.9',
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    'Referer: https://www.google.com/'
    'Connection: keep-alive'
}
params = {
    'apikey':'d522aa9719ff5694d323sdvva64849ead313',
    'format' : 'json',
    'geocode' : '42.361145,-71.057092',
    'language' : 'en-US',
    'units':'e'
}
import pandas as pd
import csv
supertitle = []
superprice = []
super_manufacturer = []
stock = []
myurl ="https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"
uclient = uReq(myurl)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")
container= page_soup.findAll("div",{"class":"product"})
title = page_soup.findAll("div",{"class":"product-description"})

for j in title:
    supertitle.append(j.find("a")['href'].split('/')[3].replace('-',' ').strip(' '))
status = page_soup.findAll("span",{"class":"status"})

for s in status:
    if((s.find("span",{"class":"out-of-stock"}).text)=="stock"):
        stock.append("True")
    else:
        stock.append("False")

price = page_soup.findAll("span",{"class":"price"})

for p in price:
    superprice.append(p.text)

Manufacturer = page_soup.findAll("div",{"class":"catalog-item-brand-item-number"})
for p in Manufacturer:
    super_manufacturer.append(p.find("a")['href'].split('/')[2].split('-')[0])

# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
with open('filecontent','a') as f:
    for i in range(len(container)):
        # print(f"{'Title'}\t\t\t\t{'Price'}\t\t\t\t\{'Stock'}\t\t\t\t{'Manufacturer'}")
        f.write(f"{supertitle[i]} \t {superprice[i]} \t {stock[i]} \t {super_manufacturer[i]} \n")
file = 'filecontent'
dict = {}
with open('filecontent') as fn:
    for d in fn:
        key,desc = d.strip().split(None,1)
        dict[key] = desc.strip

otfile=open('output.json','w')
json.dump(dict,otfile)
otfile.close()

# for i in range(len(container)):
#     newdict = {
#         "Supertitle" : supertitle[i],
#         "Price" :  superprice[i],
#         "Stock" : stock[i],
#         "manufacturer" : super_manufacturer[i]
#
#     }
#     a = json.dumps(newdict)
#
# with open("my_file.json","w") as file:
#     file.write(a)
#
# print(a)



# data = list(zip(superprice,super_manufacturer,stock,supertitle))
# df = pd.DataFrame(data,columns=['superprice       ','super_manufacturer       ','stock','supertitle'])
# print(df)



    # writer.writerow(["SN", "Name", "Contribution"])
    # writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    # writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    # writer.writerow([3, "Guido van Rossum", "Python Programming"])
