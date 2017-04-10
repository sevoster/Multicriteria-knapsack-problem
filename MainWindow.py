import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog

import file_parser
import core


class MainWindow(QMainWindow):
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
        # table = core.gettable(input_data[0], input_data[1], input_data[2][2], input_data[2][0], input_data[2][1])
        self.statusBar().showMessage('Import File: Success')
        print(input_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())
