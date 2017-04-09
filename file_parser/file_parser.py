
def parse(path):
    file = open(path, 'r')
    dimension = int(file.readline())
    knapsack_capacity = int(file.readline())
    condition_coefficients = []
    for line in file:
        condition_coefficients.append(list(map(int, line.split(' '))))
    return dimension, knapsack_capacity, condition_coefficients