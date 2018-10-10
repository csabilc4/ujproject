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


def siteParser(url='http://www.rczbikeshop.com', csv_filename='rcz_csv.csv'):
    csv_file = open(csv_filename, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Link', 'Price'])

    getSite = requests.get(url)

    soup = BeautifulSoup(getSite.text, 'html.parser')
    # soup = BeautifulSoup(getSite.text, 'lxml')
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
        # print title, type(title)

        # Product link
        try:
            link = item.find('a', class_='product-image')['href']
            link = '<a href=' + link + '></a>'
            # link = link
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
            price = "OUT OF STOCK"  # csak a termék saját weblapján jelenik meg az out of stock, itt nem, ezért sosem lesz out of stock
        price = price.strip()
        # print price.strip()#, type(price)

        csv_writer.writerow([title, link, '0.00'])

        mailText += '--------------------------------------------------------------------\n'
        mailText += title + '\n'
        mailText += link + '\n'
        mailText += image + '\n'
        mailText += price + '\n'
        mailText += '--------------------------------------------------------------------\n\n'

    # print mailText
    return mailText

    csv_file.close()


def makeTable(csvFileName):
    csv_file = open(csvFileName, 'r')

    print prettytable.from_csv(csv_file)


def makeHTML(csvFileName, htmlFileName):
    csv_file = open(csvFileName, 'r')

    line = csv_file.readline()
    lineList = line.split(",")
    table = prettytable.PrettyTable(lineList)

    table.format = True


    while 1:
        line = csv_file.readline()
        if line == '':
            break
        lineList = line.split(",")
        table.align["Link"] = "l"  # Left align city names
        table.add_row(lineList)

    # htmlTable = table.get_html_string(attributes={"name":"my_table", "class":"red_table"})
    htmlTable = table.get_html_string(padding_width = 2)

    html_file = open(htmlFileName, 'w')
    html_file = html_file.write(htmlTable)

    # html_file.close()

def send(mailT):
    # send=emailSenderWithClass.EmailSender()
    # send.sendEmail('nemeth.csaba@revolve.hu', subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked :)', massageText = 'asdfgh')

    emailSender.sendEmail('nemeth.csaba@revolve.hu,motox@freemail.hu', subjectText = '*****CURRENT RCZ CRAZY PRICES***** csak neked és nekem :)', massageText = mailT)
    #andras@pagem.hu

def main():

    csv_output_fileName = 'rcz_csv_2.csv'
    html_output_fileName = 'rcz_csv_2_html.html'

    mailT = siteParser('http://www.rczbikeshop.com/default/sales/crazy-prices.html', csv_output_fileName)
    # send(mailT)

    # makeTable(csv_output_fileName)
    makeHTML(csv_output_fileName, html_output_fileName)
    pass

if __name__ == '__main__':
    main()
