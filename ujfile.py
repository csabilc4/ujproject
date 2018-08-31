#!/usr/bin/env python
# coding=utf-8

# print "ez itt a pycharmban készült, majd feltöltöm github-baaa"
# print "na ez egy diff"

# TODO ez itt egy

# todo ez is egy tudu!!


from os import listdir
from os import walk
from bs4 import BeautifulSoup
import time
import requests

mypath = "f:\Temp"

efiles = listdir(mypath)

f = []
maxFilename = 0
maxFile = ""

for (dirpath, dirnames, filenames) in walk(mypath):
    for files in filenames:
        # print files, len(files)
        if len(files) > maxFilename:
            maxFilename = len(files)
            maxFile = files

    # f.append(filenames)

# print 'Leghosszabb filenév hossza: \033[1;31m %d \033[0;30m karakter, a file neve: "%s"' % (maxFilename, maxFile)



r = requests.get('http://www.rczbikeshop.com/default/sales/crazy-prices.html')
# print r.text

soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('span', attrs={'class':'price'})

print len(results)
# print " ".join(results)
# print ''.join(str(results))
# print type(str((results[1])))
print str((results[1]))

currentDate = time.strftime("%Y%m%d_%H%M%S")

print currentDate