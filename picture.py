import requests
import os
from bs4 import BeautifulSoup

def download_image(url, save_path):#定义了下载的函数
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

os.makedirs('images', exist_ok=True)#创建存放图片的文件夹

#这是伪装
op={"usetr-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"}

for w in range(1,2):#这个循环可以规定爬的页数
    a=requests.get("https://5ixmt.com/ss               yx/slg-ssyx/page/{}/".format(w),headers=op)

    html=a.text
    qw=BeautifulSoup(html,"html.parser")

    text=qw.find_all('img')#找有img标签的

    for i in text:
        img_url = i.get('data-src')#找date——src的值
        print(img_url)
        if img_url and img_url.startswith('http'):#再次确定是不是http
            img_name = img_url.split('/')[-1]#获取文件名
            save_path = os.path.join('images', img_name)#路径
            download_image(img_url, save_path)#调用下载函数
            print(f"Downloaded: {img_url}")

