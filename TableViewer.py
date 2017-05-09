from PyQt5 import QtCore

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class TableViewer(QTableWidget):
    def __init__(self, *args):
        QTableWidget.__init__(self, *args)

    def setData(self, table_data):
        row_index = 0
        column_index = 0
        for row in table_data:
            for column in row:
                item = QTableWidgetItem(str(column))
                item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
                self.setItem(row_index, column_index, item)
                column_index += 1
            column_index = 0
            row_index += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def highlightData(self, cells_to_highlight):
        for item in cells_to_highlight:
            row = item[1] - 1
            column = item[2] - 1
            self.item(row, column).setBackground(QtCore.Qt.green)