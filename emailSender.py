#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

currentDate = time.strftime("%Y%m%d_%H%M%S")

def sendEmail(receivers, sender = 'revolve@revolve.hu', password = "GardA2006", ccopy = '', subjectText = 'Valami cím kell ide...éáűőúöüóí', massageText = 'Valami szöveg kell ide ..éáűőúöüóí'):
    try:
        # Define to/from, texts
        # sender = 'revolve@revolve.hu'
        # password = "GardA2006"
        # receivers = 'nemeth.csaba@revolve.hu,motox@freemail.hu'
        # ccopy = 'nemeth.csaba@ingart.hu'
        # subjectText = "..............Python_zuhu_smtp_mail.............éáűőúöüóí, dátum: " + currentDate
        # massageText = ("Teszt email!! éáűőúöüóí")

        # Create message
        massage = MIMEText(massageText, 'plain', 'UTF-8')
        massage['Subject'] = str(Header(subjectText, 'UTF-8'))
        massage['From'] = sender
        massage['To'] = receivers
        massage['Cc'] = ccopy

        # Create server object with SSL option, Perform operations via server
        smtpObj = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        smtpObj.login(sender,password)
        smtpObj.sendmail(sender, receivers, massage.as_string())
        smtpObj.sendmail(sender, massage["To"].split(",") + massage["Cc"].split(","), massage.as_string())
        smtpObj.quit()

        print "E-mail sikeresen elkuldve!"
    except:
        print "Hiba az e-mail küldése során!"