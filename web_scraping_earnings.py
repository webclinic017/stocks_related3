import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#from urllib import urlopen
import re
from bs4 import BeautifulSoup 
import requests
from lxml import html
from selenium import webdriver
driver = webdriver.Chrome()

import requests
p=['GPL','GOOS','GLS']
for x in p:
    u="https://www.barchart.com/stocks/quotes/'+str(x)+'/overview', headers={'User-Agent': 'Mozilla/5.0'}"
##    print(driver(get(u))
    page = requests.get(u)
    page

    soup = BeautifulSoup(page.content, 'html.parser')

##    print(soup.prettify())

    print(list(soup.children))


driver.close()
driver.quit()
##
##for x in p:
##    r = Request('https://www.barchart.com/stocks/quotes/'+str(x)+'/overview', headers={'User-Agent': 'Mozilla/5.0'})
##    webpage = urlopen(r).read()
##
##    webpage = webpage.decode('utf-8')
##
##    table = soup.title.name
##    print(x,'   ',table)
##    
####    for url in webpage.find('div', {"class=rating"}):
####        url = div.string
####        
##    print(webpage,'  ',x)

##    nav = soup.nav
##    for url in webpage.findall('a'):
##        print(url.get('href'))

##body = soup.body
##for paragraph in body.find_all('p'):
##    print(paragraph.text)    


'''
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
   

