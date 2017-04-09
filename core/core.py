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
        if a[0] <= j+1:
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
            if (vectors[0] <= vector2[0] and vectors[1] < vector2[1]) or (vectors[0] < vector2[0] and vectors[1] <= vector2[1]):
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

