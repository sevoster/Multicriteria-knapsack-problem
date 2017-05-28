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
        try:
            file = open(path, 'r')
        except FileNotFoundError:
            raise ParserError("File not found")

        self.coefficient_lists.clear()
        try:
            self.dimension = int(file.readline())
            self.knapsack_capacity = int(file.readline())
            for line in file:
                self.coefficient_lists.append(list(map(int, line.split(' '))))
        except ValueError:
            raise ParserError("File has wrong format: Cannot parse input data.\nNote: Be sure that file "
                                    "contains one empty line in the end.")

    def get_task_instance(self):
        task = Task()
        task.set_task_data(self.dimension, self.knapsack_capacity, self.coefficient_lists)
        return task

class ParserError(Exception):
    pass
