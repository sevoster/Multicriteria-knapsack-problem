import unittest
import core


class TestCoreTable(unittest.TestCase):
    def test_table(self):
        count = 5
        weight = 11
        table = []
        b = [2, 3, 4, 1, 2]
        c = [3, 2, 2, 3, 4]
        a = [2, 2, 3, 4, 3]
        for i in range(count):
            string = []
            for j in range(weight):
                string.append(-1)
            table.append(string)
        for j in range(weight):
            if a[0] <= j + 1:
                table[0][j] = [[b[0], c[0]]]
            else:
                table[0][j] = [[0, 0]]
        self.assertEqual(core.gettable(count, weight, a, b, c),
                         [[[[0, 0]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]], [[2, 3]]],
                          [[[0, 0]], -1, -1, [[5, 5]], [[5, 5]], -1, [[5, 5]], [[5, 5]], -1, -1, [[5, 5]]],
                          [-1, -1, -1, [[5, 5]], -1, -1, [[9, 7]], [[9, 7]], -1, -1, [[9, 7]]],
                          [-1, -1, -1, -1, -1, -1, -1, [[9, 7], [6, 8]], -1, -1, [[10, 10]]],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, [[11, 11], [8, 12]]]])

    def test_sum_1(self):
        self.assertEqual(core.get_sum([[5, 5]], [1, 2]), [[6, 7]])

    def test_sum_2(self):
        self.assertEqual(core.get_sum([[5, 5], [9, 0]], [1, 2]), [[6, 7], [10, 2]])
