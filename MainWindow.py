import sys
from PyQt5 import QtCore

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea)

import file_parser
import core
from TableViewer import TableViewer


class MainWindow(QMainWindow):
    input_data = []
    max_row_height = 35

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar().showMessage('Ready')

        self.init_menu_bar()

        central_widget = QWidget(self)

        display_layout = self.init_display_layout()
        control_layout = self.init_control_layout()

        main_h_layout = QHBoxLayout()
        main_h_layout.addLayout(display_layout)
        main_h_layout.addLayout(control_layout)

        central_widget.setLayout(main_h_layout)

        self.setCentralWidget(central_widget)
        self.resize(600, 400)
        self.center()

        self.setWindowTitle('Main Window')
        self.reset()
        self.show()

    def init_menu_bar(self):
        import_action = QAction('&Import', self)
        import_action.setShortcut('Ctrl+I')
        import_action.setStatusTip('Import file')
        import_action.triggered.connect(self.import_file)

        close_action = QAction('&Close', self)
        close_action.setShortcut('Ctrl+W')
        close_action.setStatusTip('Close session')
        close_action.triggered.connect(self.reset)

        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(import_action)
        file_menu.addAction(close_action)
        file_menu.addAction(exit_action)

    def init_control_layout(self):
        run_button = QPushButton('Run')
        run_button.clicked.connect(self.on_run_click)

        v_box_buttons = QVBoxLayout()
        v_box_buttons.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        v_box_buttons.addWidget(run_button)

        return v_box_buttons

    def init_display_layout(self):
        text_label_font = QFont("Veranda", 12, QFont.Bold)

        container_widget = QWidget()
        container_layout = QVBoxLayout()
        container_layout.setAlignment(QtCore.Qt.AlignCenter)

        text_label_conditions = QLabel()
        text_label_conditions.setText("Conditions:")
        text_label_conditions.setFont(text_label_font)
        container_layout.addWidget(text_label_conditions, QtCore.Qt.AlignLeft)

        self.condition_label = QLabel()
        self.condition_label.setAlignment(QtCore.Qt.AlignCenter)
        self.condition_label.setStyleSheet("QLabel { padding: 20px 0px 20px 0px; background-color : white; color : "
                                           "black; }")
        self.condition_label.setFont(QFont("Veranda", 10, QFont.Decorative))
        container_layout.addWidget(self.condition_label)

        text_label_table = QLabel()
        text_label_table.setFont(text_label_font)
        text_label_table.setText("Solution Table:")
        container_layout.addWidget(text_label_table, QtCore.Qt.AlignLeft)

        self.table_view = TableViewer()
        container_layout.addWidget(self.table_view)

        container_widget.setLayout(container_layout)

        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(container_widget)

        display_layout = QVBoxLayout()
        display_layout.addWidget(scroll_area)

        return display_layout

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

    def reset(self):
        self.input_data = []
        self.init_table(0, 0)
        self.table_view.setEnabled(False)
        self.condition_label.setText("[ EMPTY ]\n\nPlease import data")

    @pyqtSlot()
    def on_run_click(self):
        if self.input_data:
            # Put here code to find solution
            table = core.Table(self.input_data[0], self.input_data[1], self.input_data[4], self.input_data[2],
                               self.input_data[3]).gettable()
            self.table_view.setData(table)
            pres = core.Presolver(table)
            self.table_view.highlightData(pres.getTable())
            self.statusBar().showMessage("Run: Success")
        else:
            self.statusBar().showMessage("Run: No input data available")

    # Put some beauty on it, maybe add some input from text boxes
    def setup_label(self):
        if self.input_data:
            text = ""
            for i in range(2, 5):
                index = 0
                while index < len(self.input_data[i]) - 1:
                    text += str(self.input_data[i][index]) + " * x_" + str(index + 1) + " + "
                    index += 1
                text += str(self.input_data[i][index]) + " * x_" + str(index + 1)
                if i == 4:
                    text += " <= " + str(self.input_data[1])
                else:
                    text += " => max\n\n"
            self.condition_label.setText(text)

    def init_table(self, row_count, column_count):
        self.table_view.clear()
        self.table_view.setRowCount(row_count)
        self.table_view.setColumnCount(column_count)
        self.table_view.setFixedHeight(row_count * self.max_row_height)
        self.table_view.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())
