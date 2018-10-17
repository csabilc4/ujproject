# -*- coding: utf-8 -*-


from __future__ import print_function
import openpyxl
from openpyxl import load_workbook
import xlrd
import xlwt
import os
from PIL import Image
from PySide import QtCore, QtGui
import sys
import re
import StringIO
from xlutils.copy import copy
import shutil

class ImageInserterView(QtGui.QWidget):

    def __init__(self,qtMainWindow,imageInsertModel,xlsProcess,parent = None):
        super(ImageInserterView,self).__init__()
        self.xlsProcess = xlsProcess
        self.imageInsertModel = imageInsertModel
        self.setupUi(qtMainWindow)


    def setupUi(self,qtMainWindow):
        self.centralwidget = QtGui.QWidget(qtMainWindow)
        qtMainWindow.setObjectName("qtMainWindow")
        qtMainWindow.resize(360, 240)
        qtMainWindow.setCentralWidget(self.centralwidget)
        self.setGridLayout()

    def setGridLayout(self):
        self.upperGridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.upperGridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 120))

        self.lowerGridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.lowerGridLayoutWidget.setGeometry(QtCore.QRect(10, 120, 341, 120))

        self.imagesInFolder = ("Válassz Xlsx fájlt").decode('utf8')
        successfulImages = "22"
        self.upperGridLayout =      QtGui.QGridLayout(self.upperGridLayoutWidget)
        self.getWorkspaceButton =   QtGui.QPushButton(("Add meg az Excel fájl helyét:").decode('utf8'),self.upperGridLayoutWidget)
        self.getWorkspaceButton.clicked.connect(self.fileBrowse)
        self.upperGridLayout.addWidget(self.getWorkspaceButton, 1, 1, 1, 2,QtCore.Qt.AlignTop)
        self.imageNum =             QtGui.QLabel(('Képek száma').decode('utf8'), self.upperGridLayoutWidget)
        self.upperGridLayout.addWidget(self.imageNum, 2,1,1,1)
        self.succesFulImageNums =   QtGui.QLabel(('Sikeresen beszúrt képek száma:').decode('utf8'))
        self.upperGridLayout.addWidget(self.succesFulImageNums, 3,1,1,1)
        self.varImageNum =          QtGui.QLabel(self.imagesInFolder, self.upperGridLayoutWidget)
        self.upperGridLayout.addWidget(self.varImageNum, 2,2,1,1,QtCore.Qt.AlignRight)
        self.varSuccessFulImageNums = QtGui.QLabel(successfulImages,self.upperGridLayoutWidget)
        self.upperGridLayout.addWidget(self.varSuccessFulImageNums, 3,2,1,1,QtCore.Qt.AlignRight)
        self.frame =                QtGui.QFrame()
        self.frame.setFrameShape(QtGui.QFrame.HLine)
        self.upperGridLayout.addWidget(self.frame, 4,1,1,2,QtCore.Qt.AlignBottom)


        self.lowerGridLayout = QtGui.QGridLayout(self.lowerGridLayoutWidget)
        self.startButton = QtGui.QPushButton("Ok", self.lowerGridLayoutWidget)
        self.startButton.clicked.connect(self.xlsProcess.insertImage)
        self.lowerGridLayout.setColumnMinimumWidth(1, 90)
        self.lowerGridLayout.setColumnMinimumWidth(2, 90)
        self.lowerGridLayout.setRowMinimumHeight(1, 60)
        self.lowerGridLayout.addWidget(self.startButton, 2, 3, 1, 1, QtCore.Qt.AlignBottom)
        self.cancelButton = QtGui.QPushButton("Cancel", self.lowerGridLayoutWidget)
        self.cancelButton.clicked.connect(self.imageInsertModel.closeEvent)
        self.lowerGridLayout.addWidget(self.cancelButton, 2, 4, 1, 1, QtCore.Qt.AlignBottom)



    def fileBrowse(self):
        file = QtGui.QFileDialog.getOpenFileName(self,"Single File",os.getcwd(), ("Excel Files (*.xls)"))
        self.filePath, ext = file
        self.varImageNum.setText(str(len(self.xlsProcess.processImageFolder(self.filePath))))
        return self.filePath

    def printer(self):
        # print "Dude","Dudett"
        pass

