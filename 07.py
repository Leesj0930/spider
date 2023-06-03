import requests
import os
from bs4 import BeautifulSoup
import moviepy.editor as mp

import random

url="https://29maoek.com/vodtypehtml/9_2.html"
header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) App\
        leWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg\
        /113.0.1774.57"}
html_vidio=[]

response=requests.get(url,headers=header)
text=response.text
html=BeautifulSoup(text,"html.parser")

html_url=html.find_all("a",class_="videoinfo")

for i in html_url:
    html_vidio.append(i['href'])


vidio_url="https://29maoek.com/"+html_vidio[8]
response=requests.get(vidio_url,headers=header)
text=response.text
html=BeautifulSoup(text,"html.parser")

video_html=html.find("video")

video_url=video_html.get("src")












# if __name__=="__main__":



