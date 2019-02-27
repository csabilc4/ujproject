#!/usr/bin/env python
# coding=utf-8

# class, methods, decorators

import sys




class MainClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 1000
        self.string = "valami"

    def kiir(self, string="valam"):
        return self.string

    def kiirXY(self):
        return self.x, self.y, self.zz

    @property
    def kiirProp(self):
        return self.string

    @staticmethod
    def kiirCStatic():
        return "static vagyok"



class SubClass(MainClass):
    def __init__(self, x, y, zz):
        super(SubClass, self).__init__(x, y)
        self.zz = zz

    def kiirD(self):
        print "D függvény vagyok", "x = %d," %self.x, "y = %d," %self.y, "z = %d" %self.z


class Sub2Class(MainClass):
    def __init__(self, x, y, kk=""):
        super(SubClass, self).__init__(x, y)
        if kk is None:
            self.kk = ""
        else:
            self.kk = kk

    # def

d = SubClass(5, 60, "Valami")
print d.kiirXY()

c = MainClass(4, 40)


def pri(p):
    return p * 2

cset = set([MainClass(1, 2).kiir(), MainClass(1, 2).kiir("semmi")])
# print cset

diset = {1:"ss", 2:"aaa", 3:"aaa"}
priset = set({1:"ss", 2:"aaa", 2:"aaa"})

for h, i in diset.items():
    print h, i



print
# print "kiir", d.kiir()
# print "type kiir", type(d.kiir)

# print
# print "kiirProp", d.kiirProp
# print "type kiirProp", type(d.kiirProp)
#
# print
# print "kiirCStatic", (d.kiirCStatic())
# print "type(d.kiirCStatic)", type(d.kiirCStatic)

print
# d.kiirD()


exit()



print len(sys.argv)
print type(sys.argv[1])

for ar in sys.argv:
    print ar

exit()

class MyClass(object):

    classAttr = 'This is a class attribute!'

    def __init__(self):
        self.initAttr = 'This is an instance attribute!'


    def method(self):
        return 'Instance method called', MyClass.classAttr, self.classAttr


    def akarmi(self):
        # print "akármi is ez"

        print type(self.__privateMethod())

    @classmethod
    def classmethod(cls, classAtt):
        cls.clsAttr = classAtt
        return 'Class method called', cls, cls.clsAttr


    @staticmethod
    def staticmethod():
        return 'Static method called'


    @property
    def property(self):
        return 'This is a property attribute!'


    __classAttr = 20
    def adder(self):
        return __classAttr

    # private method
    def __privateMethod(self):
        return 11


newObj = MyClass()

# print newObj.initAttr, type(newObj.initAttr)
# newObj.classAttr = "Jepp"
# print newObj.method(), type(newObj.method)
# print newObj.classmethod("Class Attribute"), type(newObj.classmethod)
# print newObj.staticmethod(), type(newObj.staticmethod)
# print newObj.property, type(newObj.property)
# print newObj.classAttr, type(newObj.classAttr)
# print newObj.adder, type(newObj.adder)

# print newObj._meth()
newObj.akarmi()

# print
# print dir(newObj)
# print
# print vars(newObj)
# print
# print locals()