class ImageInserterModel():

    def __init__(self, parent=None):
        pass

    def startImageInserting(self,test):
        # print test
        pass

    def closeEvent(self):
        # self.destroy()
        pass

class XlsEdit():

    def __init__(self, parent=None):
        #xlsPath = "E:\\Mano_arts\\WS\\sideHobbyTools\\CsabiExcelTool\\Book1.xlsx"
        pass

    def processImageFolder(self,xlsPath):
        self.xlsPath = xlsPath
        folderPath = os.path.join(os.path.split(self.xlsPath)[0],("Fotók").decode('utf8'))
        #folderPath = ("E:\\Mano_arts\\WS\\sideHobbyTools\\CsabiExcelTool\\Képek").decode('utf8')
        self.images = os.listdir(folderPath)
        self.imagePaths =[os.path.join(folderPath,image) for image in self.images]
        self.modifyImg()
        return self.imagePaths
        #self.insertImage(xlsPath,imagePaths)

    def resizeImage(self,img):
#        if img.size[0] >= img.size[1]:
#         baseheight = 264
#         hpercent = (baseheight / float(img.size[1]))
#         wsize = int(((img.size[0])*float(hpercent)))
#         img = img.resize((wsize,baseheight), Image.ANTIALIAS)
#         img = img.resize((1, 1), Image.ANTIALIAS)
#         return img
#        else:
#            basewidth = 352
#            wpercent = (basewidth / float(img.size[0]))
#            hsize = int((float(img.size[1]) * float(wpercent)))
#            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
#            return img
         return img

    def modifyImg(self):
        self.tempFolderPath = os.path.join(os.path.split(self.xlsPath)[0].replace('/','\\'),"Temp")
        if not os.path.exists(self.tempFolderPath):
            os.makedirs(self.tempFolderPath)
        for index,image in enumerate(self.imagePaths):
            img = Image.open(image)
            f = os.path.join(self.tempFolderPath,os.path.split(image)[1])
            a,b = os.path.splitext(f)
            img2 = self.resizeImage(img)
            img2.save("%s.bmp"%((a+str(index))))
        tempFolder = os.listdir(self.tempFolderPath)
        self.tempImagePaths = [os.path.join(self.tempFolderPath,t_image) for t_image in tempFolder]

    def insertImage(self):
        workbook = xlrd.open_workbook(self.xlsPath,formatting_info=True)
        wsName = ("Képek, mellékletek").decode('utf8')

        i = 0
        t = 4
        if wsName in workbook.sheet_names():
            r_worksheet = workbook.sheet_by_name(wsName)
            w_workbook = copy(workbook)
            worksheet =  w_workbook.get_sheet(0)
            while i < len(self.imagePaths):
                img1 = self.tempImagePaths[i]
                img2 = self.tempImagePaths[i+1]

#                if img1.size[0] >= img1.size[1]:
#                    xOffset1 = 352 / 2 - 198 / 2
#                else:
#                    xOffset1 = 0
#                if img2.size[0] >= img2.size[1]:
#                    xOffset2 = 352 / 2 - 198 / 2
#                else:
#                    xOffset2 = 0

                scale = 0.25
                xOffset1 = 0
                xOffset2 = 0

#                fnt = xlwt.Font()
#                fnt.height = 256 * 4
#                style = xlwt.XFStyle()
#                style.font = fnt
#                worksheet.row(t-1-1).set_style(style)

                worksheet.insert_bitmap(img1, t - 1 - 1, 1 - 1, xOffset1, 0, scale, scale)
                worksheet.insert_bitmap(img2, t - 1 - 1, 12 - 1, xOffset2, 0, scale, scale)
                t += 14
                i += 2
                if i % 3 == 0:
                    t += 2
                if r_worksheet.row_values(t) == ("Mellékletek").decode('utf8'):
                    t+= 29

            w_workbook.save(self.xlsPath)

        #if  os.path.exists(self.tempFolderPath):
        #    shutil.rmtree(self.tempFolderPath)

        else:
            # print "Az XLS-ben nincs " + wsName+" tablap."
            pass
 

def main():
    app = QtGui.QApplication(sys.argv)
    qtMainWindow = QtGui.QMainWindow()
    imageInsertModel = ImageInserterModel()
    xlsProcess = XlsEdit()
    ui = ImageInserterView(qtMainWindow,imageInsertModel,xlsProcess)
    qtMainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()