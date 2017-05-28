from table import Table
from presolver import PreSolver
from solver import Solver

class Task:
    """Class that presents task parameters.
    dimension - размерность задачи (количество предметов)
    knapsack_capacity - вместимость рюкзака
    first_criterion_coefficients - список коэффициентов первого критерия
    second_criterion_coefficients - список коэффициентов второго критерия
    limitation_coefficients - список коэффициентов ограничения
    """

    def __init__(self):
        self.dimension = 0
        self.knapsack_capacity = 0
        self.first_criterion_coefficients = []
        self.second_criterion_coefficients = []
        self.limitation_coefficients = []

    def set_task_data(self, task_dimension, knapsack_capacity, condition_coefficients):
        # инициализация задачи
        if self.validate_data(task_dimension, knapsack_capacity, condition_coefficients):
            self.dimension = task_dimension
            self.knapsack_capacity = knapsack_capacity
            self.first_criterion_coefficients = condition_coefficients[0]
            self.second_criterion_coefficients = condition_coefficients[1]
            self.limitation_coefficients = condition_coefficients[2]

    def is_valid(self):
        return self.validate_data(self.dimension, self.knapsack_capacity,
                                  [self.first_criterion_coefficients, self.second_criterion_coefficients,
                                   self.limitation_coefficients])

    @staticmethod
    def validate_data(dimension, knapsack_capacity, condition_coefficients):
        # проверка входных данных на корректность
        if dimension <= 0 or knapsack_capacity <= 0 or len(condition_coefficients) != 3:
            return False

        for coefficient_list in condition_coefficients:
            if len(coefficient_list) != dimension:
                return False

            for coefficient in coefficient_list:
                if coefficient < 0:
                    return False

        return True

class SolutionData:
    """
    Class contains solution data for a task
    table - таблица значений критериев
    sigma_table - выбранные ячейки из таблицы
    solution_vector - найденная стратегия Х
    """

    def __init__(self):
        self.table = None
        self.sigma_table = None
        self.solution_vector = None

    def set_solution_data(self, table, sigma_table, solution_vector):
        self.table = table
        self.sigma_table = sigma_table
        self.solution_vector = solution_vector

    def is_valid(self):
        if self.table is None or self.sigma_table is None or self.solution_vector is None:
            return False
        return True

class Algorithm:
    """
    Class represents algorithm to find solution for bicriteria knapsack problem
    """
    def __init__(self):
        self.task = Task()
        self.solution = SolutionData()

    def run(self):
        if not self.task.is_valid():
            return

        table = Table(self.task).gettable()
        sigma_table = PreSolver(table).get_table()
        solver = Solver(sigma_table, self.task)
        solver.calculate()
        solution = solver.get_solution()
        self.solution.set_solution_data(table, sigma_table, solution)

    def is_solution_ready(self):
        return self.solution.is_valid()

    def is_task_correct(self):
        return self.task.is_valid()