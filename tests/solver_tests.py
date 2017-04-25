import unittest
import core
from solver import Solver
from solver import Task
from core import Sigma


class TestCoreTable(unittest.TestCase):
    test_table = []
    test_table.append(Sigma([2, 3], 1, 2))
    test_table.append(Sigma([5, 5], 2, 4))
    test_table.append(Sigma([9, 7], 3, 7))
    test_table.append(Sigma([6, 8], 4, 8))
    test_table.append(Sigma([10, 10], 4, 11))
    test_table.append(Sigma([11, 11], 5, 11))
    test_table.append(Sigma([8, 12], 5, 11))

    test_task = Task(5, 11, [2, 3, 4, 1, 2], [3, 2, 2, 3, 4], [2, 2, 3, 4, 3])
    solver = Solver(test_table, test_task)

    def test_solver(self):
        self.assertEqual(self.solver.get_solution(), [1, 1, 0, 1, 1])
        pass

    def test_get_less_or_equal_record(self):
        u = [6, 8]
        ksi = 4
        eta = 8
        self.assertEqual(self.solver.get_less_or_equal_record(u, ksi, eta), [[6, 8], 5, 9]) # выяснить, нахрена нужна нумерация + 1
