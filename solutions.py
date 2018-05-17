#import libraries
import urllib2
from bs4 import BeautifulSoup

#1 getting the data

#get the URL
web_page = 'https://finance.yahoo.com/quote/FB?p=FB'

#query the website and return the html to the variable page:
page = urllib2.urlopen(web_page)
#print(page)

#parse the html page using Beautiful Soup and store in variable soup:
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

#remove div element and get its innerHTML content
name_box = soup.find('h1', attrs={'class': 'D(ib)'})
# print(name_box)

name = name_box.text.strip()
print(name)

price_box = soup.find('span', attrs={'class': 'Fw(b)'})
price = price_box.text
print(price)

#2 Exporting the data
import csv
from datetime import datetime

#open csv file with append, so that old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])