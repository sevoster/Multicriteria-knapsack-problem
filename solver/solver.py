from core import Sigma


class Task:
    """Class that presents task parameters. 
    n - count of variables 
    b - coefficient of limitation
    q1, q2 - criteries
    limitation - limitation of task"""

    def __init__(self, n, b, q1, q2, limitation):  # инициализация задачи
        self.n = n
        self.b = b
        self.q1 = q1
        self.q2 = q2
        self.limitation = limitation

    # куча геттеров для получения параметров задачи:
    def get_n(self):
        return self.n

    def get_b(self):
        return self.b

    def get_q1(self):
        return self.q1

    def get_q2(self):
        return self.q2

    def get_limitation(self):
        return self.limitation


class Solver:
    """Class that presents algorithm to find the solution"""

    def __init__(self, table, task):
        self.task = task  # инициализация параметров задачи
        self.table = table  # инициализация сигма-таблицы
        self.solution = []  # решение
        for x in range(task.n):
            self.solution.append(0)
        self.u = [0, 0]
        self.ksi = 0
        self.eta = 0
        pass

    # TODO: Изменить множество G(сигма), сделать не словарём, а таблицей с одинаковой структурой <(u1,u2),ksi,eta>
    def get_less_or_equal_record(self, vector, ksi,
                                 eta):  # возвращает запись из таблицы, у которой ksi<=ksi', eta<=eta'
        for x in self.table:  # проходим по всем записям в таблице
            if (x.get_u() == vector) and (x.get_ksi() <= ksi) and (x.get_eta() <= eta):
                return x  # если кси и эта меньше или равны(они последние в записи в таблице)

    def set_x_ksi_to_one(self, ksi):
        self.solution[ksi] = 1
        pass

    def change_u_vector(self):
        self.u = [self.u[0] - self.task.q1[self.ksi], self.u[1] - self.task.q2[self.ksi]]
        pass

    def is_u_zero(self):
        if self.u == 0:
            return 1

    def print_dict(self, table):
        for x in dict:  # проходим по всем записям в таблице
            print(x)

    def calculate(self):
        # self.u = self.get_from_dict(self.task.n, self.task.limitation)
        # for x in range(n):
        #     self.solution.append(0)  # забиваем решение изначально нулями
        return self.solution

    def get_solution(self):
        return self.solution
