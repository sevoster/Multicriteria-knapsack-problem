from PyQt5.QtWidgets import QMessageBox
from core import Task

class TaskDataParser:
    """
    Class provides methods to parse txt file and create task data instance if data is correct
    Expected txt format:
        <Dimension of task>
        <Knapsack capacity>
        <Criterion coefficients>
        <Criterion coefficients>
        <Limitation coefficients>
        <Empty line>
    """

    def __init__(self):
        self.coefficient_lists = []
        self.dimension = 0
        self.knapsack_capacity = 0

    def parse(self, path):
        msg = QMessageBox()
        msg.setWindowTitle("Parse Error")
        msg.setIcon(QMessageBox.Critical)

        try:
            file = open(path, 'r')
        except FileNotFoundError:
            msg.setText("File not found")
            msg.exec_()
            return -1

        self.coefficient_lists.clear()
        try:
            self.dimension = int(file.readline())
            self.knapsack_capacity = int(file.readline())
            for line in file:
                self.coefficient_lists.append(list(map(int, line.split(' '))))
        except ValueError:
            msg.setText("File has wrong format: Cannot parse input data.\nNote: Be sure that file contains one empty line "
                        "in the end.")
            msg.exec_()
            return -1

    def get_task_instance(self):
        task = Task()
        task.set_task_data(self.dimension, self.knapsack_capacity, self.coefficient_lists)
        return task

