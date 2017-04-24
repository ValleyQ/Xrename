#coding:utf-8
from __future__ import division
import sys
import re
import os
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "open_files.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon(r'\Iw.png'))
        self.setupUi(self)
        self.open_files.clicked.connect(self.Open_Files)

    def Open_Files(self):
        filePath = os.environ['HOMEPATH']
        fileNames = QtGui.QFileDialog.getOpenFileNames(self,"select files",filePath)
        j = []
        for i in fileNames:
            files = os.path.basename(str(i))
            print files
            j.append(files)
        print j
        '''
        for i in fileNames:
            print i
            j = re.findall(r'[^\\]+$',i)
            print j
        '''
        k = QtGui.QStringListModel(j)
        self.files_list.setModel(k)
        self.files_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)    #可以多选
        self.files_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)    #让结果不能编辑
        return fileNames

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())