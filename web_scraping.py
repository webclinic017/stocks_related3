import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.quantshare.com/index.php?option=manual&dir=/QuantShare%20Language/Candlestick%20Pattern//CdlInvertedhammer%200.html').read()
soup = bs.BeautifulSoup(source,'lxml')

nav = soup.nav
for url in nav.findall('a'):
    print(url.get('href'))

##body = soup.body
##for paragraph in body.find_all('p'):
##    print(paragraph.text)    



print('\n')
print('******************************************************************************************************************')
print('\n')

# title of the page
print(soup.title)
# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

print(soup.find_all('p'))


for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))

# https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/

for url in soup.find_all('a'):
    print(url.get('href'))


   







'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
html = urlopen("http://www.yahoo.com").read()
print(html)
##soup = BeautifulSoup(html, lxml').read()
soup = bs4.BeautifulSoup(html, 'lxml').read()                     

print(soup.prettify())



##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##from bs4 import BeautifulSoup
##import requests
##html = urlopen("http://www.yahoo.com").read()
##print(html)

# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup


##soup = BeautifulSoup(html, "lxml")
##print(soup.prettify()) # print the parsed data of html
##print(soup.title)

##for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
##    tds = row('td')
##    print (tds[0].string, tds[1].string)
##    # will print date and sunrise

##
##from pyquery import *
##
##html = PyQuery(url='http://www.example.com/')
##trs = html('table.spad tbody tr')
##
##for tr in trs:
##  tds = tr.getchildren()
##  print (tds[1].text, tds[2].text)

##import requests ; from bs4 import BeautifulSoup
##
##soup = BeautifulSoup(requests.get('https://www.flipkart.com/').text, "lxml")
##for link in soup.select('div._2kSfQ4'):
##    print(link.text)

'''
