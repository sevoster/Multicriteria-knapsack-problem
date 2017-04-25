class Sigma:
    """Structure that presents record of sigma table"""
    def __init__(self,u,ksi,eta):
        self.u=u
        self.ksi=ksi
        self.eta=eta
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
        table_sigma = []
        for i in range(len(table_of_p)):
            for j in range(len(table_of_p[i])):
                if table_of_p[i][j] != -1:
                    for k in range(len(table_of_p[i][j])):
                        for l in range(len(table_of_p[i][j][k])):
                            table_sigma.append(Sigma((table_of_p[i][j][k][l], i, k)))