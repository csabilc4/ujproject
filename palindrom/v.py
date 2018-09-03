_sourcefileName = 'e:\palin.txt'

def fileOpener():
  leghosszabb = 0
  ujszo = ''
  i = 0
  _file = open(_sourcefileName, 'r')
  for line in _file:
    words = line.split()

    szo = ''
    for _szo in words:
      hossz = len(szo)
      szo = _szo.replace('.','')
      i = 0
      ujszo = ''
      for chars in szo:
        ujszo += szo[len(szo) - 1 - i]

        i += 1

        #     if szo == ujszo and len(szo) > 1:
      #     ujszo = ujszo.encode('utf-8')
      if len(szo) > 1: print szo, ujszo

  #  print leghosszabb

fileOpener()