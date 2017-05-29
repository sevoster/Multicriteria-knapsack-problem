from unittest import TestCase

from table import Table
from algorithm import Task


class TestCoreTable(TestCase):
    def test_table_big(self):
        count = 5
        weight = 11
        b = [2, 3, 4, 1, 2]
        c = [3, 2, 2, 3, 4]
        a = [2, 2, 3, 4, 3]
        task = Task()
        task.set_task_data(count, weight, [b, c, a])
        test_table = Table(task)
        self.assertEqual(test_table.create_table(),
                         [[[[0, 0]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]],
                           [[2, 3]], [[2, 3]]],
                          [[[0, 0]], -1, -1, [[5, 5]], [[5, 5]], -1, [[5, 5]], [[5, 5]], -1, -1, [[5, 5]]],
                          [-1, -1, -1, [[5, 5]], -1, -1, [[9, 7]], [[9, 7]], -1, -1, [[9, 7]]],
                          [-1, -1, -1, -1, -1, -1, -1, [[9, 7], [6, 8]], -1, -1, [[10, 10]]],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, [[11, 11], [8, 12]]]])

    def test_table_normal(self):
        count = 3
        weight = 5
        b = [2, 3, 4]
        c = [3, 2, 2]
        a = [2, 2, 3]
        task = Task()
        task.set_task_data(count, weight, [b, c, a])
        test_table = Table(task)
        self.assertEqual(test_table.create_table(), [[[[0, 0]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]]],
                                                     [-1, [[2, 3]], -1, -1, [[5, 5]]],
                                                     [-1, -1, -1, -1, [[6, 5]]]])

    def test_sum_1_by_1(self):
        task = Task()
        task.set_task_data(5, 5, [[], [], []])
        test_table = Table(task)
        self.assertEqual(test_table.vector_sum([[5, 5]], [1, 2]), [[6, 7]])

    def test_sum_2_by_1(self):
        task = Task()
        task.set_task_data(5, 5, [[], [], []])
        test_table = Table(task)
        self.assertEqual(test_table.vector_sum([[5, 5], [9, 0]], [1, 2]), [[6, 7], [10, 2]])
