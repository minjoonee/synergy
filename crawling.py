import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import  os

url = "https://it.jbnu.ac.kr/itjbnu/2016/inner.php?sMenu=G1000"
html = urlopen(url).read() # read
soup = BeautifulSoup(html, "html.parser")

type(soup.get_text()) # change string value
a_tag = soup.select('span > a')
print(a_tag)



"""
for i in  range(5,13):
    span = soup.find_all('span')[i].text;
    print(span);
href= soup.find_all('span');

print(href); # <print a tag>

"""
