import requests
import os
from bs4 import BeautifulSoup

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

os.makedirs('images', exist_ok=True)

op={"usetr-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"}
for w in range(1,2):
    a=requests.get("https://5ixmt.com/ssyx/slg-ssyx/page/{}/".format(w),headers=op)

    html=a.text
    qw=BeautifulSoup(html,"html.parser")

    text=qw.find_all('img')
    # text=qw.find_all('img')
    # for i in text:
    #     print(i)
    for i in text:
        img_url = i.get('data-src')
        print(img_url)
        if img_url and img_url.startswith('http'):
            img_name = img_url.split('/')[-1]
            save_path = os.path.join('images', img_name)
            download_image(img_url, save_path)
            print(f"Downloaded: {img_url}")

