#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

currentDate = time.strftime(" %Y.%m.%d-%H:%M:%S")

class EmailSender:
    def __init__(self):
        # Define sender/Pwd
        self.sender = 'revolve@revolve.hu'
        self.password = "GardA2006"

    def sendEmail(self, receivers, ccopy = '', subjectText = 'Default Subject...éáűőúöüóí', massageText = 'Default Text...éáűőúöüóí'):
        try:
            # Create message
            self.receivers = receivers
            self.subjectText = subjectText
            self.massage = MIMEText(massageText, 'plain', 'UTF-8')
            self.massage['Subject'] = str(Header(subjectText + currentDate, 'UTF-8'))
            self.massage['To'] = self.receivers
            self.massage['Cc'] = ccopy
            self.massage['From'] = self.sender

            # Create server object with SSL option, Perform operations via server
            smtpObj = smtplib.SMTP_SSL('smtp.zoho.com', 465)
            smtpObj.login(self.sender, self.password)
            smtpObj.sendmail(self.sender, self.receivers, self.massage.as_string())
            smtpObj.sendmail(self.sender, self.massage["To"].split(",") + self.massage["Cc"].split(","), self.massage.as_string())
            smtpObj.quit()

            print "E-mail sikeresen elkuldve!"
        except:
            print "Hiba az e-mail küldése során!"

## Testing
if __name__ == '__main__':
    print 'TEST OK!'
    pass