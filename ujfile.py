#!/usr/bin/env python
# coding=utf-8

# print "ez itt a pycharmban készült, majd feltöltöm github-baaa"
# print "na ez egy diff"

import math
import prettytable
import urllib
import random
import time
import collections

# TODO ez itt egy
# todo ez is egy tudu!!
# fixme ezis TODO
# FIXME ez is todo


class Point:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return math.hypot(self.x, self.y)

class Circle(Point):

	def __init__(self, radius, x = 0, y = 0):
		super.__init__(x, y)
		self.radius = radius

	def edge_distance_from_origin(self):
		return abs(self.distance_from_origin() - self.radius)

p = Circle(2)

print p.edge_distance_from_origin()

exit()


cache = {}

Circle = collections.namedtuple("Circle", "x y radius")
circle = Circle(13, 84, 9)
# print circle

class Val:
	nn = 200

	def __init__(self, x = 0, y = 0, ss = "valamistring00"):
		self.x = x
		self.y = y
		self.ss = ss
		self.name = __name__

		print 'HELLO, te incializálva vagy!'

	x = 20

	# print self.x

	def pp(self, x, y):
		print x*y

	nn = 400

	def __str__(self):
		return "ez a Val class, a példány neve: " + self.name

	def __eq__(self, other):
		return self.x == other.x, self.y == other.y

	def __cmp__(self, other):
		return cmp(self.x, other.x)

	def __add__(self, other):
		return self.x + other.x + self.y + other.y

	def __neg__(self):
		return self.y

	def __len__(self):
		return len(self.ss)**3

	def __repr__(self):
		return str(self.x) + " repro"

xx = Val(0, 2, "ez")
yy = Val(1, -2)
zz = Val(3, 10)

print xx
print "'xx nagyobb mint yy?:'", xx > yy
print xx + zz
print "neg yy", -yy
print len(zz)
print '----------------------------'
print hasattr(xx, 'nn')
print repr(xx)
print xx.__str__()

print isinstance(nn, Val)


# xx.pp()
# print xx
# print xx.nn

# print str(xx)
# print repr(xx)


# cc = ["alma", "körte", "meggy"]
# KETTO = 2
# print cc[KETTO + 0]




exit()


class Parent:
	def pr(self):
		print "szülő vagyok"


class Child(Parent):
	def pr(self):
		print "gyerek vagyok"


dd = Child()
dd.pr()

exit()


def ppp(self, x, y):
	print x*y

class M:
	d = ppp
	# d(xx, 2, 3)

xx = M()
xx.d(3, 4)

exit()


class Akarmi:

	def __init__(self):
		self.param = 'CCCCCCCCSSSSS'


	faa = 35

	def prr(self):
		print self.param


	def pr(self):
		print self.faa, 'adsd'


class Akar(Akarmi):

	faa = 45
	print faa

xx = Akarmi()
ff = xx
# xx.faa = 20
ff.pr
xx.pr()

xx.prr()

print
ww = Akar()
ww.pr()


def vv():
	print type(vv)
	pass

vv()

exit()

movies = [('a', 1987),
		  ('b', 1526),
		  ('c', 2019),
		  ('d', 1907),
		  ('e', 2437),
		  ('f', 1944),
		  ('g', 2037)]

gmovies = [(title, year) for (title, year) in movies if year < 2000]
dmovies = {title.upper(): year for (title, year) in movies if year < 2500 and title == 'e'}

# gmovies = []
# for (title, year) in movies:
#     if year < 2000:
#         gmovies.append((title, year))
print gmovies, type(gmovies)
print dmovies, type(dmovies)

# v = [2, -3, 1]
# mod_v = [vect*4 for vect in v]
# print mod_v
# print len(v)



exit()

class qw:

	aaa = 40

	def __init__(self):
		# self.aaa = 15
		pass

	def asd(self):
		self._asd = 10

	def yxc(self, aaa):
		# self.aaa = 333

		print self.aaa, aaa
		# print self._asd


ss = qw()
# ss.aaa = 20
ss.yxc('10')

exit()

def camelcase(s):


	dd = 01
	cap = [word.capitalize() for word in s.split('_') if dd > 0]
	capList = ''.join(cap)

	return type(cap), type(capList)\


before = time.time()
print (camelcase('some_string_you_nike_sdgdfghD_HDhrtghR_Rthrth_ERthrthrhr_\
ERThjrthr_RTHrthrtH_RTHrthrtH_RThrth-rTHrthrt_weterte'))
after = time.time()
dur = after - before

print '{:04.3f}'.format(before)
print '{:04.3f}'.format(after)

exit()


def random_c():

	return random.choice(range(1, 91))


def lotto():
	szamok = []
	for szam in range(5):
		sz = random_c()
		if cache.has_key(sz):
			cache[sz] += 1
		else:
			cache[sz] = 1
		szamok.append(str(sz))

	# return 'A heti nyerőszámok: ' + ', '.join(szamok)
	return ', '.join(szamok)


huz = 455
i=0
while i < huz:
	lotto()
	i += 1

szum = 0
for a, b in cache.items():
	print "A(z) " + str(a) + "-s szám valószínűsége %s húzásból %5.2f" % (huz, b/455.0*1000/5) + "%"
	szum += b

print szum

if szum > 400:
	# raise NameError, 'túl nagy a megadott szám!'
	pass

print "%010.6f" % (10/3.0)

exit()





TRAP_ARTISTS = [
	'Jay Z',
	'Dr. Dre',
	'Easy E'
]

class TrapArtist:

	def __init__(self, name, age):
		self._name = name
		self._age = age

	# @property
	def name(self):
		return self._name

	# @property
	def age(self):
		return self._age

	@staticmethod
	def naame():
		return 'ez egy staticmethod'


