import requests
import os
from bs4 import BeautifulSoup

import re
import random

url="https://29maoek.com/vodtypehtml/9_2.html"#链接

header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) App\
        leWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg\
        /113.0.1774.57"}
html_vidio=[]#储存一级链接

#请求一级链接
response=requests.get(url,headers=header)
text=response.text
html=BeautifulSoup(text,"html.parser")


html_url=html.find_all("a",class_="videoinfo")
for i in html_url:
    html_vidio.append(i['href'])


# vidio_url="https://29maoek.com/"+html_vidio[8]
vidio_url="https://29maoek.com/maoplay/254442_1_1.html"
response=requests.get(vidio_url,headers=header)



pattern = r'var player_aaaa=(.*?);'
match = re.search(pattern, response.text)
if match:
    player_aaaa_value = match.group(1)
    print(player_aaaa_value)
else:
    print("No match found.")



# a=re.search(r'var player_aaaa=(.*?);',response.text)
# print(a)


# print(response.text)
















# if __name__=="__main__":



