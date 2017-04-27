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
        global filePath
        filePath = os.environ['HOMEPATH']
        self.setWindowIcon(QtGui.QIcon(r'\Iw.png'))
        self.setupUi(self)
        self.open_files.clicked.connect(self.Open_Files)
        self.add_files.clicked.connect(self.Add_Files)
        self.delete_files.clicked.connect(self.Delete_Files)

    def Open_Files(self):
        fileNames = QtGui.QFileDialog.getOpenFileNames(self,"select files",filePath)
        global j,l,k
        j,l = [],[]
        for i in fileNames:
            l.append(str(i))
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
        self.files_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.files_list.customContextMenuRequested.connect(self.onRightClick)

    def Add_Files(self):
        fileNames = QtGui.QFileDialog.getOpenFileNames(self, "select files", filePath)
        j1,a ,c= [],[],[]
        global j,l,k
        print l,45
        for i in fileNames:
            print i
            a.append(str(i))
        c = list(set(a).difference(set(l)))
        for d in c:
            files = os.path.basename(str(d))
            print files
            j1.append(files)
        print j1,11
        j = j + j1
        k = QtGui.QStringListModel(j)
        self.files_list.setModel(k)


    def Delete_Files(self):
        self.deleteItem()


    def onRightClick(self, pos):
        menu = QtGui.QMenu(self)
        delete = QtGui.QAction('Delete', self, triggered=self.deleteItem)
        menu.addAction(delete)
        menu.exec_(self.files_list.mapToGlobal(pos))

    def deleteItem(self):
        index = self.files_list.currentIndex()
        print 'Delete: %s' % index.data().toString()
        k.removeRow(index.row())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())