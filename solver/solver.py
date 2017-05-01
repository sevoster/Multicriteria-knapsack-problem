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
        self.ksi = task.n
        self.eta = task.b
        for x in self.table:
            if x.get_ksi()==task.n and x.get_eta()==task.b:
                self.u = x.get_u()
                break
        pass

    def find_u_vector(self):
        for x in self.table:
            if x.get_u()==self.u and x.get_ksi()<=self.ksi and x.get_eta()<=self.eta:
                self.u = x.get_u()
                break
        pass

    def get_less_or_equal_record(self, vector, ksi, eta):  # возвращает запись из таблицы, у которой ksi<=ksi', eta<=eta'
        for x in self.table:  # проходим по всем записям в таблице
            if (x.get_u() == vector) and (x.get_ksi() <= ksi) and (x.get_eta() <= eta):
                return x  # если кси и эта меньше или равны(они последние в записи в таблице)

    def set_x_ksi_to_one(self, ksi):
        self.solution[ksi-1] = 1
        pass

    def change_u_vector(self):
        self.u = [self.u[0] - self.task.q1[self.ksi-1], self.u[1] - self.task.q2[self.ksi-1]]
        pass

    def change_ksi_and_eta(self):
        self.ksi=self.ksi-1
        self.eta=self.eta - self.task.get_limitation()[self.ksi-1]
        pass

    def calculate(self):
        while self.u != [0,0]:
            self.set_x_ksi_to_one(self.ksi)
            self.change_u_vector()
            if self.u!=[0,0]:
                self.change_ksi_and_eta()
                self.find_u_vector()

    def get_solution(self):
        return self.solution
