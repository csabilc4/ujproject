#!/usr/bin/env python
# coding=utf-8

import IPython.core.inputtransformer
from bs4 import BeautifulSoup
import requests
import csv
import prettytable

# import emailSenderWithClass
import emailSender


class Page:
    '''parse datas from website'''
    pass


def makeCSV(url='http://www.rczbikeshop.com', csv_filename='rcz_csv.csv', sendCSV=False):
    # csv_file = open(csv_filename, 'w')
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['Title', 'Link', 'Price'])

    getSite = requests.get(url)

    soup = BeautifulSoup(getSite.text, 'html.parser')
    # soup = BeautifulSoup(getSite.text, 'lxml')
    # print soup.prettify()

    mailContent = '\n******************NEHOGY LEMARADJ VALAMI AKCIOROL*******************\n'
    mailContent += '**************************RCZ CRAZY PRICES**************************\n\n'
    for item in soup.find_all('li', class_='item'):
        # print "--------------------------------------------------------------------"

        # Product title
        try:
            title = str(item.find('a', class_='product-image')['title'])
            # title = type(_title)
            # title = '<a href = "http://example.com">' + title + '</a>'
        except:
            title = "NO PRODUCT TITLE"
            # print title, type(title)

        # Product link
        try:
            link = str(item.find('a', class_='product-image')['href'])
            # link = '<a href=' + link + '></a>'
            # link = "href='" + link
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
        # price = _price[1:]
        # price = _price.decode("UTF-8")

        if "K" in price:
            # TODO csak a termék saját weblapján jelenik meg az out of stock,
            # itt nem, ezért sosem lesz out of stock
            price = "OUT OF STOCK"
        price = price.strip()
        # print price.strip()#, type(price)

        # csv_writer.writerow([title, link, price])

        mailContent += '--------------------------------------------------------------------\n'
        mailContent += title + '\n'
        mailContent += link + '\n'
        mailContent += image + '\n'
        mailContent += price + '\n'
        mailContent += '--------------------------------------------------------------------\n\n'

    print mailContent
    # csv_file.close()

    # if sendCSV:
    #     mailContent = "csv lesz"

    return mailContent


def readCSV(csvFileName):
    with open(csvFileName, 'r') as csv_file:
        mailContent =  prettytable.from_csv(csv_file)
        print mailContent, type(mailContent)
        # mailContent = ""    #csv_file.readlines()

    return mailContent


def readHTML(htmlFileName):
    with open(htmlFileName, 'r') as html_file:
        mailContent = html_file.readlines()
        # print mailContent, type(mailContent)
        # mailContent = ""    #csv_file.readlines()

    return mailContent


def makeTABLE(csvFileName):

    with open(csvFileName, 'r') as csv_file:
        print prettytable.from_csv(csv_file)
        mailContent = csv_file.readlines()

    return mailContent


def makeHTML(csvFileName, htmlFileName):
    with open(csvFileName, 'r') as csv_file:
        line = csv_file.readline()
        lineList = line.split(",")
        table = prettytable.PrettyTable(lineList)
        table.format = True

        while 1:
            line = csv_file.readline()
            if line == '':
                break
            lineList = line.split(",")
            table.add_row(lineList)

        htmlTable = table.get_html_string(
                        header = True,
                        padding_width = 2,
                        border = True,
                        hrules = prettytable.ALL,
                        vrules = prettytable.ALL,
                        # reversesort = True,
                        attributes = {"name": "my_table", "class": "red_table"})

    with open("rcz_html_sample.html", 'r') as sampleHtml_file:
        sampleContent = sampleHtml_file.readlines()

    with open(htmlFileName, 'w') as html_file:
        html_file.writelines(sampleContent)
        html_file.write(htmlTable)


def send(mailContent):
    # send=emailSenderWithClass.EmailSender()
    # send.sendEmail('nemeth.csaba@revolve.hu', subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked :)', massageText = 'asdfgh')

    emailSender.sendEmail(
        'nemeth.csaba@revolve.hu',
        subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked és nekem :)',
        massageText = mailContent)

    # emailSender.sendEmail('nemeth.csaba@revolve.hu,motox@freemail.hu', subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked és nekem :)', massageText = mailContent)
    #andras@pagem.hu

    #comment 10.15. bemegy-e


def make_hyperlink():




    pass


def main():

    csv_output_fileName = 'rcz_csv_out.csv'
    html_output_fileName = 'rcz_html_out.html'

    mailContent = makeCSV('http://www.rczbikeshop.com/default/sales/crazy-prices.html', csv_output_fileName, True)
    # makeTABLE(csv_output_fileName)

    # mailContent = makeCSV('http://www.rczbikeshop.com/default/sales/crazy-prices.html', html_output_fileName)
    # send(mailContent)

    makeHTML(csv_output_fileName, html_output_fileName)
    # mailContent = readHTML(html_output_fileName)

    # mailContent = makeCSV('http://www.rczbikeshop.com/default/sales/crazy-prices.html', csv_output_fileName, True)
    # mailContent = readCSV(csv_output_fileName)
    # mailContent = html_output_fileName

    # mailContent = "asdghjk"
    # send(mailContent)


if __name__ == '__main__':
    main()
