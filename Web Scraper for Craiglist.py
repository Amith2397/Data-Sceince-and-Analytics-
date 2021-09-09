# -*- coding: utf-8 -*-
"""
A simple web scraper written in Python to extract the data from the web site (craiglist) using BeautifulSoup,
the result is saved in csv file.

The program can be further modified to work with areas/locations/categories of Craig’s list by
providing a few options that the user can select at run-time.

@author: amith
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
    
response = urlopen("craiglist link")
soup = BeautifulSoup(response,"lxml")
    
    
description = soup.find_all("a", class_="result-title hdrlnk")
f = open('sample.csv',"w",newline='')
writer = csv.writer(f)
for a in description:
   links = "craiglist link" + a.get('href') 
   timenDate = soup.find('time', class_= 'result-date')
   actualTnd = timenDate['title']
   txt = a.get_text()
            
   #print(txt, actualTnd, links) 
   list = [actualTnd, txt, links]
   writer.writerow(list)
f.close()

