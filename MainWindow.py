import sys
from PyQt5 import QtCore

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog, QPushButton,
                             QGridLayout, QHBoxLayout, QVBoxLayout, QWidget)

import file_parser
import core
import presolver

class MainWindow(QMainWindow):
    input_data = []

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage('Ready')

        import_action = QAction('&Import', self)
        import_action.setShortcut('Ctrl+I')
        import_action.setStatusTip('Import file')
        import_action.triggered.connect(self.import_file)

        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(import_action)
        file_menu.addAction(exit_action)

        central_widget = QWidget(self)

        run_button = QPushButton('Run')
        run_button.clicked.connect(self.on_run_click)

        v_box_buttons = QVBoxLayout()
        v_box_buttons.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        v_box_buttons.addWidget(run_button)

        central_widget.setLayout(v_box_buttons)

        self.setCentralWidget(central_widget)
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
        self.input_data = file_parser.parse(file_name)
        if self.input_data != -1:
            self.statusBar().showMessage('Import File: Success')
        else:
            self.input_data = []
            self.statusBar().showMessage('Import File: Error')

    @pyqtSlot()
    def on_run_click(self):
        if self.input_data:
            # Put here code to find solution
            print(self.input_data)
            core.gettable()
            Presolver


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())
