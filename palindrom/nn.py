#!/usr/bin/env python
# coding=utf-8

_sourceFileName1 = 'e:\palin.txt'
_sourceFileName1 = 'e:\HUN_ENG_dict.txt'
_targetFileName1 = 'e:\HUN_ENG_dict TARGET2.txt'

def addLangCode():
  _targetFile = open(_targetFileName1, 'w')

  try:
    _sourceFile = open(_sourceFileName1, 'r')
  except:
    print 'Nincs ilyen fájl!'
    exit()

  blankLine = 1

  for line in _sourceFile:
    words = line.split()

    if len(line) > 1:
      if blankLine == True:
        newLine = 'HUN:' + line
      else:
        newLine = 'ENG:' + line
      blankLine = 0
    else:
      newLine = '--------------' + '\n'
      blankLine = 1
    # print newLine
    _targetFile.write(newLine)

  _sourceFile.close()
  _targetFile.close()

def searchForPalindromWords():
  leghosszabb = 0
  ujszo = ''
  i = 0
  palinNum = 0

  _targetFileName1 = 'e:\palin_dict.txt'

  try:
    _file = open(_targetFileName1, 'r')
  except:
    print 'Nincs ilyen fájl!'
    exit()

  for line in _file:
    if line.startswith('HUN'):
      hunWord1 = line.replace('HUN:','')
      hunWord2 = hunWord1.replace(' ','')
      hunWord3 = hunWord2.replace('-','')
      # print hunWord3

      i = 0
      ujszo = ''
      for chars in hunWord3:
        # ujszo += hunWord3[len(hunWord3) - 1 - i]
        ujszo = hunWord3[::-1]
        i += 1

        # if hunWord3 == ujszo and len(hunWord3) > 1:
      print hunWord3, hunWord3[1], len(ujszo)
          # palinNum += 1

    # szo = ''
    # for _szo in words:
    #   hossz = len(szo)
    #   szo = _szo.replace('.','')
    #   i = 0
    #   ujszo = ''
    #   for chars in szo:
    #     ujszo += szo[len(szo) - 1 - i]
    #     i += 1
    #
    #     #     if szo == ujszo and len(szo) > 1:
    #   #     ujszo = ujszo.encode('utf-8')
    #   if szo == ujszo and len(szo) > 1:
    #     print szo, ujszo
    #     palinNum += 1
  print 'Palindrom szavak száma: ', palinNum
  #  print leghosszabb

  _file.close()

# addLangCode()
searchForPalindromWords()