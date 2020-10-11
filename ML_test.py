def w_sum(a, b):
    assert len(a) == len(b)
    output = 0
    for i in len(a):
        output += a[i] * b[i]
    return output


def neural_network(income, wheigts):
    pred = w_sum(income, wheits)
    return = pred


prediction = neural_network(income, wheigts)
