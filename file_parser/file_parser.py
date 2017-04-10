

def parse(path):
    file = open(path, 'r')
    try:
        dimension = int(file.readline())
        knapsack_capacity = int(file.readline())
        condition_coefficients = []
        for line in file:
            condition_coefficients.append(list(map(int, line.split(' '))))
    except ValueError:
        print("File has wrong format: Cannot parse input data.\nNote: Be sure that file contains one empty line in "
              "the end.")
        return -1
    if condition_coefficients.__len__() != 3:
        print("There should be three lines with coefficients in file.\nNote: Be sure that file contains one empty "
              "line in the end.")
        return -1
    return dimension, knapsack_capacity, condition_coefficients[0], condition_coefficients[1], condition_coefficients[2]
