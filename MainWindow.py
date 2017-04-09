import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog
import core.core as core

import file_parser


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        importAction = QAction('&Import', self)
        importAction.setShortcut('Ctrl+I')
        importAction.setStatusTip('Import file')
        importAction.triggered.connect(self.import_file)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(importAction)
        fileMenu.addAction(exitAction)

        self.resize(600, 400)
        self.center()

        self.setWindowTitle('Main Window')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def import_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Text files (*.txt)")[0]
        input_data = file_parser.parse(file_name)
        self.statusBar().showMessage('Import File: Success')
        print(input_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())