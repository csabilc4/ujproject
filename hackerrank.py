#!/usr/bin/env python
# coding=utf-8


df = [1, 2, 3, 4]
a, b, c, d = df
print a, b, c, d



exit()

def minion_game(ss):
    # your code goes here

    vowels = 'AEIOU'
    print s
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"


    vows = {}
    cons = {}
    vNum = 0
    cNum = 0
    string = s
    for st in range(len(string)):
        for m in range(len(string)-st):
            string_mod = string[st:]
            if m > 0:
                ff = string_mod[0:-m]
            else:
                ff = string_mod[0:]

            if ff.startswith('A')\
                    or ff.startswith('E')\
                    or ff.startswith('I')\
                    or ff.startswith('O')\
                    or ff.startswith('U'):

                if ff in vows:
                    vows[ff] += 1
                else:
                    vows[ff] = 1
                vNum += 1
            else:
                if ff in cons:
                    cons[ff] += 1
                else:
                    cons[ff] = 1
                cNum += 1

    if cNum > vNum:
        print 'Stuart', str(cNum)
    elif cNum == vNum:
        print 'Draw'
    else:
        print 'Kevin', str(vNum)


if __name__ == '__main__':
    # s = raw_input()

    s = "BANANNNNUBOIUBTJHFBRRRRGGGGGGGSDTREAVPOUIBŐPOOIŐOBUZZTTREVREÁŰÉÚŐÚŐÚÉSAEWQREVUZTZUIBZNNNNNNAA"
    minion_game("s")