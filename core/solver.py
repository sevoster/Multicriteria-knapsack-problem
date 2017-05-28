class Solver:
    """Class that presents algorithm to find the solution"""

    def __init__(self, table, task):
        self.task = task  # инициализация параметров задачи
        self.table = table  # инициализация сигма-таблицы
        self.solution = []  # решение
        for x in range(task.dimension):
            self.solution.append(0)
        self.ksi = task.dimension
        self.eta = task.knapsack_capacity
        for x in self.table:
            if x.ksi == task.dimension and x.eta == task.knapsack_capacity:
                self.u = x.u
                break
        pass

    def find_u_vector(self):
        for x in self.table:
            if x.u == self.u and x.ksi <= self.ksi and x.eta <= self.eta:
                self.u = x.u
                self.ksi = x.ksi
                self.eta = x.eta
                break
        pass

    def get_less_or_equal_record(self, vector, ksi,
                                 eta):  # возвращает запись из таблицы, у которой ksi<=ksi', eta<=eta'
        for x in self.table:  # проходим по всем записям в таблице
            if (x.u == vector) and (x.ksi <= ksi) and (x.eta <= eta):
                return x  # если кси и эта меньше или равны(они последние в записи в таблице)

    def set_x_ksi_to_one(self, ksi):
        self.solution[ksi - 1] = 1
        pass

    def change_u_vector(self):
        self.u = [self.u[0] - self.task.first_criterion_coefficients[self.ksi - 1], self.u[1]
                  - self.task.second_criterion_coefficients[self.ksi - 1]]
        pass

    def change_ksi_and_eta(self):
        self.eta = self.eta - self.task.limitation_coefficients[self.ksi - 1]
        self.ksi = self.ksi - 1
        pass

    def calculate(self):
        while self.u != [0, 0]:
            self.set_x_ksi_to_one(self.ksi)
            self.change_u_vector()
            if self.u != [0, 0]:
                self.change_ksi_and_eta()
                self.find_u_vector()

    def get_solution(self):
        return self.solution
