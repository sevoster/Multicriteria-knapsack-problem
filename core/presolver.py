class Sigma:
    """Structure that presents record of sigma table"""

    def __init__(self, u, ksi, eta):
        self.u = u
        self.ksi = ksi
        self.eta = eta

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
                        new_sigma = Sigma(table_of_p[i][j][k], i + 1, j + 1)
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
