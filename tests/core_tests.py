import unittest
import core


class TestCoreTable(unittest.TestCase):
    def test_table_big(self):
        count = 5
        weight = 11
        b = [2, 3, 4, 1, 2]
        c = [3, 2, 2, 3, 4]
        a = [2, 2, 3, 4, 3]
        task = core.Task(count, weight, b, c, a)
        test_table = core.Table(task)
        self.assertEqual(test_table.gettable(),
                         [[[[0, 0]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]]],
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
        task = core.Task(count, weight, b, c, a)
        test_table = core.Table(task)
        self.assertEqual(test_table.gettable(), [[[[0, 0]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]]],
                                                 [-1, [[2, 3]], -1, -1, [[5, 5]]],
                                                 [-1, -1, -1, -1, [[6, 5]]]])

    def test_sum_1(self):
        task = core.Task(5, 5, [], [], [])
        test_table = core.Table(task)
        self.assertEqual(test_table.get_sum([[5, 5]], [1, 2]), [[6, 7]])

    def test_sum_2(self):
        task = core.Task(5, 5, [], [], [])
        test_table = core.Table(task)
        self.assertEqual(test_table.get_sum([[5, 5], [9, 0]], [1, 2]), [[6, 7], [10, 2]])
