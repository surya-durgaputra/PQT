# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(478, 226)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEditor = QtGui.QMenu(self.menubar)
        self.menuEditor.setObjectName(_fromUtf8("menuEditor"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenFile = QtGui.QAction(MainWindow)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionSaveFile = QtGui.QAction(MainWindow)
        self.actionSaveFile.setObjectName(_fromUtf8("actionSaveFile"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionOpenEditor = QtGui.QAction(MainWindow)
        self.actionOpenEditor.setObjectName(_fromUtf8("actionOpenEditor"))
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionSaveFile)
        self.menuFile.addAction(self.actionQuit)
        self.menuEditor.addAction(self.actionOpenEditor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEditor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEditor.setTitle(_translate("MainWindow", "Editor", None))
        self.actionOpenFile.setText(_translate("MainWindow", "Open File", None))
        self.actionOpenFile.setStatusTip(_translate("MainWindow", "Open File", None))
        self.actionOpenFile.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSaveFile.setText(_translate("MainWindow", "Save File", None))
        self.actionSaveFile.setStatusTip(_translate("MainWindow", "Save File", None))
        self.actionSaveFile.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Close Application", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionOpenEditor.setText(_translate("MainWindow", "Open Editor", None))
        self.actionOpenEditor.setStatusTip(_translate("MainWindow", "Open Editor", None))
        self.actionOpenEditor.setShortcut(_translate("MainWindow", "Ctrl+E", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

