#!/usr/bin/env python
# coding=utf-8

# print "ez itt a pycharmban készült, majd feltöltöm github-baaa"
# print "na ez egy diff"

# TODO ez itt egy

# todo ez is egy tudu!!


from os import listdir
from os import walk
from bs4 import BeautifulSoup
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


from emailSender import sendEmail
sendEmail('nemeth.csaba@revolve.hu', subjectText = 'Ez lesz a cím...éáűőúöüóí')

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header

rr = False
if rr == True:
    # Define to/from, texts
    currentDate = time.strftime("%Y%m%d_%H%M%S")
    sender = 'revolve@revolve.hu'
    password = "GardA2006"
    receiver = 'nemeth.csaba@revolve.hu,motox@freemail.hu'
    ccopy = 'nemeth.csaba@ingart.hu'
    subjectText = "..............Python_zuhu_smtp_mail.............éáűőúöüóí, dátum: " + currentDate
    massageText = ("Teszt email!! éáűőúöüóí")

    # Create message
    massage = MIMEText(massageText, 'plain', 'UTF-8')
    massage['Subject'] = str(Header(subjectText, 'UTF-8'))
    massage['From'] = sender
    massage['To'] = receiver
    massage['Cc'] = ccopy

    # Create server object with SSL option, Perform operations via server
    smtpObj = smtplib.SMTP_SSL('smtp.zoho.com', 465)
    smtpObj.login(sender,password)
    smtpObj.sendmail(sender, receiver, massage.as_string())
    smtpObj.sendmail(sender, massage["To"].split(",") + massage["Cc"].split(","), massage.as_string())
    smtpObj.quit()

    print "E-mail sikeresen elkuldve!"

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



exit()

class TestClass:
    def __init__(self):
        self.b = 2

    def start(self):
        bb = self.b * 2
        return bb

    def add(self):
        pass

    def plusOne(self):
        return self.add() + 1


c = TestClass()
c.a = 1
a= 22
print c.plusOne()

