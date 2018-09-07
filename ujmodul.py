#!/usr/bin/env python
# coding=utf-8

import math

# print '\n'.join(sys.modules)
# print math.cos(math.radians(60))

ff = [1, 2, 3, 1]
gg = [1, 2, 3, 1, 3, 3, 1]
# d = set(ff)
# print d

import sys

# print '\n'.join(sys.path)

# print ('ajtó\n')
# print repr('ajtó\n')
# print str(repr('ajtó\n'))

# nevek = ['Németh Csaba', 'Németh Józsefné']
# cimek = ['Szentendre', 'Mosonmagyaróvár']
# for nev in range(len(nevek)):
#     print nevek[nev].rjust(20 + nev * 0), cimek[nev].rjust(20 + nev * 0)
# print '\n',
# for nev in range(len(nevek)):
#     print '%20s %20s' % (nevek[nev], cimek[nev])




# gyumolcsok = ["3alma", "1szőlő", "2korte"]
# # zoldsegek = ["paradicsom", "uborka", "paprika", "hagyma"]
# for i, v in zip(gyumolcsok, reversed(zoldsegek)):
#     print i, "majdnem", v
#
# for s in sorted(gyumolcsok):
#     print s

zoldsegek = {"paradicsom":"jo", "uborka":"szuper", "paprika":"rossz", "hagyma":"gut"}

# for k in zoldsegek.values():
#     print k
#
# k = 1
# z = 3 + (k <> 2)
# print z

class Proba():
    ll = 3
    def __init__(self, lista = (1,2,3,4)):
        self.li = lista * self.ll
        # self.li2 = lista
        print type(self.li)

    def pp(self, li2=[5,6,7]):
        print self.li
        print li2
        li3 = 4
k = Proba()
k.pp()

k2 = Proba()
k2.pp([10,11])
# print(Proba.__dict__)
print Proba.ll



exit()
def jj():
    pass
jj.temp="affg"

print jj.__dict__

class TempClass():
    vv = 1

print TempClass.__dict__












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
