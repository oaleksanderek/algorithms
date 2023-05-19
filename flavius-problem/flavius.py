def fun(num):
    l = num - (1 << (num.bit_length() - 1))
    result = 2*l + 1

    return result
