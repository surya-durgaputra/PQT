import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import pyqtSlot
import main_menu


class Window(QtGui.QMainWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Window"
        self.left = 200
        self.top = 100
        self.width = 400
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon('favicon-0.png'))
        self.setGeometry(self.left, self.top,
                         self.width, self.height)

        self.main_menu()

        # statusBar is shown at the bottom
        self.statusBar()

        self.show()

    def main_menu(self):
        uic.loadUi('MainMenu.ui', self)
        # implement main menu actions

        # openEditor = QtGui.QAction("&Editor", self)
        # openEditor.setShortcut("Ctrl+E")
        # openEditor.setStatusTip('Open Editor')
        # openEditor.triggered.connect(self.editor)
        # main_menu.actionOpenEditor.triggered.connect(self.editor)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+o")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+s")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        exitApp = QtGui.QAction('&Quit', self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.setStatusTip('Leave the app')
        exitApp.triggered.connect(self.close_application)

        # build the main menu here
        mainMenu = self.menuBar()
        
        # add the submenus and submenu actions
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitApp)

        # editorMenu = mainMenu.addMenu('&Editor')
        # editorMenu.addAction(openEditor)

    @pyqtSlot()
    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        # setting as CentralWidget will make the editor
        # cover the whole application area
        self.setCentralWidget(self.textEdit)

    @pyqtSlot()
    def file_open(self):
        # we will return the file that we choose in the picker as name
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        # open the file with the intention to read
        file = open(name, 'r')

        # we need to make the editor as central widget
        # otherwise there will be nowhere to load the file 
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)

    @pyqtSlot()
    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    @pyqtSlot()
    def close_application(self):
        choice = QtGui.QMessageBox.question(
                                            self, 'Quit!',
                                            'Leave Application?',
                                            QtGui.QMessageBox.Yes
                                            | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.No  # default
                                           )
        if choice == QtGui.QMessageBox.Yes:
            print('Quitting!')
            sys.exit()
        else:
            pass


def main():
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
