class Solver:
    """Class that presents algorithm to find the solution"""

    def __init__(self, dict, table, n, b):
        self.ksi = n
        self.eta = b
        self.dict = dict  # инициализация таблицы(множества сигма)
        self.table = table  # инициализация таблицы параметров задачи
        self.solution = []  # решение
        self.u = self.get_from_dict(n, b)
        for x in range(n):
            self.solution.append(0)  # забиваем решение изначально нулями
        pass

    # TODO: Изменить множество G(сигма), сделать не словарём, а таблицей с одинаковой структурой <(u1,u2),ksi,eta>
    def get_less_or_equal_from_dic(self, vector, ksi, eta):
        for x in self.dict:  # проходим по всем записям в таблице
            if x[-2] <= ksi and x[-1] <= eta:  # если кси и эта меньше или равны(они последние в записи в таблице)
                self.ksi = x[-1]
                self.eta = x[-2]
                return x[0]  # вернуть первый вектор из этой записи

    def get_from_dict(self, ksi, eta):
        for x in self.dict:  # проходим по всем записям в таблице
            if x[-2] == ksi and x[-1] == eta:  # если кси и эта совпадают(они последние в записи в таблице)
                return x[0]  # вернуть первый вектор из этой записи

    def set_xksi_to_one(self, ksi):
        self.solution[ksi] = 1
        pass

    def change_u_vector(self):
        x = self.u
        x[0] = x[0] - self.table[0].c[self.ksi]
        x[1] = x[1] - self.table[1].c[self.eta]

    def is_u_zero(self):
        if self.u == 0:
            return 1

    def print_dict(self, dict):
        for x in dict:  # проходим по всем записям в таблице
            print(x)

    def algorithm(self):
        return self.solution

#TODO: сделаю из этого тест
# def client_code():
#     solver = Solver([[[2, 1], [2, 1], 2, 2], [[3, 1], [2, 1], 2, 2]])
#     print(solver.get_from_dict(2, 2))
#
#
# client_code()
