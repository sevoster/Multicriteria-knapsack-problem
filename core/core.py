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


class Table:
    """"Table Creation"""

    def __init__(self, task):
        self.table = []
        self.count = task.n
        self.weight = task.b
        self.weights = task.limitation
        self.costs1 = task.q1
        self.costs2 = task.q2

    def gettable(self):
        for i in range(self.count):
            string = []
            for j in range(self.weight):
                string.append(-1)
            self.table.append(string)
        for j in range(self.weight):
            if self.weights[0] <= j + 1:
                self.table[0][j] = [[self.costs1[0], self.costs2[0]]]
            else:
                self.table[0][j] = [[0, 0]]
        self.rec_fill_table(self.count - 1, self.weight - 1)
        return self.table

    @staticmethod
    def get_sum(first, sec):
        res = []
        for vectors in first:
            tic_res = []
            for el in range(2):
                tic_res.append(vectors[el] + sec[el])
            res.append(tic_res)
        return res

    @staticmethod
    def do_filter(variety):
        result = []
        for vectors in variety:
            not_bad = True
            for vector2 in variety:
                if (vectors[0] <= vector2[0] and vectors[1] < vector2[1]) or \
                        (vectors[0] < vector2[0] and vectors[1] <= vector2[1]):
                    not_bad = False
            if not_bad:
                if vectors not in result:
                    result.append(vectors)
        return result

    def rec_fill_table(self, count, weight):
        if self.table[count][weight] != -1:
            return self.table[count][weight]
        else:
            first = self.rec_fill_table(count - 1, weight)
            if weight - self.weights[count] >= 0:
                sec = self.get_sum(self.rec_fill_table(count - 1, weight - self.weights[count]), [self.costs1[count],
                                                                                                  self.costs2[count]])
            else:
                sec = [[0, 0]]
            self.table[count][weight] = self.do_filter(first + sec)
        return self.table[count][weight]


class Sigma:
    """Structure that presents record of sigma table"""

    def __init__(self, u, ksi, eta):
        self.u = u
        self.ksi = ksi + 1
        self.eta = eta + 1

    def is_not_empty(self):
        return self.u[0] != 0 or self.u[1] != 0


class PreSolver:
    """Class that makes sigma-table"""
    def __init__(self, table_of_p):
        self.table_sigma = []
        for i in range(len(table_of_p)):
            for j in range(len(table_of_p[i])):
                if table_of_p[i][j] != -1:
                    for k in range(len(table_of_p[i][j])):
                        new_sigma = Sigma(table_of_p[i][j][k], i, j)
                        self.add_rows(new_sigma)

    def add_rows(self, sigma):
        if sigma.is_not_empty():
            flag = 1
            for s in self.table_sigma:
                if s.u == sigma.u:
                    flag = 0
            if flag:
                self.table_sigma.append(sigma)

    def get_table(self):
        return self.table_sigma
