import numpy as np

devInput = """ 
ITA BEL GER SWE AUT FRA
3
MOC 1 98 58 66 74 90 82
BEZP 1 8 0 5 3 7 10
KOSZT -1 400 800 1000 600 200 600
3 0 0
2 0 2
5 100 300
"""
inputLineNr = 0
dev = True


def get_input(n):
    global inputLineNr, dev
    if dev:
        inputLineNr += 1
        print(n, end="")
        x = devInput.split('\n')[inputLineNr]
        print(x)
        return x
    else:
        return input(n)


def calcHowGood(var1, var2, q, p, gain_or_cost):
    diff = var1 - var2
    diff = diff * gain_or_cost
    if diff <= 0:
        return 0
    else:
        if diff >= p:
            return 1
        if q <= diff <= p:
            return np.interp([diff], [q, p], [0, 1])[0]
        else:
            return 0


if __name__ == '__main__':
    names = [x.strip() for x in get_input("podaj nazw rzeczów po spacji\n").strip().split(' ')]
    attr_count = int(get_input("ile atrybutów?\n"))
    attr_names = []
    values = []
    attr_params = []
    gain_costs = []
    for _ in range(len(names)):
        values.append([])
    for _ in range(attr_count):
        a = [x.strip() for x in get_input("podaj kolejny atrybut z wartosciami po spacji\n").strip().split(' ')]
        attr_names.append(a[0])
        gain_costs.append(int(a[1]))
        for i in range(len(a[2:])):
            values[i].append(float(a[i + 2]))
    for i in range(attr_count):
        attr_params.append([float(x.strip()) for x in
                            get_input("k q p atrybutu {} po spacji\n".format(attr_names[i])).strip().split(' ')])

    sum_of_weights = 0.
    for p in attr_params:
        sum_of_weights += p[0]

    matrix = []
    print()
    for i in range(len(names)):
        matrix.append([])
        for j in range(len(names)):
            print('{} vs {}'.format(names[i], names[j]))
            print('nazwa - v1 v2 k q p wyliczone')
            v = 0.
            for k in range(attr_count):
                v1 = calcHowGood(values[i][k], values[j][k], attr_params[k][1], attr_params[k][2], gain_costs[k]) * \
                     attr_params[k][0]
                v += v1
                print('{} - {} {} {} {} {} {}'.format(attr_names[k][:3], values[i][k], values[j][k], attr_params[k][0],
                                                      attr_params[k][1], attr_params[k][2], v1 / sum_of_weights))
            v /= sum_of_weights
            matrix[i].append(v)
            print(v)
            print()
    print("    ", '  '.join(names))
    for i in range(len(matrix)):
        print(names[i], end=" ")
        for j in matrix[i]:
            print("%.2f" % j, end=" ")
        print()
