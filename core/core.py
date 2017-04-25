table = []
a = []
b = []
c = []


def gettable(count, weight, weights, costs1, costs2):
    global table, a, b, c
    a = weights
    b = costs1
    c = costs2
    for i in range(count):
        string = []
        for j in range(weight):
            string.append(-1)
        table.append(string)
    for j in range(weight):
        if a[0] <= j + 1:
            table[0][j] = [[b[0], c[0]]]
        else:
            table[0][j] = [[0, 0]]
    rec_fill_table(count - 1, weight - 1)
    return table


def get_sum(first, sec):
    res = []
    for vectors in first:
        tic_res = []
        for el in range(2):
            tic_res.append(vectors[el] + sec[el])
        res.append(tic_res)
    return res


def do_filter(variety):
    result = []
    for vectors in variety:
        not_bad = True
        for vector2 in variety:
            if (vectors[0] <= vector2[0] and vectors[1] < vector2[1]) or (
                    vectors[0] < vector2[0] and vectors[1] <= vector2[1]):
                not_bad = False
        if not_bad:
            if vectors not in result:
                result.append(vectors)
    return result


def rec_fill_table(count, weight):
    global table, a, b, c
    if table[count][weight] != -1:
        return table[count][weight]
    else:
        first = rec_fill_table(count - 1, weight)
        sec = []
        if weight - a[count] >= 0:
            sec = get_sum(rec_fill_table(count - 1, weight - a[count]), [b[count], c[count]])
        else:
            sec = [[0, 0]]
        table[count][weight] = do_filter(first + sec)
    return table[count][weight]


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
        for i in range(len(table_of_p)):
            for j in range(len(table_of_p[i])):
                if table_of_p[i][j] != -1:
                    for k in range(len(table_of_p[i][j])):
                        newsigma = Sigma(table_of_p[i][j][k], i, j)
                        self.addRows(newsigma)

    def add_rows(self, sigma):
        if sigma.is_not_empty():
            row = [sigma.get_u(), sigma.get_ksi(), sigma.get_eta()]
            flag = 1
            for s in self.table_sigma:
                if s[0] == row[0]:
                    flag = 0
            if flag:
                self.table_sigma.append(row)

    def get_table(self):
        return self.table_sigma
