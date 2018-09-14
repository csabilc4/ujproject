#!/usr/bin/env python
# coding=utf-8
import IPython.core.inputtransformer
from bs4 import BeautifulSoup
import requests

# import emailSenderWithClass
import emailSender


class Page:
    '''parse datas from website'''
    pass

def siteParser(url):
    getSite = requests.get(url)

    # soup = BeautifulSoup(getSite.text, 'html.parser')
    soup = BeautifulSoup(getSite.text, 'lxml')
    # print soup.prettify()

    mailText = '\n******************NEHOGY LEMARADJ VALAMI AKCIOROL*******************\n'
    mailText += '**************************RCZ CRAZY PRICES**************************\n\n'
    for item in soup.find_all('li', class_='item'):
        # print "--------------------------------------------------------------------"

        # Product title
        try:
            title = item.find('a', class_='product-image')['title']
        except:
            title = "NO PRODUCT TITLE"
        # print title#, type(title)

        # Product link
        try:
            link = item.find('a', class_='product-image')['href']
        except:
            link = "NO PRODUCT LINK"
        # print link#, type(link)

        # Product image
        try:
            image = item.find('img')['src']
        except:
            image = "NO IMAGE"
        # print image#, type(image)

        # Product price
        price = item.find('span', class_='price').text
        if "K" in price:
            price = "OUT OF STOCK"
        price = price.strip()
        # print price.strip()#, type(price)

        # print "--------------------------------------------------------------------"
        # print "\n"

        mailText += '--------------------------------------------------------------------\n'
        mailText += title + '\n'
        mailText += link + '\n'
        mailText += image + '\n'
        mailText += price + '\n'
        mailText += '--------------------------------------------------------------------\n\n'

    # print mailText
    return mailText

def send(mailT):
    # send=emailSenderWithClass.EmailSender()
    # send.sendEmail('nemeth.csaba@revolve.hu', subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked :)', massageText = 'asdfgh')

    emailSender.sendEmail('nemeth.csaba@revolve.hu,motox@freemail.hu,andras@pagem.hu', subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked és nekem :)', massageText = mailT)

def main():
    mailT = siteParser('http://www.rczbikeshop.com/default/sales/crazy-prices.html')
    send(mailT)

if __name__ == '__main__':
    main()
