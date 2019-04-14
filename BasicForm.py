"""
first program
https://www.pythonforthelab.com/blog/step-by-step-guide-to-building-a-gui/
"""

import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("My Window")
        self.setWindowIcon(QtGui.QIcon('favicon-0.png'))
        # implement main menu actions
        extractAction = QtGui.QAction("&Get to the choppah!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+o")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        saveFile = QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+s")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        # statusBar is shown at the bottom
        self.statusBar()

        # build the main menu here
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(openEditor)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        # btn.resize(100, 100)
        btn.move(0, 100)

        # ADD A TOOLBAR
        # toolbars are more specofic to the item like home
        # add the toolbar here
        extractAction = QtGui.QAction(
                                        QtGui.QIcon('todachoppa.png'),
                                        'Flee the scene', self
                                     )
        extractAction.triggered.connect(self.close_application)

        # create the actual toolbar
        self.toolbar = self.addToolBar("Extraction")
        self.toolbar.addAction(extractAction)

        # ADD A FONT CHOICE TO THE TOOLBAR  
        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)

        # create the actual toolbar
        # self.toolbar = self.addToolBar("Font")
        self.toolbar.addAction(fontChoice)

        # ADD A FONT COLOR WIDGET
        color = QtGui.QColor(0, 0, 0)
        # note: we can change the font colot itself
        # but background color is more visible for demo
        fontColor = QtGui.QAction('Font bg Color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolbar.addAction(fontColor)

        # ADD A CHECKBOX
        checkbox = QtGui.QCheckBox('Enlarge Window', self)
        # if you want it default checked, checkbox.toggle()
        # but note that the window size will only change when
        # a statechage is detected. Since this does not happen
        # with a checkbox default checked, you wont see a 
        # large window. In that case, keep the default checked
        # state at large window and then when unchecked,
        # statechanged will get triggered and in the callback
        # function, shrink the window
        checkbox.stateChanged.connect(self.enlarge_window)
        checkbox.move(270, 30)

        # ADD A PROGRESS BAR
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        # ADD A DROPDOWN MENU
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Plastique", self)
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        # ADD A CALENDAR WIDGET
        cal = QtGui.QCalendarWidget(self)
        cal.move(400, 200)
        cal.resize(500, 200)

        self.show()

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

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def color_picker(self):
        # get the color picker and return the chosen color
        color = QtGui.QColorDialog.getColor()
        # stylesheet is going to let you customize things
        # within the application
        self.styleChoice.setStyleSheet(
            "QWidget { background-color: %s }" % color.name()
            )

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        # setting as CentralWidget will make the editor 
        # cover the whole application area
        self.setCentralWidget(self.textEdit)

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        # we will set the font on the name of the Style label
        if valid:
            self.styleChoice.setFont(font)

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def download(self):
        # establish a starting point
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QtGui.QMessageBox.question(
                                            self, 'Extract!',
                                            'Get into the chopper?',
                                            QtGui.QMessageBox.Yes
                                            | QtGui.QMessageBox.No
                                           )
        if choice == QtGui.QMessageBox.Yes:
            print('Extracting Nowwwww!!!!')
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
