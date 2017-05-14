import sys
from PyQt5 import QtCore

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel, QWidget)

import file_parser
import core
from TableViewer import TableViewer


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

        v_box_info = QVBoxLayout()
        v_box_info.setAlignment(QtCore.Qt.AlignHCenter)

        self.label = QLabel()
        self.label.setVisible(False)
        self.label.setStyleSheet("QLabel { background-color : white; color : blue; }")
        v_box_info.addWidget(self.label)

        self.table_view = TableViewer()
        self.table_view.setVisible(False)
        v_box_info.addWidget(self.table_view)

        v_box_buttons = QVBoxLayout()
        v_box_buttons.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        v_box_buttons.addWidget(run_button)

        h_box = QHBoxLayout()
        h_box.addLayout(v_box_info)
        h_box.addLayout(v_box_buttons)

        central_widget.setLayout(h_box)

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
        if not file_name:
            return
        self.input_data = file_parser.parse(file_name)
        if self.input_data != -1:
            self.setup_label()
            self.init_table(self.input_data[0], self.input_data[1])
            self.statusBar().showMessage('Import File: Success')
        else:
            self.input_data = []
            self.statusBar().showMessage('Import File: Error')

    @pyqtSlot()
    def on_run_click(self):
        if self.input_data:
            # Put here code to find solution
            table = core.Table(self.input_data[0], self.input_data[1], self.input_data[4], self.input_data[2],
                                 self.input_data[3]).gettable()
            self.table_view.setData(table)
            pres = core.PreSolver(table)
            self.table_view.highlightData(pres.get_table())

    # Put some beauty on it, maybe add some input from text boxes
    def setup_label(self):
        margin = "                      "
        if self.input_data:
            self.label.setVisible(True)
            text = "CONDITIONS:\n"
            for i in range(2, 5):
                text += margin
                index = 0
                while index != len(self.input_data[i]) - 1:
                    text += str(self.input_data[i][index]) + " * x" + str(index + 1) + " + "
                    index += 1
                text += str(self.input_data[i][index]) + " * x" + str(index + 1) + "\n\n"
            self.label.setText(text)

    def init_table(self, row_count, column_count):
        self.table_view.clear()
        self.table_view.setRowCount(row_count)
        self.table_view.setColumnCount(column_count)
        self.table_view.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())
