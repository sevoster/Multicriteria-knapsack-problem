class Table:
    """"Table Creation"""

    def __init__(self, task):
        self.count = task.dimension
        self.weight = task.knapsack_capacity
        self.weights = task.limitation_coefficients
        self.costs1 = task.first_criterion_coefficients
        self.costs2 = task.second_criterion_coefficients
        self.table = []
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

    def create_table(self):
        self.recurs_fill_table(self.count - 1, self.weight - 1)
        return self.table

    @staticmethod
    def vector_sum(first, sec):
        result = []
        for vectors in first:
            tmp_result = []
            for element in range(2):
                tmp_result.append(vectors[element] + sec[element])
            result.append(tmp_result)
        return result

    @staticmethod
    def vector_filter(variety):
        """Remove same or least vectors"""
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

    def recurs_fill_table(self, count, weight):
        if self.table[count][weight] != -1:
            return self.table[count][weight]
        else:
            self.table[count][weight] = self.vector_filter(self.recurs_fill_table(count - 1, weight) +
                                                           self.get_second_for_recurs(weight, count))
            return self.table[count][weight]

    def get_second_for_recurs(self, weight, count):
        if weight - self.weights[count] >= 0:
            return self.vector_sum(self.recurs_fill_table(count - 1, weight - self.weights[count]),
                                  [self.costs1[count], self.costs2[count]])
        else:
            return [[0, 0]]
