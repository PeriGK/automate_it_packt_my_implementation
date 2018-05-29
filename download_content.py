from bs4 import BeautifulSoup
import re
import requests
import os

image_type = 'Project'
movie = 'Avatar'
url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch'.format(movie)

header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(url).content, "lxml")

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]

for img in images:
    print("Image sources: {}".format(img))
    raw_img = requests.get(img).content
    cntr = len([i for i in os.listdir(".") if image_type in i]) + 1
    f = open(image_type + "_"+ str(cntr)+".jpg", 'wb')
    f.write(raw_img)
    f.close()