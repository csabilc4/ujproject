#!/usr/bin/env python
# coding=utf-8

attri = "proba_modul attributum vagyok!"

def kiir():
    print "proba_modul függvény vagyok!"

class Ujclass:
    def kiir(self):
        print "proba_modul classmethod vagyok!"

    def __init__(self):
        self.attri = "proba_modul class attributum vagyok!"