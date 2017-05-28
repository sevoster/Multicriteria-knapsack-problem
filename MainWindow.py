import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel, QWidget, QScrollArea, QMessageBox)

sys.path.insert(0, 'core')
sys.path.insert(0, 'file_parser')

from TableViewer import TableViewer
from core import *
from solver import Solver
from file_parser import *


class MainWindow(QMainWindow):
    max_row_height = 35

    def __init__(self):
        super().__init__()
        self.parser = TaskDataParser()
        self.task = Task()

        self.text_label_conditions = QLabel()
        self.text_label_table = QLabel()
        self.text_label_solution = QLabel()

        self.condition_label = QLabel()
        self.table_view = TableViewer()
        self.solution_label = QLabel()

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
        self.reset_ui()
        self.show()

    def init_menu_bar(self):
        import_action = QAction('&Import', self)
        import_action.setShortcut('Ctrl+I')
        import_action.setStatusTip('Import file')
        import_action.triggered.connect(self.import_file)

        close_action = QAction('&Close', self)
        close_action.setShortcut('Ctrl+W')
        close_action.setStatusTip('Close current session')
        close_action.triggered.connect(self.on_close_click)

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
        condition_label_font = QFont("Veranda", 10, QFont.Decorative)
        solution_label_font = QFont("Veranda", 16, QFont.Bold)
        text_label_style_sheet = "QLabel { padding: 20px 0px 10px 0px; }"
        condition_label_style_sheet = "QLabel { padding: 20px 10px 20px 10px; background-color : white; color : " \
                                      "black; } "
        solution_label_style_sheet = "QLabel { padding: 20px 10px 30px 10px; background-color: white;}"

        container_widget = QWidget()
        container_layout = QVBoxLayout()

        self.text_label_conditions.setText("Conditions:")
        self.text_label_conditions.setFont(text_label_font)
        self.text_label_conditions.setStyleSheet(text_label_style_sheet)
        container_layout.addWidget(self.text_label_conditions, QtCore.Qt.AlignLeft)

        self.condition_label.setAlignment(QtCore.Qt.AlignCenter)
        self.condition_label.setStyleSheet(condition_label_style_sheet)
        self.condition_label.setFont(condition_label_font)
        container_layout.addWidget(self.condition_label, QtCore.Qt.AlignJustify)

        self.text_label_table.setFont(text_label_font)
        self.text_label_table.setStyleSheet(text_label_style_sheet)
        self.text_label_table.setText("Solution Table:")
        container_layout.addWidget(self.text_label_table, QtCore.Qt.AlignLeft)

        container_layout.addWidget(self.table_view, QtCore.Qt.AlignJustify)

        self.text_label_solution.setFont(text_label_font)
        self.text_label_solution.setStyleSheet(text_label_style_sheet)
        self.text_label_solution.setText("Solution:")
        container_layout.addWidget(self.text_label_solution, QtCore.Qt.AlignLeft)

        self.solution_label.setFont(solution_label_font)
        self.solution_label.setStyleSheet(solution_label_style_sheet)
        self.solution_label.setAlignment(QtCore.Qt.AlignCenter)
        container_layout.addWidget(self.solution_label, QtCore.Qt.AlignCenter)

        container_widget.setLayout(container_layout)

        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
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

    def reset_ui(self):
        self.text_label_solution.setVisible(False)
        self.text_label_table.setVisible(False)
        self.condition_label.setText("[ EMPTY ]\n\nPlease import data")
        self.table_view.setVisible(False)
        self.solution_label.setVisible(False)

    def show_solution(self, solution_data):
        if not solution_data.is_valid():
            return

        self.table_view.setData(solution_data.table)
        self.table_view.highlightData(solution_data.sigma_table)
        self.text_label_table.setVisible(True)
        self.table_view.setVisible(True)
        self.text_label_solution.setVisible(True)
        self.solution_label.setText("X = {0}".format(str(solution_data.solution_vector)))
        self.solution_label.setVisible(True)

    def import_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Text files (*.txt)")[0]
        if not file_name:
            return

        try:
            self.parser.parse(file_name)
        except ParserError as error:
            self.show_error_message("Parser Error", str(error))
            return

        self.task = self.parser.get_task_instance()

        if not self.task.is_valid():
            self.statusBar().showMessage('Import File: Error')
            return

        self.reset_ui()
        self.setup_label()
        self.init_table()
        self.statusBar().showMessage('Import File: Success')

    def on_run_click(self):
        if not self.task.is_valid():
            self.statusBar().showMessage("Run: No input data available")
            return

        solution_data = self.find_solution()

        self.show_solution(solution_data)
        self.statusBar().showMessage("Run: Success")

    def find_solution(self):
        table = Table(self.task).gettable()
        sigma_table = PreSolver(table).get_table()
        solver = Solver(sigma_table, self.task)
        solver.calculate()
        solution = solver.get_solution()
        solution_data = SolutionData()
        solution_data.set_solution_data(table, sigma_table, solution)
        return solution_data

    def on_close_click(self):
        self.task = Task()
        self.reset_ui()

    def init_table(self):
        self.table_view.clear()
        self.table_view.setRowCount(self.task.dimension)
        self.table_view.setColumnCount(self.task.knapsack_capacity)
        self.table_view.setFixedHeight(self.task.dimension * self.max_row_height)

    def setup_label(self):
        if not self.task.is_valid():
            pass

        text = "{0} => max\n\n".format(self.coefficient_list_to_str(self.task.first_criterion_coefficients))
        text += "{0} => max\n\n".format(self.coefficient_list_to_str(self.task.second_criterion_coefficients))
        text += "{0} <= {1}".format(self.coefficient_list_to_str(self.task.limitation_coefficients),
                                    str(self.task.knapsack_capacity))

        self.condition_label.setText(text)

    @staticmethod
    def coefficient_list_to_str(coefficient_list):
        text = ""
        length = len(coefficient_list)
        for index in range(0, length):
            text += "{0} * x_{1}{2}".format(str(coefficient_list[index]), str(index + 1),
                                            (" + " if index != length - 1 else ""))

        return text

    @staticmethod
    def show_error_message(title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()

    sys.exit(app.exec_())
