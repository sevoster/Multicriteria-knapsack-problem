class Table:
    """"Table Creation"""
    def __init__(self, count, weight, weights, costs1, costs2):
        self.table = []
        self.count = count
        self.weight = weight
        self.weights = weights
        self.costs1 = costs1
        self.costs2 = costs2

    def gettable(self):
        for i in range(self.count):
            string = []
            for j in range(self.weight):
                string.append(-1)
            self.table.append(string)
        for j in range(self.weight):
            if self.weights[0] <= j+1:
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
                if (vectors[0] <= vector2[0] and vectors[1] < vector2[1]) or (vectors[0] < vector2[0] and vectors[1] <= vector2[1]):
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
            sec = []
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

    def get_u(self):
        return self.u

    def get_ksi(self):
        return self.ksi

    def get_eta(self):
        return self.eta

    def is_not_empty(self):
        return self.u[0] != 0 or self.u[1] != 0
# class Table:
#     def __init__(self):
#         self.t = [];
#     def find(u):
#         for x in self.t:
#             if x.
#     def add_sigma(self, sigma):
#         if sigma.is_not_empty() and :


class Presolver:
    """Class that makes sigma-table"""
    def __init__(self, table_of_p):
        self.table_sigma = []
        dlina = range(len(table_of_p))
        for i in range(len(table_of_p)):
            for j in range(len(table_of_p[i])):
                if table_of_p[i][j] != -1:
                    for k in range(len(table_of_p[i][j])):
                        newsigma = Sigma(table_of_p[i][j][k], i, j)
                        self.addRows(newsigma)

    def addRows(self, sigma):
        if sigma.is_not_empty():
            row = [sigma.get_u(), sigma.get_ksi(), sigma.get_eta()]
            flag = 1
            for s in self.table_sigma:
                if s[0] == row[0]:
                    flag = 0
            if flag:
                self.table_sigma.append(row)

    def getTable(self):
        return self.table_sigma