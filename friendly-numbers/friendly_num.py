def fun(lower, upper):
    def suma_dz(number):
        total = 0
        for i in range(1, number):
            if (number % i) == 0:
                total += i
        return total

    for i in range(lower, upper+1):
        for j in range(i+1, upper+1):
            if suma_dz(j) == i and suma_dz(i) == j:
                return i, j
