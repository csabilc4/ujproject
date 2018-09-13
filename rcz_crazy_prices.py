#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
import requests


rrr = False
if rrr == True:
    r = requests.get('http://www.rczbikeshop.com/default/sales/crazy-prices.html')

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('span', attrs={'class':'price'})
    print len(results)
    # print " ".join(results)
    # print ''.join(str(results))
    # print type(str((results[1])))
    print str((results[1]))

