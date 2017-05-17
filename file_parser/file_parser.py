from PyQt5.QtWidgets import QMessageBox


def parse(path):
    msg = QMessageBox()
    msg.setWindowTitle("Parse Error")

    try:
        file = open(path, 'r')
    except FileNotFoundError:
        msg.setText("File not found")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return -1

    try:
        dimension = int(file.readline())
        knapsack_capacity = int(file.readline())
        condition_coefficients = []
        for line in file:
            condition_coefficients.append(list(map(int, line.split(' '))))
    except ValueError:
        msg.setText("File has wrong format: Cannot parse input data.\nNote: Be sure that file contains one empty line "
                    "in the end.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return -1

    # Validate input data
    if len(condition_coefficients) != 3:
        msg.setText("There should be three lines with coefficients in file.\nNote: Be sure that file contains one "
                    "empty line in the end.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return -1
    return dimension, knapsack_capacity, condition_coefficients[0], condition_coefficients[1], condition_coefficients[2]
