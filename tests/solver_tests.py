import unittest

from solver import Solver
from algorithm import Task
from presolver import Sigma


class TestSolver(unittest.TestCase):
    def setUp(self):  # настройка параметров тестов, запускается перед каждым тестом
        self.test_table = []
        test_table = self.test_table
        test_table.append(Sigma([2, 3], 1, 2))
        test_table.append(Sigma([5, 5], 2, 4))
        test_table.append(Sigma([9, 7], 3, 7))
        test_table.append(Sigma([6, 8], 4, 8))
        test_table.append(Sigma([10, 10], 4, 11))
        test_table.append(Sigma([8, 12], 5, 11))
        test_table.append(Sigma([11, 11], 5, 11))
        self.test_task = Task()
        self.test_task.set_task_data(5, 11, [[2, 3, 4, 1, 2], [3, 2, 2, 3, 4], [2, 2, 3, 4, 3]])
        self.solver = Solver(test_table, self.test_task)

    def test_get_less_or_equal_record_6_8(self):
        u = [6, 8]
        ksi = 4
        eta = 8
        answer = self.solver.get_less_or_equal_record(u, ksi, eta)
        correct_answer = Sigma([6, 8], 4, 8)
        self.assertEqual(answer.u, correct_answer.u)
        self.assertEqual(answer.ksi, correct_answer.ksi)
        self.assertEqual(answer.eta, correct_answer.eta)

    def test_get_less_or_equal_record_10_10(self):
        u = [10, 10]
        ksi = 5
        eta = 12
        answer = self.solver.get_less_or_equal_record(u, ksi, eta)
        correct_answer = Sigma(u, 4, 11)
        self.assertEqual(answer.u, correct_answer.u)
        self.assertEqual(answer.ksi, correct_answer.ksi)
        self.assertEqual(answer.eta, correct_answer.eta)

    def test_set_x_ksi_to_one(self):
        for x in range(self.test_task.dimension):
            with self.subTest(x=x):
                correct_answer = []
                self.setUp()
                for i in range(self.test_task.dimension):
                    correct_answer.append(0)  # забили нулями
                correct_answer[x] = 1  # установили нужный х в единицу
                self.solver.set_x_ksi_to_one(x + 1)
                self.assertEqual(self.solver.get_solution(), correct_answer)

    def test_change_u_vector(self):
        self.solver.u = [8, 12]
        self.solver.ksi = 5
        self.solver.eta = 11
        self.solver.change_u_vector()
        self.assertEqual(self.solver.u, [6, 8])

        self.solver.change_ksi_and_eta()
        self.solver.change_u_vector()
        self.assertEqual(self.solver.u, [5, 5])

    def test_calculate(self):
        self.solver.calculate()
        self.assertEqual(self.solver.get_solution(), [1, 1, 0, 1, 1])