# rr = TrapArtist('Jabba', 21)
# print rr.name()
# print rr.age()

# print TrapArtist.naame()

exit()


class Valami:

	def printt(self):
		print "ez valamiclass"


dd = Valami()
dd.printt()

exit()


def mapper(fnc):
	def inner():
		pass

	return inner


# @mapper
def random_c():
	return random.choice(range(1, 91))


def lotto():
	szamok = []
	for szam in range(5):
		szamok.append(str(random_c()))

	return 'A heti nyerőszámok: ' + ', '.join(szamok)


print lotto()

exit()


def another_function():
	"""
	decorator
	:rtype: object
	"""
	print "Another functionsdfsfgdflkj"


def turn_into_another_function(fff):
	"""

	:param f:
	:return:
	"""
	return another_function()


@turn_into_another_function
def a_function():
	print "A function"


# a_function = turn_into_another_function(a_function)


print a_function.__doc__

exit()

list1 = ["   parrradicsom ", "            uborka      ", " paprika", "hagyma      "]

# kk = [gy.strip() for gy in list1]

kk = []
for gy in list1:
	kk.append(gy.strip())

print kk

exit()

movies = [('a', 1987),
		  ('b', 1526),
		  ('c', 2019),
		  ('d', 1907),
		  ('e', 2437),
		  ('f', 1944),
		  ('g', 2037)]

# gmovies = [(title, year) for (title, year) in movies if year < 2000]
gmovies = []
for (title, year) in movies:
	if year < 2000:
		gmovies.append((title, year))
print gmovies

v = [2, -3, 1]
# mod_v = [vect*4 for vect in v]
# print mod_v
print len(v)

exit()


def random_walk(n):
	x = 0
	y = 0
	for i in range(n):
		step = random.choice(['N', 'S', 'E', 'W'])
		if step == 'N':
			y += 1
		elif step == 'S':
			y -= 1
		elif step == 'E':
			x += 1
		else:
			x -= 1
	return (x, y)


for i in range(25):
	walk = random_walk(10)
	print "Próba", i, ":", walk, "Távolság: ", abs(walk[0]) + abs(walk[1])

exit()

resp = urllib.urlopen("https://www.wikipedia.org/")
print type(resp)
print resp.code
data = resp.read()
print len(data)

exit()

full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
print full_name(' nEMEtH', ' csABA')

ddd = "   dfsdfjh sdfkh sdf  sdfsdf    "
eee = "   dfsdfjh sdfkh sdf  sdfsdf    ".strip()
# print ddd
# print eee

list1 = ["parrradicsom", "uborka", "paprika", "hagyma"]
list1.sort()
print list1


def nev():
	return 5 + 10


def build(a, b, c):
	# return lambda x: a+b+c+x
	return c, b, a, nev()


print build(1, 2, 3)

exit()

list1 = ["parrradicsom", "uborka", "paprika", "hagyma"]
list2 = ["100", "200", "300", "400"]

table = prettytable.PrettyTable(['Zöldségek', 'Árak'])
for x in range(0, 4):
	table.add_row([list1[x], list2[x]])

print table

zoldsegek = ["parrradicsom", "uborka", "paprika", "hagyma"]

loud = [z.upper() for z in zoldsegek]

print loud

exit()


def lone_sum(a, b, c):
	list = [a, b, c]

	sum = 0
	lastN = 0

	for n in list:
		if n != lastN:
			sum += n
			print lastN, sum
		lastN = n
		# print n, lastN

	# return sum


print lone_sum(3, 2, 3)

exit()


def make_bricks(small, big, goal):
	smallB = 1
	bigB = 5

	biggest = small * smallB + big * bigB

	sum = 0
	for bi in range(big + 1):
		for sm in range(small + 1):
			sum = sm * smallB + bi * bigB
			# print bi, sm, sum
			if sum == goal:
				return True

	return False


print make_bricks(40, 1, 45)

exit()

print str(math.pi)[0:4]

exit()

zoldsegek = ["parrradicsom", "uborka", "paprika", "hagyma"]

for it, zz in enumerate(zoldsegek):
	print it, 'típusa:', type(it), zz, 'típusa:', type(zz)

exit()

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

	f.append(filenames)

# print 'Leghosszabb filenév hossza: \033[1;31m %d \033[0;30m karakter, a file neve: "%s"' % (maxFilename, maxFile)


# import emailSender
# emailSender.sendEmail('nemeth.csaba@revolve.hu', massageText = 'Ez a szöveg_____éáűőúöüóí', subjectText = 'Ez lesz a cím...éáűőúöüóí')

import emailSenderWithClass

send = emailSenderWithClass.EmailSender()
send.sendEmail(
	'nemeth.csaba@revolve.hu')  # , subjectText = 'Ez lesz a cím...CLASS', massageText = 'Ez a szöveg...CLASS')

exit()

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
	smtpObj.login(sender, password)
	smtpObj.sendmail(sender, receiver, massage.as_string())
	smtpObj.sendmail(sender, massage["To"].split(",") + massage["Cc"].split(","), massage.as_string())
	smtpObj.quit()

	print "E-mail sikeresen elkuldve!"

rrr = False
if rrr == True:
	r = requests.get('http://www.rczbikeshop.com/default/sales/crazy-prices.html')

	soup = BeautifulSoup(r.text, 'html.parser')
	results = soup.find_all('span', attrs = {'class': 'price'})
	print len(results)
	# print " ".join(results)
	# print ''.join(str(results))
	# print type(str((results[1])))
	print str((results[1]))

# dic = {'a':1, 'b':2}
# print dic.has_key('c')
# print dic.get('c')
# print "hali éáűőúöüóí............."


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
a = 22
print c.plusOne()
