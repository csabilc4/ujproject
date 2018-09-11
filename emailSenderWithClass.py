#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

currentDate = time.strftime(" %Y.%m.%d-%H:%M:%S")

class EmailSender:
    def __init__(self, receivers, ccopy = '', subjectText = 'Valami cím kell ide...éáűőúöüóí', massageText = 'Valami szöveg kell ide ..éáűőúöüóí'):
        self.receivers = receivers
        self.subjectText = subjectText
        self.massage = MIMEText(massageText, 'plain', 'UTF-8')
        self.massage['Subject'] = str(Header(subjectText + currentDate, 'UTF-8'))
        self.massage['To'] = receivers
        self.massage['Cc'] = ccopy
        self.sender = 'revolve@revolve.hu'
        self.password = "GardA2006"
        self.massage['From'] = self.sender

    def sendEmail(self):
        try:
            # Define to/from, texts
            # sender = 'revolve@revolve.hu'
            # password = "GardA2006"
            # receivers = 'nemeth.csaba@revolve.hu,motox@freemail.hu'
            # ccopy = 'nemeth.csaba@ingart.hu'
            # subjectText = "..............Python_zuhu_smtp_mail.............éáűőúöüóí, dátum: " + currentDate
            # massageText = ("Teszt email!! éáűőúöüóí")

            # Create message
            # massage = MIMEText(massageText, 'plain', 'UTF-8')
            # massage['Subject'] = str(Header(subjectText + currentDate, 'UTF-8'))
            # massage['From'] = sender
            # massage['To'] = receivers
            # massage['Cc'] = ccopy

            # Create server object with SSL option, Perform operations via server
            smtpObj = smtplib.SMTP_SSL('smtp.zoho.com', 465)
            smtpObj.login(self.sender, self.password)
            smtpObj.sendmail(self.sender, self.receivers, self.massage.as_string())
            smtpObj.sendmail(self.sender, self.massage["To"].split(",") + self.massage["Cc"].split(","), self.massage.as_string())
            smtpObj.quit()

            print "E-mail sikeresen elkuldve!"
        except:
            print "Hiba az e-mail küldése során!"


# print 'test OK!!!!!'

## Testing
if __name__ == '__main__':
    # print 'test OK!'
    pass