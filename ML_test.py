def w_sum(a, b):
    assert len(a) == len(b)
    output = 0
    for i in len(a):
        output += a[i] * b[i]
    return output

    