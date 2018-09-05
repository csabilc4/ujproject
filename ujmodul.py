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






dd = 'ave'
print len(dd)








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
