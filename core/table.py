class Table:
    """"Table Creation"""

    def __init__(self, task):
        self.table = []
        self.count = task.dimension
        self.weight = task.knapsack_capacity
        self.weights = task.limitation_coefficients
        self.costs1 = task.first_criterion_coefficients
        self.costs2 = task.second_criterion_coefficients

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
