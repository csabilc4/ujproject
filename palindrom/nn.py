#!/usr/bin/env python
# coding=utf-8

import os
import time
import ftfy

# os.chdir('e:/')

currentDate = time.strftime(" %Y.%m.%d-%H:%M:%S")

print os.getcwd()

# _sourceFileName1 = '/palin.txt'
_sourceFileName1 = 'HUN_ENG_dict TARGET short.txt'

# _targetFile = open(_targetFileName1, 'w')

def addLangCode():

  try:
    _sourceFile = open(_sourceFileName1, 'r')
  except:
    print 'Nincs ilyen SOURCE fájl!'
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

lettersToDelete   = ["'", "-", " ", ".", "&", "*", "<", ">",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def searchForPalindromWords():
  leghosszabb = 0
  ujszo = ''
  i = 0
  palinNum = 0
  palinWords = []

  bDeleteFirstLetter = 0
  newLine = ''

  try:
    _file = open(_sourceFileName1, 'r')
  except:
    print 'Nincs ilyen SOURCE fájl!'
    exit()

  for _line in _file:
    invalidLine = 0

    line = repr(_line)
    # line = (_line).rstrip("\n")

    print line

    for letter in lettersToDelete:
        if letter in line:
            # print letter
            invalidLine = 1
            break

    if line.startswith('HUN') and len(line) > 6 and not invalidLine:
      bDeleteFirstLetter = 0
      for letter in lettersToDelete:
          # print line[4]
          if line[4] == letter:
              bDeleteFirstLetter = 1

      newLine = line[4:]
      # newLine = line
      # print newLine, len(newLine)

      reverseLine = ''
      # for letters in newLine:
      #   reverseLine = newLine[::-1]

      reverseLine = newLine[::-1]

      print newLine, len(newLine), reverseLine, len(reverseLine)
      # print unicode(reverseLine, "utf-8")

      if newLine.lower() == reverseLine.lower():
        # print newLine, reverseLine
        palinNum += 1
        palinWords.append(newLine)

  print 'Palindrom szavak:', ", ".join(palinWords), #, palinNum

  _file.close()

def main():
    # addLangCode()
    searchForPalindromWords()
    pass

## Testing
if __name__ == '__main__':
    # print 'test OK!'

    main()

    # try:
    #     main()
    # except:
    #     quit("Something went wrong!")

