import unittest
import core
from solver import Solver
from solver import Task
from core import Sigma


class TestCoreTable(unittest.TestCase):
    def setUp(self):  # настройка параметров тестов, запускается перед каждым тестом
        self.test_table = []
        test_table = self.test_table
        test_table.append(Sigma([2, 3], 1, 2))
        test_table.append(Sigma([5, 5], 2, 4))
        test_table.append(Sigma([9, 7], 3, 7))
        test_table.append(Sigma([6, 8], 4, 8))
        test_table.append(Sigma([10, 10], 4, 11))
        test_table.append(Sigma([11, 11], 5, 11))
        test_table.append(Sigma([8, 12], 5, 11))
        self.test_task = Task(5, 11, [2, 3, 4, 1, 2], [3, 2, 2, 3, 4], [2, 2, 3, 4, 3])
        self.solver = Solver(test_table, self.test_task)

    def test_get_less_or_equal_record(self):
        u = [6, 8]
        ksi = 4
        eta = 8
        answer = self.solver.get_less_or_equal_record(u, ksi, eta)
        correct_answer = Sigma([6, 8], 4, 8)
        self.assertEqual(answer.get_u(), correct_answer.get_u())
        self.assertEqual(answer.get_ksi(), correct_answer.get_ksi())
        self.assertEqual(answer.get_eta(), correct_answer.get_eta())
        u = [10, 10]
        ksi = 5
        eta = 12
        answer = self.solver.get_less_or_equal_record(u, ksi, eta)
        correct_answer = Sigma(u, 4, 11)
        self.assertEqual(answer.get_u(), correct_answer.get_u())
        self.assertEqual(answer.get_ksi(), correct_answer.get_ksi())
        self.assertEqual(answer.get_eta(), correct_answer.get_eta())

    def test_set_x_ksi_to_one(self):
        for x in range(self.test_task.get_n()):
            with self.subTest(x=x):
                correct_answer = []
                self.setUp()
                for i in range(self.test_task.get_n()):
                    correct_answer.append(0)  # забили нулями
                correct_answer[x] = 1  # установили нужный х в единицу
                self.solver.set_x_ksi_to_one(x)
                self.assertEqual(self.solver.get_solution(), correct_answer)



            # def test_solver(self):
            #     self.assertEqual(self.solver.get_solution(), [1, 1, 0, 1, 1])
