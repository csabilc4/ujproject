#!/usr/bin/env python
# coding=utf-8

print "ez itt a pycharmban készült, majd feltöltöm github-baaa"
print "na ez egy diff"

# TODO ez itt egy

# todo ez is egy tudu!!


from os import listdir
from os import walk

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

    # f.append(filenames)

print 'Leghosszabb filenév hossza: \033[1;37;30m %d \033[0;31;30m karakter, a file neve: "%s"' % (maxFilename, maxFile)

# print type(maxFile)

