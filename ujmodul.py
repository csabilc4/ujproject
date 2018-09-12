#!/usr/bin/env python
# coding=utf-8

########################################################
# inp_name=raw_input("What is your name?: ")
# inp_age=raw_input("How old are you?: ")
# print type(inp_age)
# print inp_name, "you will be 100 years old in", str(int(2018 - int(inp_age)) + 100)
########################################################

########################################################
# import string
# nevek = ['Németh Csaba', 'Németh Józsefné']
# letter=["ö","ü","ó","ő","ú","é","á","ű","í",
#         "Ö","Ü","Ó","Ő","Ú","É","Á","Ű","Í"]
# letterTo=["o","u","o","o","u","e","a","u","i",
#         "O","U","O","O","U","E","A","U","I"]
# letter="öüóőúéáűíÖÜÓŐÚÉÁŰÍ"
# letterTo="ouooueauiOUOOUEAUI"
# print len(letter), len(letterTo)
# table=string.maketrans(letter,letterTo)
# exit()
########################################################

########################################################
import math
# print '\n'.join(sys.modules)
# print math.cos(math.radians(60))
########################################################

########################################################
# ff = [1, 2, 3, 1]
# gg = [1, 2, 3, 1, 3, 3, 1]
# d = set(ff)
# print d
########################################################

########################################################
# import sys
# print '\n'.join(sys.path)
########################################################

########################################################
# print ('ajtó\n')
# print repr('ajtó\n')
# print str(repr('ajtó\n'))
########################################################

########################################################
# nevek = ['Németh Csaba', 'Németh Józsefné']
# cimek = ['Szentendre', 'Mosonmagyaróvár']
# for nev in range(len(nevek)):
#     print nevek[nev].rjust(20 + nev * 0), cimek[nev].rjust(20 + nev * 0)
# print '\n',
# for nev in range(len(nevek)):
#     print '%20s %20s' % (nevek[nev], cimek[nev])
########################################################

########################################################
# gyumolcsok = ["3alma", "1szőlő", "2korte"]
# # zoldsegek = ["paradicsom", "uborka", "paprika", "hagyma"]
# for i, v in zip(gyumolcsok, reversed(zoldsegek)):
#     print i, "majdnem", v
#
# for s in sorted(gyumolcsok):
#     print s
########################################################

########################################################
# zoldsegek = {"paradicsom":"jo", "uborka":"szuper", "paprika":"rossz", "hagyma":"gut"}
# for k in zoldsegek.values():
#     print k
#
# k = 1
# z = 3 + (k <> 2)
# print z
########################################################

########################################################
# import Tkinter
# # print "\n".join(dir(Tkinter))
# gomb=Tkinter.Button()
########################################################

########################################################
# class Name:
#     def __init__(self, first, middle, last):
#         self.first=first
#         self.middle=middle
#         self.last=last
#
#     def __str__(self):
#         return self.first+' '+self.middle+' '+self.last
#
# aName=Name("Csabi", "Nagy", "Nemeth")
# print aName
# exit()
########################################################

########################################################
# class Student:
#     grades=[]
#     def __init__(self, name, id):
#         self.name=name
#         self.id=id
#
#     def addGrade(self, grade):
#         self.grades.append(grade)
#
#     def showGrades(self):
#         grds=''
#         for grade in self.grades:
#             grds+= str(grade)+' '
#         return grds
#
# stu1=Student("John", '123')
# stu1.addGrade(88)
# stu1.addGrade(90)
# stu1.addGrade(92)
# print stu1.showGrades()
# exit()
########################################################



exit()







lll=2
class Proba():
    ll = 2*lll
    def __init__(self, lista = (1,2,3,4)):
        self.ll = 3 * lll
        self.li = lista * self.ll
        # self.li2 = lista
        # print type(self.li)
        print "self.ll =", self.ll

    def pp(self, li2=[5,6,7]):
        print self.li
        print li2
        li3 = 4
        # print getattr(Proba.pp, "li2")

class Proba2(Proba):
    print "qwertzui"
    def __init__(self):
        self.li="asdfgh"
        print type(self.li), self.li

    # print type(self.li), self.li
k = Proba(2)
k.pp()
print Proba.ll


# k2=Proba2()
# k2 = Proba()
# k2.pp([10,11])



exit()

import random
zoldsegek = ["paradicsom", "uborka", "paprika", "hagyma"]
print random.choice(zoldsegek)
print random.sample(zoldsegek, 2)


exit()
temp=11
def jj(qwe):
    print qwe

    def jjj(asd):
        print asd

    jjj(30)
jj(20)
# print "jj.temp", jj.temp

class TempClass():
    vv = 1

# print TempClass.__dict__







exit()

gyumolcsok = ["alma", "korte"]
penztarcaban = 22


def kiir():
    print gyumolcsok


def kosar_kiirasa():
    print gyumolcsok
    gyumolcsok.append('barack')
    # del(gyumolcsok[2])
    print gyumolcsok

    print penztarcaban, id(penztarcaban)

    # penztarcaban = 33
    print penztarcaban, id(penztarcaban)


kosar_kiirasa()

print penztarcaban, id(penztarcaban)
print gyumolcsok
